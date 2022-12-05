import copy
import string

f = open("./Day 3/input.txt", "r")

lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

letter_dict = {k:0 for k in string.ascii_letters}

total = 0

for line in lines:
    empty_letter_dict1 = copy.copy(letter_dict)
    empty_letter_dict2 = copy.copy(letter_dict)
    index_max = len(line)
    index = 0
    for letter in line:
        if index < (index_max/2):
            empty_letter_dict1[letter] += 1
            index += 1
        else:
            empty_letter_dict2[letter] += 1
    index_list = list(empty_letter_dict1)
    for i in range(len(empty_letter_dict1)):
        if empty_letter_dict1[index_list[i]] >= 1 and empty_letter_dict2[index_list[i]] >= 1:
            total += (i+1)
            break

print(total)