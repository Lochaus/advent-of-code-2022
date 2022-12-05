import copy
import string

f = open("./Day 3/input.txt", "r")

lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

letter_dict = {k:0 for k in string.ascii_letters}

total = 0

for i in range(int(len(lines)/3)):
    empty_letter_dict1 = copy.copy(letter_dict)
    empty_letter_dict2 = copy.copy(letter_dict)
    empty_letter_dict3 = copy.copy(letter_dict)
    for letter in lines[(i*3)]:
        empty_letter_dict1[letter] += 1
    for letter in lines[(i*3)+1]:
        empty_letter_dict2[letter] += 1
    for letter in lines[(i*3)+2]:
        empty_letter_dict3[letter] += 1
    index_list = list(empty_letter_dict1)
    for i in range(len(empty_letter_dict1)):
        if empty_letter_dict1[index_list[i]] >= 1 and empty_letter_dict2[index_list[i]] >= 1 and empty_letter_dict3[index_list[i]] >= 1:
            total += (i+1)
            break

print(total)