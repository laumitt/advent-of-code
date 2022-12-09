import copy
# import numpy as np
import math 
day = '12'
test = 1
if test == 1:
    with open('day'+ day + 'input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('day'+ day + 'input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('day'+ day + 'input.txt') as f:
        lines = f.readlines()

input = [int(i) for i in lines[0].split(',')]
# or
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

input = [i for i in lines[0].split(' ')]
xlims = [i for i in input[2][2:-1].split('.')]
ylims = [i for i in input[3][2:].split('.')]
x1 = int(xlims[0])
x2 = int(xlims[2])
y1 = int(ylims[0])
y2 = int(ylims[2])

