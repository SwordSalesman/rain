# rain.py
# turn your console into a soothing fall window
# by jack way
# feb 2021

import numpy as np
import random as rand
import time

sky = np.zeros((25, 80), str)
sky[True] = ' '

print("deez nuts")

clear_str = ''
for i in range(100): clear_str += '\n'

while(True):
    print(clear_str)

    # loop through columns for falling drops
    for col_num in range(len(sky[0])):        
        # loop through rows
        fall = False
        for i in range(len(sky[:,col_num])):
            if sky[:,col_num][i] == '|':
                sky[:,col_num][i] = ' '
                fall = True
            elif sky[:,col_num][i] == '*':
                if rand.random() < 0.3: sky[:,col_num][i] = ' '
            elif fall:
                # last row, i.e. 'the ground'
                if i == len(sky[:,col_num]) - 1:    
                    sky[:,col_num][i] = '*'
                else:
                    sky[:,col_num][i] = '|'
                fall = False

        if sky[:,col_num][0] == ' ' and rand.random() < 0.10:
            sky[:,col_num][0] = '|'

    # construct output string
    out = ''
    for row_num in range(len(sky)):
        for col_num in range(len(sky[row_num])):
            out += sky[row_num][col_num]
        out += '\n'
    
    print(out, end='')
    time.sleep(0.09)