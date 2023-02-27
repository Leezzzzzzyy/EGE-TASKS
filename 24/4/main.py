with open('4.txt') as f:
    string = f.read()
    counter_max = -10
    counter = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            counter += 1
        else:
            counter_max = max(counter, counter_max)
            counter = 0

print(counter_max)
