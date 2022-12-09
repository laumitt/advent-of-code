with open('day1input.txt') as f:
    lines = f.readlines()

depths = []
for i in range(len(lines)):
    depths.append(int(lines[i]))

"""
# part 1
deltas = []
num_inc = 0

for i in range(len(depths)):
    if i >= 1:
        if depths[i] > depths[i-1]:
            num_inc = num_inc + 1
print(num_inc)
"""

# part 2
num_depths = len(depths)
num_inc_w = 0

for i in range(num_depths):
    if i <= num_depths-4:
        sum_win1 = depths[i] + depths[i+1] + depths[i+2]
        sum_win2 = depths[i+1] + depths[i+2] + depths[i+3]
        if sum_win1 < sum_win2:
            num_inc_w = num_inc_w + 1

print(num_inc_w)
