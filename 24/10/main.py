with open('10.txt') as f:
    string = f.read()
    counter = 0
    counter_max = -1
    for i in range(0, len(string) - 3, 3):
        if 'XYZ' == string[i: i + 3]:
            counter += 3
        else:
            counter_max = max(counter, counter_max)
            counter = 0

print(counter_max)
