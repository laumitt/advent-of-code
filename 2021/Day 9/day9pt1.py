test = 1
if test == 1:
    with open('day9input_test.txt') as f:
        lines = f.readlines()
else:
    with open('day9input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

# print(input)
num_rows = len(input)
num_cols = len(input[0])
low_points = []
print(num_rows)
print(num_cols)

def check_above(x,y):
    if x == 0:
        return "top row"
    if 0 < x <= num_rows:
        print("location", x, y, "holds", input[x][y])
        print("above this is", x-1, y, "with", input[x-1][y])
        if input[x][y] < input[x-1][y]:
            return "lower"
        else:
            return "higher"
def check_left(x,y):
    if x == 0:
        return "left edge"
    if 0 < x <= num_cols:
        print("location", x, y, "holds", input[x][y])
        print("left of this is", x, y-1, "with", input[x][y-1])
        if input[x][y] < input[x][y-1]:
            return "lower"
        else:
            return "higher"
def check_right(x,y):
    if x == num_cols:
        return "right edge"
    if 0 <= x < num_cols:
        print("location", x, y, "holds", input[x][y])
        print("right of this is", x, y+1, "with", input[x][y+1])
        if input[x][y] < input[x+1][y]:
            return "lower"
        else:
            return "higher"
def check_below(x,y):
    if y == num_rows:
        return "bottom row"
    if 0 <= y < num_rows:
        print("location", x, y, "holds", input[x][y])
        print("below this is", x+1, y, "with", input[x+1][y])
        if input[x][y] < input[x][y+1]:
            return "lower"
        else:
            return "higher"

for b in range(num_cols):
    for c in range(num_rows):
        print(b, c)
        if check_above(b,c) == "lower":
            if check_below(b,c) == "lower":
                if check_left(b,c) == "lower":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # middle of the grid
                    elif check_right(b,c) == "right edge":
                            low_points.append(input[b][c]) # right edge
                elif check_left(b,c) == "left edge":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # left edge
            elif check_below(b,c) == "bottom row":
                if check_left(b,c) == "lower":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # bottom row
                    elif check_right(b,c) == "right edge":
                            low_points.append(input[b][c]) # bottom right corner
                elif check_left(b,c) == "left edge":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # bottom left corner
            elif check_above(b,c) == "top row":
                if check_left(b,c) == "lower":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # top row
                    elif check_right(b,c) == "right edge":
                            low_points.append(input[b][c]) # top right corner
                elif check_left(b,c) == "left edge":
                    if check_right(b,c) == "lower":
                        low_points.append(input[b][c]) # top left corner

        # if c == 0: # left edge
        #     if b == 0: # top left corner
        #         if check_below(b,c) == "lower":
        #             if check_right(b,c) == "lower":
        #                 low_points.append(input[b][c])
        #     elif b == num_rows: # bottom left corner
        #         if check_above(b,c) == "lower":
        #             if check_right(b,c) == "lower":
        #                 low_points.append(input[b][c])
        #     else: # just left edge
        #         if check_above(b,c) == "lower":
        #             if check_below(b,c) == "lower":
        #                 if check_right(b,c) == "lower":
        #                     low_points.append(input[b][c])
        # elif c == num_cols: # right edge
        #     if b == 0: # top right corner
        #         if check_below(b,c) == "lower":
        #             if check_left(b,c) == "lower":
        #                 low_points.append(input[b][c])
        #     elif b == num_rows: # bottom right corner
        #         if check_above(b,c) == "lower":
        #             if check_left(b,c) == "lower":
        #                 low_points.append(input[b][c])
        #     else: # just right edge
        #         if check_above(b,c) == "lower":
        #             if check_below(b,c) == "lower":
        #                 if check_left(b,c) == "lower":
        #                     low_points.append(input[b][c])
        # else:
        #     if b == 0: # middle top edge
        #         if check_below(b,c) == "lower":
        #             if check_left(b,c) == "lower":
        #                 if check_right(b,c) == "lower":
        #                     low_points.append(input[b][c])
        #     elif b == num_rows: # middle bottom edge
        #         if check_above(b,c) == "lower":
        #             if check_left(b,c) == "lower":
        #                 if check_right(b,c) == "lower":
        #                     low_points.append(input[b][c])
        #     else:
        #         if check_above(b,c) == "lower":
        #             if check_below(b,c) == "lower":
        #                 if check_left(b,c) == "lower":
        #                     if check_right(b,c) == "lower":
        #                         low_points.append(input[b][c])
print(low_points)
risk_score = 0
for i in low_points:
    risk_score += int(i) + 1
print(risk_score)
