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

modnum_int = 98999956599999
valid_num = False
a = 0

while valid_num == False:
  if a % 100000 == 0:
    print(modnum_int)
  modnum_str = str(modnum_int)
  w1 = int(modnum_str[0])
  w2 = int(modnum_str[1])
  w3 = int(modnum_str[2])
  w4 = int(modnum_str[3])
  w5 = int(modnum_str[4])
  w6 = int(modnum_str[5])
  w7 = int(modnum_str[6])
  w8 = int(modnum_str[7])
  w9 = int(modnum_str[8])
  w10 = int(modnum_str[9])
  w11 = int(modnum_str[10])
  w12 = int(modnum_str[11])
  w13 = int(modnum_str[12])
  w14 = int(modnum_str[13])
  
  z1 = 14 * (w1 + 8)
  z2 = z1 * ((25 * ((z1 % 26) + 15) + 1)) + ((w2 + 11) * ((z1 % 26) + 15))
  z3 = z2 * ((25 * ((z2 % 26) + 13) + 1)) + ((w3 + 2) * ((z2 % 26) + 13))
  if ((z3 % 26) - 10) == w4 or ((z3 % 26) - 10) == 0:
    z4 = z3 * (w4 + 11)
  else:
    z4 = ((z3/26) * ((25 * ((z3 % 26) - 10)) + 1)) * ((w4 + 11) * ((z3 % 26) - 10))
  z5 = z4 * ((25 * ((z4 % 26) + 14) + 1)) + ((w5 + 1) * ((z4 % 26) - 14))
  if ((z5 % 26) - 3) == w6 or ((z3 % 26 ) - 3) == 0:
    z6 = z5 + w6 + 5
  else:
    z6 = (z5 / 26) * ((25 * ((z5 % 26) - 3)) + 1) + ((w6 + 5) * ((z5 % 26) - 3))
  if ((z6 % 26) - 14) == w7 or ((z6 % 26) - 14) == 0:
    z7 = z6 + w6 + 10
  else:
    z7 = (z6 / 26) * ((25 * ((z6 % 26) - 14) + 1)) + ((w7 + 10) * ((z6 % 26) - 14))
  z8 = z7 * ((25 * ((z7 % 26) + 12)) + 1) + ((w8 + 6) * ((z7 % 26) + 12))
  z9 = z8 * ((25 * ((z8 % 26) + 14)) + 1) + ((w9 + 1) * ((z8 % 26) + 14))
  z10 = z9 * ((25 * ((z9 % 26) + 12)) + 1) + ((w10 + 11) * ((z9 % 26) + 12))
  if ((z10 % 26) - 6) == w11 or ((z10 % 26) - 6) == 0:
    z11 = z10 + w11 + 9
  else:
    z11 = ((z10 / 26) * ((25 * ((z10 % 26) - 6)) + 1)) + ((w11 + 9) * ((z10 % 26) - 6))
  if ((z11 % 26) - 6) == w12 or ((z11 % 26) - 6) == 0:
    z12 = z11 + w12 + 14
  else:
    z12 = ((z11 / 26) * ((25 * ((z11 % 26) - 6)) + 1)) + ((25 * ((z11 % 26) - 6)))
  if ((z12 % 26) - 2) == w13 or ((z12 % 26) - 2) == 0:
    z13 = z12 + w13 + 11
  else:
    z13 = ((z12 / 26) * ((25 * ((z12 % 26) - 2)) + 1)) + ((w13 + 11) * ((z12 % 26) - 2))
  if ((z13 % 26) - 9) == w14 or ((z13 % 26) - 9) == 0:
    z14 = z13 + ((w14 + 2) * z13)
  else:
    z14 = ((z13 / 26) * ((25 * ((z13 % 26) - 9)) + 1)) + ((w14 + 2) * ((z13 % 26) * ((25 * ((z13 % 26) - 9)) + 1)))

  if z14 == 0:
    break
    print(modnum_str, z14)
  modnum_int -= 1
  a += 1