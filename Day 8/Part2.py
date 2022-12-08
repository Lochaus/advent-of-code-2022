import string

f = open("./Day 8/input.txt", "r")

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

max_height = len(lines)
max_width = len(lines[0])
max = 1

def distance_up(x, y, lines):
    total = 1
    first_value = True
    for i in range(y-1, -1, -1):
        if lines[i][x] < lines[y][x]:
            if not first_value:
                total += 1
            else:
                first_value = False
        else:
            if first_value:
                return total
            total += 1
            return total
    return total

def distance_down(x, y, lines, max_height):
    total = 1
    first_value = True
    for i in range(y+1, max_height):
        if lines[i][x] < lines[y][x]:
            if not first_value:
                total += 1
            else:
                first_value = False
        else:
            if first_value:
                return total
            total += 1
            return total
    return total

def distance_left(x, y, lines):
    total = 1
    first_value = True
    for i in range(x-1, -1, -1):
        if lines[y][i] < lines[y][x]:
            if not first_value:
                total += 1
            else:
                first_value = False
        else:
            if first_value:
                return total
            total += 1
            return total
    return total

def distance_right(x, y, lines, max_width):
    total = 1
    first_value = True
    for i in range(x+1, max_width):
        if lines[y][i] < lines[y][x]:
            if not first_value:
                total += 1
            else:
                first_value = False
        else:
            if first_value:
                return total
            total += 1
            return total
    return total

for y in range(1, max_height-1):
    for x in range(1,max_height-1):
        scenic_score = distance_down(x, y, lines, max_height) * distance_left(x, y, lines) * distance_right(x, y, lines, max_width) * distance_up(x, y, lines)
        if scenic_score > max:
            max = scenic_score
            print(x, y)

print(max)