with open('2.txt') as f:
    string = ''.join([i for i in f])
    counter_max = -10
    counter = 0
    for i in range(0, len(string)):
        if string[i] == 'Z':
            counter_max = max(counter, counter_max)
            counter = 0
        else:
            counter += 1

print(counter_max)
