"""
- For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
- For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
- For a mass of 1969, the fuel required is 654.
- For a mass of 100756, the fuel required is 33583.
"""

# Imports
import math
import csv


def calculate_fuel_for_mass(mass, cumulative_fuel):
    fuel = math.floor(mass/3) - 2
    if fuel >= 0:
        cumulative_fuel += fuel
        return calculate_fuel_for_mass(fuel, cumulative_fuel)
    else:
        return cumulative_fuel


def main():
    total_fuel_required = 0

    with open('inputs.csv', 'r') as f:
        reader = csv.reader(f)
        modules = list(reader)
    
    for module in modules:
        total_fuel_required += calculate_fuel_for_mass(int(module[0]), 0)

    print(f'Total fuel required: {total_fuel_required}')


if __name__ == "__main__":
    main()