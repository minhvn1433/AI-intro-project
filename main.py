import sys
import time

import pyautogui
import keyboard

from game import Game


if __name__ == '__main__':
    # Get number of rows, columns
    mode = sys.argv[1]
    if mode == 'beginner':
        nrows, ncols, nmines = 9, 9, 10
    elif mode == 'intermediate':
        nrows, ncols, nmines = 16, 16, 40
    elif mode == 'expert':
        nrows, ncols, nmines = 16, 30, 99
    else:
        pass
    
    # Get top left corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    right, bottom = pyautogui.position()

    # Calculate width and height of a cell
    width, height = (right - left) / ncols, (bottom - top) / nrows

    # Play the game
    num_all_covered = 1000
    game = Game(nrows, ncols, nmines, width, height, left, top)
    while True:
        img = pyautogui.screenshot()
        game.update_field(img)
        if game.num_all_covered() != num_all_covered:
            num_all_covered = game.num_all_covered()
            game.solve()
        else:
            break
        time.sleep(0.05)