f = open("./Day 4/input.txt", "r")

lines = f.readlines()
input_values = []

for line in lines:
    line = line.replace("\n", "")
    line = line.split(",")
    for line2 in line:
        line2 = line2.split("-")
        input_values.append(line2)

print(input_values)

counter = 0

for i in range(len(lines)):
    if (int(input_values[(i*2)][0]) >= int(input_values[(i*2)+1][0]) and int(input_values[(i*2)][1]) <= int(input_values[(i*2)+1][1])
     or (int(input_values[(i*2)+1][0]) >= int(input_values[(i*2)][0]) and int(input_values[(i*2)+1][1]) <= int(input_values[(i*2)][1]))):
        counter += 1

print(counter)