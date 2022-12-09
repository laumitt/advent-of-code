# import copy
# import numpy as np
import math

day = '24'
test = 0
if test == 1:
    with open('day'+ day + 'input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('day'+ day + 'input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('day'+ day + 'input.txt') as f:
        lines = f.readlines()

input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

w = 0
x = 0
y = 0
z = 0

vars = [w,x,y,z]

var_dict = {
  "w" : 0,
  "x" : 1,
  "y" : 2,
  "z" : 3
}

# model_number = 99999999999999
model_number = 99919999989000
valid_num = False
a = 0

while valid_num == False:
  if a % 1000 == 0:
    print("model number", model_number)
  vars = [0, 0, 0, 0]
  for i in range(14):
    digit = int(str(model_number)[i])
    for line in input:
      command = line.split(" ")
      # print("command", command)
      # print("variables", vars)
      comm = command[0]
      var1 = command[1]
      if comm == "inp":
        vars[0] = digit
        # print('input digit', digit)
        # print("input vars", vars)
      else:
        if command[2] in var_dict:
          var2 = command[2]
          # print("var2", vars[var_dict[var2]])
          if comm == "add":
            vars[var_dict[var1]] = vars[var_dict[var1]] + vars[var_dict[var2]]
          elif comm == "mul":
            vars[var_dict[var1]] = vars[var_dict[var1]] * vars[var_dict[var2]]
          elif comm == "div":
            vars[var_dict[var1]] = math.floor(vars[var_dict[var1]]/vars[var_dict[var1]])
          elif comm == "mod":
            vars[var_dict[var1]] = vars[var_dict[var1]] % vars[var_dict[var2]]
          elif comm == "eql":
            if vars[var_dict[var1]] == vars[var_dict[var2]]:
              vars[var_dict[var1]] = 1
            else:
              vars[var_dict[var1]] = 0
          else:
            print("var2 comm error")
        else:
          num = int(command[2])
          # print('num', num)
          if comm == "add":
            vars[var_dict[var1]] = vars[var_dict[var1]] + num
          elif comm == "mul":
            vars[var_dict[var1]] = vars[var_dict[var1]] * num
          elif comm == "div":
            vars[var_dict[var1]] = math.floor(vars[var_dict[var1]]/num)
          elif comm == "mod":
            vars[var_dict[var1]] = vars[var_dict[var1]] % num
          elif comm == "eql":
            if vars[var_dict[var1]] == num:
              vars[var_dict[var1]] = 1
            else:
              vars[var_dict[var1]] = 0
          else:
            print("num comm error")
        # print("a", type(a), a, "b", type(b), b)
  if vars[3] == 0:
    print("valid number:", model_number)
    valid_num = True
    break
  model_number -= 1
  a += 1

# print("result variables", vars)