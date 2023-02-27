with open('5.txt') as f:
    string = f.read()
    counter = 0
    counter_max = -1
    for i in range(len(string) - 1):
        if int(string[i]) % 2 != 0 and int(string[i + 1]) % 2 != 0 and int(string[i]) <= int(string[i + 1]):
            counter += 1
        else:
            counter_max = max(counter, counter_max)
            counter = 0

print(counter_max)
