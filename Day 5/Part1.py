import string

f = open("./Day 5/input.txt", "r")

lines = f.readlines()
empty_line = 0

letter_list = [k for k in string.ascii_uppercase]

for line in lines:
    if line == "\n":
        break
    else:
        empty_line += 1

number_of_stacks = int((lines[empty_line-1].replace("\n", "").replace(" ", "")[-1]))
stacks = [[] for i in range(number_of_stacks)]

position_of_stacks = []

for i in range(1,number_of_stacks+1):
    position_of_stacks.append(lines[empty_line-1].index(str(i)))

for i in range(empty_line-2, -1, -1):
    j = 0
    for value in position_of_stacks:
        if lines[i][value] in letter_list:
            nested_list = stacks[j]
            nested_list.append(lines[i][value])
        j += 1

instructions = []

for i in range(empty_line+1, len(lines)):
    instruction = lines[i].replace("move", "").replace("from", "").replace("to", "").replace("\n", "")[1:]
    instruction = instruction.split("  ")
    instructions.append(instruction)

for instruction in instructions:
    temp_list = []
    for i in range(int(instruction[0])):
        nested_list = stacks[int(instruction[1])-1]
        temp_list.append(nested_list.pop())
    nested_list = stacks[int(instruction[2])-1]
    for value in temp_list:
        nested_list.append(value)

answer = ""
for i in range(len(stacks)):
    answer += stacks[i][-1]

print(answer)