import pyautogui
import random
import time
import numpy as np
import copy
res = []
a = [0,0,0]
def backtrack(i):
	for j in [0, 1]:
		a[i] = j
		if i == 2:
			res.append(copy.deepcopy(a))
		else:
			backtrack(i + 1)
backtrack(0)
print()
for ele in res:
    print(ele)

# pyautogui.mouseInfo()

# list = [[1,2,3,7], [1,5,3,2], [1,8,3,9], [1,7,3,3], [1,3,3,4]]
# new_res = []
# array = np.array(list).transpose()
# index = - 1
# for row in array:
#     index += 1
#     res = all(element == row[0] for element in row)
#     if res:
#         new_res.append(row[0])
#     else:
#         new_res.append(0)
# print(array)
# print(list)
# for ele in new_res:
#     print(ele)

# res = [['covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'flag', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'flag', 
# 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'flag', 'covered', 'covered', 
# 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'flag', 'covered', 
# 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'flag'],
# ['covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'flag', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 
# 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 
# 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 
# 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered'],
# ['covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 
# 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag'],
# ['covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 
# 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'flag', 'covered', 'covered', 'covered'],
# ['covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'flag', 'covered', 'covered', 'covered', 
# 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'flag', 'covered', 'flag', 'flag'],
# ['flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered'],
# ['flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'flag', 'covered', 'flag', 'flag', 'covered', 'covered'],
# ['flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'flag', 'flag'],
# ['flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'flag', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered', 'covered']]
# for row in range(len(res)):
#     for col in range(22):
#         if res[row][col] == 'covered':
#             res[row][col] = 0
#         else:
#             res[row][col] = 1
# array = np.array(res).transpose()
# for row in array:
#     print(row)
#     bool = np.all(row == row[0])
#     print(bool)