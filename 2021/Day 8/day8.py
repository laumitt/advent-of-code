with open('day8input.txt') as f:
    lines = f.readlines()

input = []
for a in range(len(lines)):
    input.append(lines[a])

outputs = []
for b in range(len(input)):
    parts = input[b].strip().split(" | ")
    outputs.append(parts[1])

count_ones = 0
count_four = 0
count_seve = 0
count_eigh = 0
for c in range(len(outputs)):
    display = outputs[c].split(" ")
    for d in range(len(display)):
        if len(display[d]) == 2:
            count_ones = count_ones + 1
        elif len(display[d]) == 3:
            count_seve = count_seve + 1
        elif len(display[d]) == 4:
            count_four = count_four + 1
        elif len(display[d]) == 7:
            count_eigh = count_eigh + 1

print("ones ", count_ones)
print("four ", count_four)
print("seven ", count_seve)
print("eight ", count_eigh)

total = count_ones + count_four + count_seve + count_eigh
print(total)
