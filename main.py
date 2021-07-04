# Erin-Louise Connolly
# Game of Life
# 4/7/2021
import random
import time

def generate_grid(xsize,ysize):
    # Sparse matrix to represent infinite grid
    # Stores only live cell positions, dead are not stored. 
    # Takes in x and y size of grid and generates a random number of live cells.
    live_cells = [(1,2),(2,2),(3,2)]

    return live_cells
    
def print_grid(xsize,ysize,live_cells):
    #Takes in positions of live cells and prints out a view of them and surrounding dead cells
    # 0 represents a dead cell, 1 represents a live cell
    for y in range(ysize):
            grid_string = ' '.join( ' 1 ' if (x,y) in live_cells else ' 0 ' for x in range(xsize))
            print(grid_string)
    print("")
    return

def find_neighbours(live_cells,xsize,ysize):
    # Each cell has up to eight neighbours - top left, top, top right, left, right, bottom left, bottom, right
    neighbours_dict = {}
    live_neighbours_dict = {}
    for x in range(xsize):
        for y in range(ysize):
            live_count=0
            neighbour_list = []
            neighbour_list.append((x-1,y-1)) # top left
            neighbour_list.append((x,y-1))   # top
            neighbour_list.append((x+1,y-1)) # top right
            neighbour_list.append((x-1,y))   # left
            neighbour_list.append((x,y+1))   # right
            neighbour_list.append((x-1,y+1)) # bottom left
            neighbour_list.append((x+1,y))   # bottom
            neighbour_list.append((x+1, y+1)) #bottom right
            neighbours_dict.update({(x,y):neighbour_list})
            for neighbour in neighbour_list:
                if neighbour in live_cells:
                    live_count+=1
            live_neighbours_dict.update({(x,y):live_count})

    return neighbours_dict,live_neighbours_dict


def main():
    #Loops infinitely.
    xsize = 5
    ysize = 5
    live_cells = generate_grid(xsize,ysize)

    while True:
        print_grid(xsize,ysize,live_cells)
        neighbours_dict,live_neighbours_dict = find_neighbours(live_cells,xsize,ysize)
        
        for cell in live_cells: 
            if live_neighbours_dict.get(cell) <2 or live_neighbours_dict.get(cell) >3:
                live_cells.remove(cell)
        
        for x in range(xsize):
            for y in range(ysize):
                cell = (x,y)
                if cell not in live_cells and live_neighbours_dict.get(cell) == 3:
                    live_cells.append(cell)

        time.sleep(5)


main()
