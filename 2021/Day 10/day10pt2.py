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
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

matches = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
 }

corrupt_rows = []
incomplete_rows = []
row_scores = []
for b in range(len(input)):
    expected = ""
    for c in range(len(input[b])):
        row = input[b]
        if row[c] in "([{<":
            expected += matches[row[c]]
        elif row[c] in ")]}>":
            if row[c] != expected[-1]:
                # syn_err_score += points[row[c]]
                # corrupt_rows.append(row)
                break
            else:
                expected = expected[:-1]
        if c == len(input[b])-1:
            expected = expected[::-1]
            print(expected)
            if len(expected) != 0:
                incomplete_rows.append(row)
                row_score = 0
                for d in range(len(expected)):
                    row_score = row_score * 5
                    row_score += points[expected[d]]
                row_scores.append(row_score)

row_scores.sort()
print(row_scores)
auto_score = row_scores[len(row_scores) // 2]

print(len(incomplete_rows))
print(auto_score)
