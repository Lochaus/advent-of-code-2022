import string

f = open("./Day 8/input.txt", "r")

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

max_height = len(lines)
max_width = len(lines[0])
answer = (max_width*2)+(max_height*2)-4

for y in range(1, max_height-1):
    for x in range(1,max_height-1):
        highest1 = True
        highest2 = True
        highest3 = True
        highest4 = True
        for i in range(x-1, -1, -1):
            if lines[y][i] >= lines[y][x] and highest1:
                highest1 = False
        for i in range(x+1, max_width):
            if lines[y][i] >= lines[y][x] and highest2:
                highest2 = False
        for i in range(y-1, -1, -1):
            if lines[i][x] >= lines[y][x] and highest3:
                highest3 = False
        for i in range(y+1, max_height):
            if lines[i][x] >= lines[y][x] and highest4:
                highest4 = False
        if highest1 or highest2 or highest3 or highest4:
            answer += 1

print(answer)