import numpy as np


class Cell:
    ''' A cell represents a location in a two-dimensional field, where
    coordinates are given by (x, y)
    '''

    def __init__(self, x, y):
        ''' Initiatlizes a cell with coordinates (x, y)
        '''
        self.x = x
        self.y = y
        # TODO: your code here
        pass


class Field:
    ''' A field is a rectangular region containing all cell, implemented 
    by a two-dimensional array
    '''

    def __init__(self, num_rows, num_cols):
        ''' Initializes the field
        '''
        self.num_rows = num_rows
        self.num_cols = num_cols
        # TODO: your code here
    
    def create_field(self):
        ''' Create the field by adding cells to a two-dimensional array
        '''
        self.field = []
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                row.append(Cell(x, y))
            self.field.append(row)
    
    def print_field(self, img):
        ''' Print the field on the terminal for debugging

        img: pyautogui image
        '''
        # TODO: your code here
        pass

    def click_cell(self):
        # TODO: your code here
        pass