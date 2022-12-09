with open('day3input.txt') as f:
    lines = f.readlines()

diagno = []
for a in range(len(lines)):
    diagno.append(lines[a])

# part 1
rows = len(diagno)
cols = 12 #ew
num_zero = [0]*cols
num_ones = [0]*cols
for i in range(rows):
    for j in range(cols):
        current = diagno[i]
        if int(current[j]) == 0:
            num_zero[j] = num_zero[j] + 1
        elif int(current[j]) == 1:
            num_ones[j] = num_ones[j] + 1

most_com = [0]*cols
less_com = [0]*cols
for b in range(cols):
    if num_zero[b] > num_ones[b]:
        most_com[b] = 0
        less_com[b] = 1
    elif num_zero[b] < num_ones[b]:
        most_com[b] = 1
        less_com[b] = 0

mc = ""
lc = ""
for c in range(cols):
    mc = mc + str(most_com[c])
    lc = lc + str(less_com[c])

gamma = int(mc,2)
epsil = int(lc,2)
power = gamma * epsil
print(power)
