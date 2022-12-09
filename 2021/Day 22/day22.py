import copy
day = '22'
test = 2
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

class Cube():
  def __init__(self,x,y,z,state):
    self.x = x
    self.y = y
    self.z = z
    self.state = state

start_state = "Off"
low_x_lim = -50
high_x_lim = 50
low_y_lim = -50
high_y_lim = 50
low_z_lim = -50
high_z_lim = 50
cubes = []
on_count = 0

for a in range(abs(low_x_lim) + high_x_lim):
  for b in range(abs(low_y_lim) + high_y_lim):
    for c in range(abs(low_z_lim) + high_z_lim):
      d = Cube(a,b,c,start_state)
      cubes.append(copy.deepcopy(d))

for line in input:
  if line[1] == "n":
    comm = "On"
    lims = line[3:].split(",")
  elif line[1] == "f":
    comm = "Off"
    lims = line[4:].split(",")
  low_x = int(lims[0][2:].split(".")[0])
  high_x = int(lims[0][2:].split(".")[2])
  low_y = int(lims[1][2:].split(".")[0])
  high_y = int(lims[1][2:].split(".")[2])
  low_z = int(lims[2][2:].split(".")[0])
  high_z = int(lims[2][2:].split(".")[2])

  for a in cubes:
    if low_x <= a.x <= high_x:
      if low_y <= a.y <= high_y:
        if low_z <= a.z <= high_z:
          a.state = comm
          # print("cube at", a.x, a.y, a.z, "set to", a.state)

for a in cubes:
  if a.state == "On":
    on_count += 1
print(on_count)
  