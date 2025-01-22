# LED Resistor Calculator
# This script calculates the required resistor value for an LED, considering its forward voltage and desired current.
# It also adjusts the forward voltage based on the desired current if needed.

import math

def calculate_forward_voltage(vf_20ma, current_ma, n):
    """
    Adjusts the forward voltage (Vf) of the LED based on the desired current.

    Parameters:
        vf_20ma (float): Forward voltage at 20 mA (from the LED's datasheet, in volts).
        current_ma (float): Desired current through the LED (in mA).
        n (float): Constant factor depending on the LED type (typical values: 0.05-0.1 V).

    Returns:
        float: Adjusted forward voltage (in volts).
    """
    current_ratio = current_ma / 20.0  # Ratio of desired current to 20 mA
    return vf_20ma + n * math.log(current_ratio)

def calculate_resistor(v_supply, vf, current_ma):
    """
    Calculates the required resistor value for the LED.

    Parameters:
        v_supply (float): Supply voltage (in volts).
        vf (float): Forward voltage of the LED (in volts).
        current_ma (float): Desired current through the LED (in mA).

    Returns:
        float: Resistor value (in ohms).
    """
    current_a = current_ma / 1000.0  # Convert current from mA to A
    v_r = v_supply - vf  # Voltage drop across the resistor
    if v_r <= 0:
        raise ValueError("Supply voltage is too low to drive the LED with the desired current.")
    return v_r / current_a

# Main program
if __name__ == "__main__":
    # Input parameters
    v_supply = float(input("Enter supply voltage (V): "))
    vf_20ma = float(input("Enter forward voltage at 20 mA (V): "))
    current_ma = float(input("Enter desired current (mA): "))
    n = float(input("Enter LED constant factor (typical: 0.05-0.1 V): "))

    try:
        # Adjust forward voltage
        vf_adjusted = calculate_forward_voltage(vf_20ma, current_ma, n)
        print(f"Adjusted forward voltage: {vf_adjusted:.3f} V")

        # Calculate resistor value
        resistor_value = calculate_resistor(v_supply, vf_adjusted, current_ma)
        print(f"Required resistor value: {resistor_value:.2f} ohms")
    except ValueError as e:
        print(f"Error: {e}")
