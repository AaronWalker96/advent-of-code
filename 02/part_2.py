"""
- 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
- 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
- 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
- 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""

# Imports
import csv


def compute(intcode, index):
    # Get indexes
    index_first_num = intcode[index+1]
    index_second_num = intcode[index+2]
    insert_at = intcode[index+3]
        
    # Addition code 
    if intcode[index] == 1:
        intcode[insert_at] = intcode[index_first_num] + intcode[index_second_num]
        return intcode

    # Multiplication code
    elif intcode[index] == 2:
        intcode[insert_at] = intcode[index_first_num] * intcode[index_second_num]
        return intcode

    # Something's gone wrong...
    else:
        raise Exception("Operator not recognised...")

    return intcode


def main():

    for noun in range(100):
        for verb in range(100):
            index = 0  # Start at position 0
            with open('intcode.csv', 'r') as f:
                reader = csv.reader(f)
                intcode = list(reader)[0]
                intcode = [ int(x) for x in intcode ]  # Cast the str values to int

            intcode[1] = noun
            intcode[2] = verb

            # Loop until we hit a 99
            while intcode[index] != 99:
                intcode_computed = compute(intcode, index)  # Compute this chunk of intcode
                index += 4  # Look at the next chunk of intcode

            if intcode_computed[0] == 19690720:
                print('Found match!')
                print(f'Noun: {noun}')
                print(f'Verb: {verb}')
                break


if __name__ == "__main__":
    main()