f = open("./Day 1/input.txt", "r")

lines = f.readlines()

elves = 1

for i in range(len(lines)):
    if lines[i] == "\n":
        elves += 1

calories = [0]*elves

index = 0
for value in lines:
    value = value.replace("\n", "")
    if value == "":
        index += 1
    else:
        calories[index] += int(value)

print(max(calories))