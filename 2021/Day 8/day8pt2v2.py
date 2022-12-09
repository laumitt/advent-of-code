test = 0

if test == 1:
    with open('day8input_test.txt') as f:
        lines = f.readlines()
else:
    with open('day8input.txt') as f:
        lines = f.readlines()

input = []
for a in range(len(lines)):
    input.append(lines[a])

def get_key(dict, val):
    for key, value in dict.items():
         if val == value:
             return key

wire_digit_dict = { # number of wires to digit
    2 : "1",
    3 : "7",
    4 : "4",
    5 : "2, 3, or 5",
    6 : "0, 6, or 9",
    7 : "8"
}
easy_digits = ["1", "4", "7", "8"]
total = 0
wires = []
segments = []
outputs = []
for b in range(len(input)):
    parts = input[b].strip().split(" | ")
    wires.append(parts[0])
    segments.append(parts[1])

for c in range(len(segments)):
    curr_out = ""
    entry_wires = wires[c].split(" ")
    entry_wires.sort(key=len)
    entry_out = segments[c].split(" ")
    all_wires = entry_wires + entry_out
    entry_out_dec = ""
    entry_dict = {
        0 : "x",
        1 : "x",
        2 : "x",
        3 : "x",
        4 : "x",
        5 : "x",
        6 : "x",
        7 : "x",
        8 : "x",
        9 : "x"
    }
    entry_wire_poss = {}
    wires_dec = 0
    entry_dec = False
    print("wire connections for this entry ", entry_wires)
    print("output for this entry ", entry_out)
    while entry_dec == False:
        for d in range(len(all_wires)):
            in_one = 0
            in_four = 0
            in_seven = 0
            sorted_wires = sorted(all_wires[d])
            curr_wires = "".join(sorted_wires)
            num_wires = len(curr_wires)
            curr_digit = wire_digit_dict[num_wires]
            if curr_digit == "2, 3, or 5":
                for e in range(len(curr_wires)):
                    if curr_wires[e] in entry_dict[1]:
                        in_one += 1
                    if curr_wires[e] in entry_dict[4]:
                        in_four += 1
                    if curr_wires[e] in entry_dict[7]:
                        in_seven += 1
                if in_one == 2:
                    curr_digit = "3"
                elif in_four == 3:
                    curr_digit = "5"
                elif in_seven == 2:
                    curr_digit = "2"
                    print("overlaps", in_one, in_four, in_seven)
            elif curr_digit == "0, 6, or 9":
                for e in range(len(curr_wires)):
                    if curr_wires[e] in entry_dict[4]:
                        in_four += 1
                    if curr_wires[e] in entry_dict[7]:
                        in_seven += 1
                if in_four == 4:
                    curr_digit = "9"
                elif in_seven == 3:
                    curr_digit = "0"
                elif in_four == 3:
                    curr_digit = "6"
            if len(curr_digit) == 1:
                print("current wires ", curr_wires)
                print("found current digit ", curr_digit)
                if entry_dict[int(curr_digit)] == "x":
                    entry_dict[int(curr_digit)] = curr_wires
                entry_wire_poss[int(curr_digit)] = curr_wires
                # print("entry dict is now", entry_dict)
                # print("entry wire possibilities now ", entry_wire_poss)
                wires_dec += 1
        for e in range(len(entry_out)):
            sorted_wires_out = sorted(entry_out[e])
            out_wires = "".join(sorted_wires_out)
            print("output wires", out_wires)
            out_digit = get_key(entry_wire_poss, out_wires)
            print("found output digit", out_digit)
            entry_out_dec += str(out_digit)
        if wires_dec >= 14 or len(entry_out_dec) == 4:
            entry_dec = True
    outputs.append(entry_out_dec)
    total += int(entry_out_dec)
    print("entry output decoded to", entry_out_dec)
print("decoded outputs ", outputs)
print(total)
