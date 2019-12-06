"""
wire 1 = R8,U5,L5,D3
wire 2 = U7,R6,D4,L4
closest intersection = 6
"""

# Imports 
import numpy as np
import csv


def get_wires(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)[0]


def trace_wire(wire):
    # TODO 
    for direction in wire:
        print(direction)



def draw_wire(wire, grid, start_x, start_y, wire_num):#

    direction = wire[0]
    distance = int(wire[1:])

    # If up
    if direction == "U":

        for i in range(distance):
            if grid[(start_y-1) - i,start_x] == 0:  # 0 indicates no wire
                grid[(start_y-1) - i,start_x] = wire_num  
            else:  # There's a wire here!
                grid[(start_y-1) - i,start_x] = 5  # 5 indicates crossed wire
        
        return start_x, start_y-distance
        

    # If down
    elif direction == "D":

        for i in range(distance):
            if grid[(start_y+1) + i,start_x] == 0:  # 0 indicates no wire
                grid[(start_y+1) + i,start_x] = wire_num
            else:  # There's a wire here!
                grid[(start_y+1) + i,start_x] = 5  # 5 indicates crossed wire
        
        return start_x, start_y+distance

    # If left
    elif direction == "L":

        for i in range(distance):
            if grid[start_y,(start_x-1) - i] == 0:  # 0 indicates no wire
                grid[start_y,(start_x-1) - i] = wire_num
            else:  # There's a wire here!
                grid[start_y,(start_x-1) - i] = 5  # 5 indicates crossed wire
        
        return start_x-distance, start_y

    # If right
    elif direction == "R":

        for i in range(distance):
            if grid[start_y,(start_x+1) + i] == 0:  # 0 indicates no wire   
                grid[start_y,(start_x+1) + i] = wire_num
            else:  # There's a wire here!
                grid[start_y,(start_x+1) + i] = 5  # 5 indicates crossed wire
        
        return start_x+distance, start_y

    else:
        print('Unknown direction...')


def main():

    start_x = 10000
    start_y = 10000

    wire_1 = get_wires('wire_1_test.csv')
    wire_2 = get_wires('wire_2_test.csv')

    grid = np.zeros(shape=(20000,20000), dtype=int)

    grid[start_y,start_x] = 3  # 3 indicates starting point

    for wire in wire_1:
        start_x, start_y = draw_wire(wire, grid, start_x, start_y, 1)

    # Reset the start
    start_x = 10000
    start_y = 10000
    
    for wire in wire_2:
        start_x, start_y = draw_wire(wire, grid, start_x, start_y, 2)
    
    # Reset the start
    start_x = 10000
    start_y = 10000

    crosses = np.argwhere(grid == 5)
    origin = np.where(grid == 3)
    results = [None] * len(crosses)


    for index, cross in enumerate(crosses):
        results[index] = abs(cross[0]-origin[0]) + abs(cross[1]-origin[1])

    results.sort() 
  
    # printing the first element 
    print("Closest cross is:", *results[:1][0]) 

    # Trace wire
    trace_wire(wire_1)


if __name__ == "__main__":
    main()