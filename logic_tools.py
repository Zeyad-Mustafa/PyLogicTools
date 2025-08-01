# ==============================================================================
# PySpiceNet: A Pythonic SPICE Simulation Wrapper
# ==============================================================================
# This script provides a starting point for a Python project that automates
# circuit simulation tasks, a common activity in semiconductor and chip design.
# It showcases how to:
# 1. Generate a SPICE netlist programmatically.
# 2. Interface with an external simulator (Ngspice) using the subprocess module.
# 3. Parse and analyze the simulation output data.
# 4. Visualize the results using Matplotlib.
#
# Prerequisites:
# - Ngspice installed and accessible from your system's PATH.
# - Python libraries: matplotlib, numpy
#   (Install with: `pip install matplotlib numpy`)
# ==============================================================================

import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration ---
# Set the name for your temporary SPICE netlist file
NETLIST_FILENAME = 'common_source_amp.sp'
# Set the name for the simulation output file
OUTPUT_FILENAME = 'simulation_output.csv'

def generate_netlist():
    """
    Generates a SPICE netlist for a simple common-source amplifier circuit.

    This function programmatically creates the content of a .sp file as a string.
    In a full project, this could be extended to accept parameters and generate
    much more complex circuits.

    Returns:
        str: The complete SPICE netlist content.
    """
    # Define a simplified SPICE model for an NMOS transistor.
    # In a real project, this would be imported from a technology library file.
    model_definition = """
.model nmos_model nmos level=1 vto=0.5 k=100e-6 lambda=0.01
"""
    # Create the circuit description.
    # This circuit includes a DC sweep of the input voltage V_in.
    circuit_description = f"""
* Common-Source Amplifier with DC Sweep Analysis

* Components
Vdd Vdd 0 5V          * Power supply
Vbias Vbias 0 1.5V    * Bias voltage
Vin Vin 0 0           * Input voltage, will be swept
R_D Vdd Vout 10e3     * Drain resistor (10 kOhm)
M1 Vout V_in Vbias 0 nmos_model L=1u W=10u * NMOS transistor with V_in tied to gate
M2 V_in Vbias 0 0 nmos_model L=1u W=10u * Transistor M2 used as diode-connected load to apply V_in on M1. We can also simply define Vin as Vin Vin 0 0 and sweep it.
R_in V_in Vbias 1e6     * Input resistance (1 MOhm)
* Subcircuit for the common-source amplifier
.subckt common_source_amp V_in V_out
R_D Vdd V_out 10e3
M1 V_out V_in 0 0 nmos_model L=1u W=10u
.ends

* Analysis
.dc V_in 0 3 0.01       * DC sweep of V_in from 0V to 3V with 0.01V step

* Control block for simulation and data export
.control
  run
  let V_in = V(V_in)
  let V_out = V(V_out)
  set wr_singlescale = 1
  write {OUTPUT_FILENAME} V_in V_out
.endc
.end
"""
    netlist = model_definition + circuit_description
    return netlist

def run_simulation(netlist_path):
    """
    Runs the SPICE simulation using Ngspice.

    Args:
        netlist_path (str): The path to the SPICE netlist file.

    Returns:
        tuple: A tuple containing the stdout and stderr from the Ngspice process.
               Returns (None, None) if the file doesn't exist.
    """
    if not os.path.exists(netlist_path):
        print(f"Error: Netlist file not found at {netlist_path}")
        return None, None

    print(f"Running simulation with ngspice on {netlist_path}...")
    try:
        # Use subprocess to call ngspice with the netlist file
        result = subprocess.run(
            ['ngspice', '-b', netlist_path],
            capture_output=True,
            text=True,
            check=True
        )
        print("Simulation completed successfully.")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Error during ngspice execution: {e.stderr}")
        return e.stdout, e.stderr
    except FileNotFoundError:
        print("Error: ngspice command not found. Please ensure it's installed and in your PATH.")
        return None, "Ngspice not found."

def parse_and_plot_results(output_path):
    """
    Parses the simulation output CSV file and plots the results.

    Args:
        output_path (str): The path to the CSV output file from ngspice.
    """
    if not os.path.exists(output_path):
        print(f"Error: Output file not found at {output_path}")
        return

    print(f"Parsing and plotting results from {output_path}...")
    try:
        # Load data from the CSV file.
        # The first row is headers, so we skip it.
        data = np.genfromtxt(output_path, delimiter=',', names=True)
        
        # The columns are defined in the .control block as V_in and V_out.
        # The names from np.genfromtxt will be 'V_in' and 'V_out'.
        input_voltage = data['V_in']
        output_voltage = data['V_out']
        
        # Create a plot using matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(input_voltage, output_voltage, label='V_out vs. V_in')
        plt.title('Common-Source Amplifier DC Transfer Curve')
        plt.xlabel('Input Voltage (V)')
        plt.ylabel('Output Voltage (V)')
        plt.grid(True)
        plt.legend()
        plt.show()

        print("Plot displayed successfully.")

    except Exception as e:
        print(f"An error occurred while parsing or plotting: {e}")

def cleanup(file_list):
    """
    Removes temporary files created during the process.
    """
    for file_path in file_list:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Cleaned up {file_path}")


# --- Main execution block ---
if __name__ == '__main__':
    # 1. Generate the SPICE netlist and write it to a file
    netlist_content = generate_netlist()
    with open(NETLIST_FILENAME, 'w') as f:
        f.write(netlist_content)
    print(f"Netlist saved to {NETLIST_FILENAME}")

    # 2. Run the simulation
    # The run_simulation function will handle calling ngspice and checking for errors.
    stdout, stderr = run_simulation(NETLIST_FILENAME)

    # 3. Check if the simulation was successful and if the output file was created
    if stdout is not None and os.path.exists(OUTPUT_FILENAME):
        # 4. Parse and plot the results
        parse_and_plot_results(OUTPUT_FILENAME)
    else:
        print("Skipping plotting due to simulation error or missing output file.")

    # 5. Clean up temporary files
    cleanup([NETLIST_FILENAME, OUTPUT_FILENAME])

