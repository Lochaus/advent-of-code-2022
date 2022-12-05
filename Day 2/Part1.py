f = open("./Day 2/input.txt", "r")

lines = f.readlines()

score = 0
for lines in lines:
    if lines[2] == "X":
        score += 1
        if lines[0] == "A":
            score += 3
        elif lines[0] == "B":
            score += 0
        elif lines[0] == "C":
            score += 6
    elif lines[2] == "Y":
        score += 2
        if lines[0] == "A":
            score += 6
        elif lines[0] == "B":
            score += 3
        elif lines[0] == "C":
            score += 0
    elif lines[2] == "Z":
        score += 3
        if lines[0] == "A":
            score += 0
        elif lines[0] == "B":
            score += 6
        elif lines[0] == "C":
            score += 3


print(score)