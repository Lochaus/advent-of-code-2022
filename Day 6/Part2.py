from tracemalloc import start


f = open("./Day 6/input.txt", "r")

input_data = f.readline()

for i in range(13, len(input_data)):
    start_marker = []
    for j in range(14):
        start_marker.append(input_data[i-j])
    if len(set(start_marker)) == 14:
        print(i+1)
        break