f = open("./Day 6/input.txt", "r")

input_data = f.readline()

for i in range(3, len(input_data)):
    if len(set([input_data[i], input_data[i-1], input_data[i-2], input_data[i-3]])) == 4:
        print(i+1)
        break