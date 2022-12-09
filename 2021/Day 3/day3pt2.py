test = 1

if test == 1:
    with open('day3input_test.txt') as f:
        lines = f.readlines()
else:
    with open('day3input.txt') as f:
        lines = f.readlines()

input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

num_rows = len(input)
num_cols = len(input[0])
ox_crit = ""
co_crit = ""
ox_keep = input[:]
co_keep = input[:]
oxy_gen = ""
co2_rat = ""
# for b in range(num_cols):
#     count_ones = 0
#     count_zero = 0
#     for c in range(num_rows):
#         current_row = input[c]
#         current_bit = current_row[b]
#         if current_bit == '1':
#             count_ones += 1
#         elif current_bit == '0':
#             count_zero += 1
#     if count_ones > count_zero:
#         ox_crit += "1"
#         co_crit += "0"
#     elif count_ones == count_zero:
#         ox_crit += "1"
#         co_crit += "0"
#     elif count_ones < count_zero:
#         ox_crit += "0"
#         co_crit += "1"

# find oxygen generator rating
for d in range(num_cols):
    count_ones = 0
    count_zero = 0
    for c in range(len(ox_keep)):
        current_row = ox_keep[c]
        current_bit = current_row[d]
        if current_bit == '1':
            count_ones += 1
        elif current_bit == '0':
            count_zero += 1
    print("ones", count_ones)
    print('zero', count_zero)
    if count_ones > count_zero:
        print('more 1')
        for e in range(len(ox_keep)):
            if e < len(ox_keep):
                this_row = ox_keep[e]
                if this_row[d] != "1":
                    ox_keep.remove(this_row)
            elif e == len(ox_keep):
                this_row = ox_keep[0]
                if this_row[d] != "1":
                    ox_keep.remove(this_row)
    elif count_ones == count_zero:
        print('equal - keep 1')
        for f in range(len(ox_keep)):
            if f < len(ox_keep):
                this_row = ox_keep[f]
                if this_row[d] != "1":
                        ox_keep.remove(this_row)
            elif f == len(ox_keep):
                this_row = ox_keep[0]
                if this_row[d] != "1":
                        ox_keep.remove(this_row)
    elif count_ones < count_zero:
        print('more 0')
        for g in range(len(ox_keep)):
            if g < len(ox_keep):
                this_row = ox_keep[g]
            elif g == len(ox_keep):
                this_row = ox_keep[0]
            if this_row[d] != "0":
                    ox_keep.remove(this_row)
    else:
        print('oops')
    print(ox_keep)
print(ox_keep)
oxy_gen = int(ox_keep[0],2)
print("oxygen generator rating", oxy_gen)

# find co2 scrubber  rating
for d in range(num_cols):
    count_ones = 0
    count_zero = 0
    for c in range(len(co_keep)):
        current_row = co_keep[c]
        current_bit = current_row[d]
        if current_bit == '1':
            count_ones += 1
        elif current_bit == '0':
            count_zero += 1
    print("ones", count_ones)
    print('zero', count_zero)
    if count_ones > count_zero:
        print('more 1')
        for e in range(len(co_keep)):
            if e < len(co_keep):
                this_row = co_keep[e]
                if this_row[d] == "1":
                    co_keep.remove(this_row)
                    if len(co_keep) == 1:
                        break
            elif e == len(co_keep):
                this_row = co_keep[0]
                if this_row[d] == "1":
                    co_keep.remove(this_row)
                    if len(co_keep) == 1:
                        break
    elif count_ones == count_zero:
        print('equal - keep 0')
        for f in range(len(co_keep)):
            if f < len(co_keep):
                this_row = co_keep[f]
                if this_row[d] == "1":
                    co_keep.remove(this_row)
                    if len(co_keep) == 1:
                        break
            elif f == len(co_keep):
                this_row = co_keep[0]
                if this_row[d] == "1":
                    co_keep.remove(this_row)
                    if len(co_keep) == 1:
                        break
    elif count_ones < count_zero:
        print('more 0')
        for g in range(len(co_keep)):
            # if g < len(co_keep):
            #     this_row = co_keep[g]
            # elif g == len(co_keep):
            #     this_row = co_keep[0]
            if co_keep[g][d] == "0":
                co_keep.remove(co_keep[g])
                if len(co_keep) == 1:
                    break
    else:
        print('oops')
    print('removed', this_row)
    print(co_keep)

# print(co_keep)
# co2_rat = int(co_keep[0],2)
# print("co2 scrubber rating", co2_rat)
#
# life_support = oxy_gen * co2_rat
# print(life_support)
