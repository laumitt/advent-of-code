test = 0
if test == 1:
    with open('day10input_test.txt') as f:
        lines = f.readlines()
else:
    with open('day10input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

matches = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
 }

syn_err_score = 0
expected = ""
for b in range(len(input)):
    for c in range(len(input[b])):
        row = input[b]
        if row[c] in "([{<":
            expected += matches[row[c]]
        elif row[c] in ")]}>":
            if row[c] != expected[-1]:
                syn_err_score += points[row[c]]
                print(row[c])
                print(points[row[c]])
                break
            else:
                expected = expected[:-1]

print(syn_err_score)
