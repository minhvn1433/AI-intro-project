import random
import copy

import numpy as np
import pyautogui
import termcolor

pyautogui.PAUSE = 0.01

colors = np.array([
    [189, 189, 189], # 0
    [0, 0, 255], # 1
    [0, 123, 0], # 2 
    [255, 0, 0], # 3
    [0, 0, 123], # 4
    [123, 0, 0], # 5
    [0, 123, 123], # 6
    [0, 0, 0], # 7
    [123, 123, 123], # 8
    [255, 255, 255] # 9 covered
])

colors_no0 = np.array([
    [1000, 1000, 1000], # not 0
    [0, 0, 255], # 1
    [0, 123, 0], # 2 
    [255, 0, 0], # 3
    [0, 0, 123], # 4
    [123, 0, 0], # 5
    [0, 123, 123], # 6
    [0, 0, 0], # 7
    [123, 123, 123], # 8
    [255, 255, 255] # 9 covered
])

colors_dict = {
    '0' : 'grey',
    '1' : 'blue',
    '2' : 'green',
    '3' : 'red',
    '4' : 'magenta',
    '5' : 'red',
    '6' : 'cyan',
    '7' : 'yellow',
    '8' : 'yellow',
    '.' : 'white',
    'F' : 'white'
} 


class Cell: 
    def __init__(self, r, c):
        ''' Initiatlize a cell with coordinates (r, c)
        '''
        self.r, self.c = r, c
        self.value = 'covered' # 0-8, covered, flag
        self.visited = False # For backtrack


class Game:
    ''' Game class hold information about the game current state,
    methods to solve the field from the current state
    '''
    def __init__(self, nrows, ncols, nmines, width, height, left, top):
        self.nrows, self.ncols, self.nmines = nrows, ncols, nmines
        self.width, self.height = width, height
        self.left, self.top = left, top
        self.create_field()
    
    def create_field(self):
        ''' Initialize a field by adding cells to a two-dimensional array
        '''
        self.field = np.empty((self.nrows, self.ncols), dtype=object)
        for row in range(self.nrows):
            for col in range(self.ncols):
                self.field[row, col] = Cell(row, col)

#=========================================
# Part A: Take screenshot and update field
#=========================================
    def get_value(self, img, cell):
        ''' Get the current state of a cell from screenshot
        Return: cell value
        '''
        y_center = self.top + cell.r * self.height + 0.5 * self.height
        x_center = self.left + cell.c * self.width + 0.5 * self.width
        is_zero_cell = True
        lowest_error = 3000000

        # Check if value of a cell is zero. If it is not a zero cell, exit loop
        for y in range(int(y_center - 0.3 * self.height), int(y_center + 0.3 * self.height)):      
            color = np.array(img.getpixel((x_center, y)))
            error = np.sum(np.square(color - colors), axis = 1, keepdims = True)
            state = np.argmin(error)
            if state != 0:
                is_zero_cell = False
                break
            value = 0
        
        # Find value of a cell when already know it is not zero
        if not is_zero_cell:
            for y in range(int(y_center - 0.3 * self.height), int(y_center + 0.3 * self.height)):      
                color = np.array(img.getpixel((x_center, y)))
                error = np.sum(np.square(color - colors_no0), axis = 1, keepdims = True)
                state = np.argmin(error)  
                if np.min(error) < lowest_error:
                    lowest_error = np.min(error)
                    value = state

        # Zero cell and covered cell has same color. Check if it is a covered cell
        if is_zero_cell:
            for x in range(int(x_center - 0.5 * self.width), int(x_center - 0.3 * self.width)): 
                color = np.array(img.getpixel((x, y_center)))
                error = np.sum(np.square(color - colors), axis = 1, keepdims = True)
                state = np.argmin(error)      
                if state == 9:
                    value = 9
                    break

        return value

    def update_field(self, img):
        ''' Print the field on the terminal, modify cells (except flag)
        '''
        for row in self.field:
            for cell in row:
                if cell.value == 'flag':
                    value = 'F'
                else:
                    value = self.get_value(img, cell)
                    if value == 9:
                        value = '.'
                    else: 
                        cell.value = value
        #         print(termcolor.colored(value, colors_dict[str(value)]), end = ' ')
        #     print()
        # print()
        # print()

#=========================================
# Part B: Helper functions
#=========================================
    def num_all_covered(self):
        ''' Purpose: exit game
        Return: number of all covered cells on the field
        '''
        count = 0

        for row in self.field:
            for cell in row:
                if cell.value == 'covered':
                    count += 1

        return count

    def get_neighbors(self, cell):
        ''' Return a list of neighbor cells
        '''
        r, c = cell.r, cell.c
        neighbors = []

        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if ((row != r or col != c) and
                    (0 <= row < self.nrows) and
                    (0 <= col < self.ncols)):
                    neighbors.append(self.field[row, col])

        return neighbors
    
    def get_covered_neighbors(self, cell):
        ''' Return a list of covered neighbor cells
        '''
        covered_neighbors = []

        for neighbor in self.get_neighbors(cell):
            if neighbor.value == 'covered':
                covered_neighbors.append(neighbor)

        return covered_neighbors

    def get_numbered_neighbors(self, cell):
        ''' Return a list of "number" neighbor cells
        '''
        numbered_neighbors = []

        for neighbor in self.get_neighbors(cell):
            if neighbor.value != 'covered' and neighbor.value != 'flag':
                numbered_neighbors.append(neighbor)

        return numbered_neighbors
    
    def get_border(self):
        ''' Return a list of border cells
        '''
        border = []

        for row in self.field:
            for cell in row:
                if cell.value != 'covered' and cell.value != 'flag':
                    for neighbor in self.get_covered_neighbors(cell):
                        border.append(cell)

        return list(set(border))

    def get_frontier(self):
        ''' Return a list of frontier cells
        '''
        frontier = []
        
        for cell in self.get_border():
            for neighbor in self.get_covered_neighbors(cell):
                frontier.append(neighbor)
        
        return list(set(frontier))

    def is_subgroup(self, cell_1, cell_2):
        ''' Check if uncovered neighbors of cell 1 is a subgroup of 
        uncovered neighbors of cell 2
        Return: boolean
        '''
        res = True

        for neighbor in self.get_covered_neighbors(cell_1):
            if neighbor not in self.get_covered_neighbors(cell_2):
                res = False

        return res
    
    def get_num_covered(self, cell):
        ''' Return: int(number of covered around a cell)
        '''
        return len(self.get_covered_neighbors(cell))

    def get_num_flag(self, cell):
        ''' Return: int(number of flag around a cell)
        '''
        count = 0

        for neighbor in self.get_neighbors(cell):
            if neighbor.value == 'flag':
                count += 1

        return count
    
    def get_num_mine(self, cell):
        ''' Return: int(number of mines left around a cell)
        '''
        return int(cell.value) - self.get_num_flag(cell)

    def get_num_unvisited(self, cell):
        ''' Return: int(number of unvisited around a cell)
        '''
        count = 0

        for neighbor in self.get_covered_neighbors(cell):
            if neighbor.visited == False:
                count += 1

        return count
    
    def backtrack_helper_1(self, cell):
        ''' Return: boolean
        '''
        res = False

        for neighbor in self.get_numbered_neighbors(cell):
            if int(neighbor.value) == self.get_num_flag(neighbor):
                res = True

        return res

    def backtrack_helper_2(self, cell):
        ''' Return: boolean
        '''
        res = False

        for neighbor in self.get_numbered_neighbors(cell):
            if int(neighbor.value) == self.get_num_flag(neighbor) + self.get_num_unvisited(neighbor):
                res = True

        return res

#=========================================
# Part C: Solve algorithm
#=========================================
    def method_naive(self):
        ''' Basic algorithm to solve minesweeper
        Return: list of safe and mine cells
        '''
        safe, mines = [], []
        
        for cell in self.get_border():
            mine = self.get_num_mine(cell)
            covered = self.get_num_covered(cell)

            # No mines around
            if mine == 0:
                safe.extend(self.get_covered_neighbors(cell))

            # Number of mines left = number of unclicked cells
            if mine == covered:
                mines.extend(self.get_covered_neighbors(cell))
        
        return list(set(safe)), list(set(mines))

    def method_group(self):
        ''' A simple CSP
        Return: list of safe and mine cells
        '''
        safe, mines = [], []

        for cell_1 in self.get_border():
            for cell_2 in self.get_border():
                if self.is_subgroup(cell_1, cell_2):
                    unclicked = self.get_covered_neighbors(cell_2)
                    for ele in self.get_covered_neighbors(cell_1):
                        unclicked.remove(ele)

                    # Deduce safe cells
                    if self.get_num_mine(cell_1) == self.get_num_mine(cell_2):
                        safe.extend(unclicked)

                    # Deduce mine cells
                    if self.get_num_mine(cell_1) + len(unclicked) == self.get_num_mine(cell_2):
                        mines.extend(unclicked)
        
        return list(set(safe)), list(set(mines))
    
    def method_backtrack(self):
        ''' Enumerate all possible configuration of frontier cells
        Return: list of safe and mine cells
        '''
        safe, mines = [], []
        res = []
        cell_list = self.get_frontier()
        if len(cell_list) > 39:
            return [], []
        # for cell in cell_list:
        #     print(cell.r, cell.c)
        frontier = []
        for cell in cell_list:
            frontier.append(0) # Create frontier has same length as cell_list

        def backtrack(index):
            # Exit condition
            if index == len(frontier):
                res.append(copy.copy(frontier))
                return

            # Recursive backtrack
            if self.backtrack_helper_1(cell_list[index]) and \
                self.backtrack_helper_2(cell_list[index]):
                return
            if self.backtrack_helper_1(cell_list[index]): # Just enough flags
                cell_list[index].value = 'covered'
                cell_list[index].visited = True
                frontier[index] = 'covered'
                backtrack(index + 1)
                cell_list[index].value = 'covered'
                cell_list[index].visited = False
            elif self.backtrack_helper_2(cell_list[index]): # Not enough flags
                cell_list[index].value = 'flag'
                cell_list[index].visited = True
                frontier[index] = 'flag'
                backtrack(index + 1)
                cell_list[index].value = 'covered'
                cell_list[index].visited = False
            else:
                for value in ['covered', 'flag']:
                    cell_list[index].value = value 
                    cell_list[index].visited = True
                    frontier[index] = value
                    backtrack(index + 1)
                    cell_list[index].value = 'covered'
                    cell_list[index].visited = False
        backtrack(0)

        # Reset all cell
        for cell in cell_list:
            cell.visited = False
            cell.value = 'covered'
        
        # for ele in res:
        #     print(ele)
        array = np.array(res).transpose()
        value_list = []
        for row in array:
            bool = np.all(row == row[0])
            if bool:
                value_list.append(row[0])
            else:
                value_list.append([])

        index = -1
        for ele in value_list:
            index += 1
            if ele == 'covered':
                safe.append(cell_list[index])
            if ele == 'flag':
                mines.append(cell_list[index])

        return list(set(safe)), list(set(mines))
    
    def method_csp(self):
        pass
        # TODO: your code here

    def method_random(self):
        ''' Pick a random cell, prefer corner(for opening)
        Return: list of safe cells(random cell) and mine cells(none)
        '''
        safe, mines= [], []
        rand = []
        corner = [self.field[0,0],
        self.field[0, self.ncols - 1],
        self.field[self.nrows - 1, 0], 
        self.field[self.nrows - 1, self.ncols - 1]]

        # If all corner cells are opened, pick a random cell
        if corner[0].value != 'covered' and \
           corner[1].value != 'covered' and \
           corner[2].value != 'covered' and \
           corner[3].value != 'covered':
            for row in self.field:
                for cell in row:
                    if cell.value == 'covered':
                        rand.append(cell)
            safe.append(random.choice(rand))
        
        # Open a corner cell
        else:
            for cell in corner:
                if cell.value == 'covered':
                    safe.append(cell)
                    break

        return safe, mines
    
    def solve(self):
        ''' Go through all methods, then open safe cells and flag mine cells
        '''
        # methods = [(self.method_naive, 'Naive'),
        # (self.method_group, 'Group'),
        # (self.method_backtrack, 'Backtrack'),
        # (self.method_random, 'Random')]

        # for method, method_name in methods:
        #     safe, mines = method()
        #     if safe or mines:
        #         print(method_name)
        #         break
        
        methods = [self.method_naive, self.method_group, self.method_backtrack,
        self.method_random]

        for method in methods:
            safe, mines = method()
            if safe or mines:
                break

        for cell in safe:
            self.click(cell, 'left')
        for cell in mines:
            # self.click(cell, 'right')
            cell.value = 'flag'
            self.nmines -= 1

    def click(self, cell, button):
        y_center = self.top + cell.r * self.height + 0.5 * self.height
        x_center = self.left + cell.c * self.width + 0.5 * self.width
        pyautogui.click(x_center, y_center, button = button)
        
        
    # def get_starting_point(self,starting_point):#random starting point
	# 	if not starting_point:
	# 		start_x = random.randint(0,self.cols-1)
	# 		start_y = random.randint(0,self.rows-1)
	# 		starting_point = (start_x,start_y)
	# 	return starting_point
