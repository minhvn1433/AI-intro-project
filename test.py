import pyautogui
import random
import time
# a = [0,0,0,0]
# def backtrack(i):
# 	for j in ['covered', 'flag']:
# 		a[i] = j
# 		if i == 3: 
# 			print(a)
# 		else:
# 			backtrack(i + 1)
# backtrack(0)
# print(a)

# pyautogui.mouseInfo()

res = []
cell_list = []
frontier = [0, 0, 0, 0]
def backtrack(index): #use zip to get column
    # Exit condition
    if index == len(frontier):
        print(frontier)
        res.append(frontier)
        return

    # Recursive backtrack
    if False: # vừa đủ mìn
            cell_list[index].value = 'covered'
            frontier[index] = 'covered'
            backtrack(index + 1)
    elif False: # thiếu mìn (value = flag + unvisited)
            cell_list[index].value = 'flag'
            frontier[index] = 'flag'
            backtrack(index + 1)
    else:
        for value in ['covered', 'flag']:
            #cell_list[index].value = value 
            frontier[index] = value
            backtrack(index + 1)
backtrack(0)