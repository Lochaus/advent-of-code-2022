f = open("./Day 2/input.txt", "r")

lines = f.readlines()

score = 0
for lines in lines:
    if lines[2] == "X":
        score += 0
        if lines[0] == "A":
            score += 3
        elif lines[0] == "B":
            score += 1
        elif lines[0] == "C":
            score += 2
    elif lines[2] == "Y":
        score += 3
        if lines[0] == "A":
            score += 1
        elif lines[0] == "B":
            score += 2
        elif lines[0] == "C":
            score += 3
    elif lines[2] == "Z":
        score += 6
        if lines[0] == "A":
            score += 2
        elif lines[0] == "B":
            score += 3
        elif lines[0] == "C":
            score += 1

print(score)