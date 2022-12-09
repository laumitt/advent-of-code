with open('day2input.txt') as f:
    lines = f.readlines()

commands = []
for i in range(len(lines)):
    commands.append(lines[i])
num_com = len(commands)

"""
# part 1
horiz = 0
depth = 0
for i in range(num_com):
    curr_com = commands[i]
    if curr_com[0] == "f":
        horiz = horiz + int(curr_com[8])
    elif curr_com[0] == "d":
        depth = depth + int(curr_com[5])
    elif curr_com[0] == "u":
        depth = depth - int(curr_com[3])

result = horiz * depth

print("final horizontal ", horiz)
print("final depth ", depth)
print("result ", result)
"""

# part 2
horiz = 0
depth = 0
aim = 0
for i in range(num_com):
    curr_com = commands[i]
    if curr_com[0] == "f":
        horiz = horiz + int(curr_com[8])
        depth = depth + aim*int(curr_com[8])
    elif curr_com[0] == "d":
        aim = aim + int(curr_com[5])
    elif curr_com[0] == "u":
        aim = aim - int(curr_com[3])

result = horiz * depth

print("final horizontal ", horiz)
print("final depth ", depth)
print("result ", result)
