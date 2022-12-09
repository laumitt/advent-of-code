import copy
day = '20'
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

input_image = []
im_alg = ""
for a in range(len(lines)):
  if a == 0:
    im_alg = lines[a].strip()
  else:
    input_image.append(lines[a].strip())
# print("image enhancement algorithm", im_alg)
# print("input image", input_image)

# for each input image pixel [x,y], read the 9x9 grid around it
  # if on the edge, fill surroundings with dark pixels
# dark becomes 0, light becomes 1
# mush together and convert binary to decimal
# index into image enhancement algorithm
# if im_alg[index] is dark, output image pixel [x,y] is dark
# save output image 1
# do it again but output image 1 is the input
# count lit pixels in output image 2

def convert_image(input, alg, surr):
  im_rows = len(input)
  im_cols = copy.deepcopy(im_rows)
  # print('old size', im_rows, im_cols)
  new_cols = im_cols + 2
  expanded = [copy.deepcopy(surr)*new_cols]
  for i in range(im_rows):
    new_row = surr
    for j in range(im_cols):
      new_row += input[i][j]
    new_row += surr
    expanded.append(new_row)
  expanded.append(copy.deepcopy(surr)*new_cols)
  num_rows = len(expanded)
  num_cols = len(expanded[0])
  # print("new size", num_rows, num_cols)
  # print("expanded image", expanded)
  output = []
  for b in range(num_rows):
    out_row = ""
    for c in range(num_cols):
      grid_str = ""
      row = expanded[b]
      # print('point', b, c)
      row = expanded[b]
      if b == 0: # top row
        row_above = surr*num_cols # surroundings
        row_below = expanded[b+1]
      elif b == num_rows-1: # bottom row
        row_above = expanded[b-1]
        row_below = surr*num_cols # surroundings
      else:
        row_above = expanded[b-1]
        row_below = expanded[b+1]
      if c == 0: # left edge
        grid_str += surr + row_above[c] + row_above[c+1]
        grid_str += surr + row[c]       + row[c+1]
        grid_str += surr + row_below[c] + row_below[c+1]
      elif c == num_cols-1: # right edge
        grid_str += row_above[c-1] + row_above[c] + surr
        grid_str += row[c-1]       + row[c]       + surr
        grid_str += row_below[c-1] + row_below[c] + surr
      else: # middle
        grid_str += row_above[c-1] + row_above[c] + row_above[c+1]
        grid_str += row[c-1]       + row[c]       + row[c+1]
        grid_str += row_below[c-1] + row_below[c] + row_below[c+1]
      # print("str", grid_str)
      grid_bin = [copy.deepcopy("x")]*len(grid_str)
      for d in range(len(grid_str)):
        if grid_str[d] == ".":
          grid_bin[d] = "0"
        elif grid_str[d] == "#":
          grid_bin[d] = "1"
        else:
          print('oops')
      grid_bin = "".join(grid_bin)
      # print("bin", grid_bin)
      grid_dec = int(grid_bin,2)
      # print("dec", grid_dec)
      # print(alg[grid_dec])
      out_pix = alg[grid_dec]
      # print("pix", out_pix)
      out_row += out_pix
      # print(out_row)
    output.append(out_row)
    # print("output", output)
  return output

def count_pix(image, to_count):
  counter = 0
  out_of = 0
  for e in range(len(image)):
    for g in range(len(image[e])):
      out_of += 1
      if image[e][g] == to_count:
        counter += 1
  return [counter, out_of]

def print_image(image):
  for i in image:
    print(i)

# # print("puzzle input")
# # print_image(input_image)
# output_image1 = convert_image(input_image, im_alg, ".")
# # print('version 1')
# # print_image(output_image1)
# output_image2 = convert_image(output_image1, im_alg, "#")
# # print('version 2')
# # print_image(output_image2)
# light_count = count_pix(output_image2, "#")
# print(light_count)

old_image = input_image
for i in range(50):
  if i % 2 == 0:
    surround = "."
  elif i % 2 == 1:
    surround = "#"
  else:
    print('oops 2')
  new = convert_image(old_image, im_alg, surround)
  old_image = new
new_count = count_pix(old_image, "#")
print(new_count)