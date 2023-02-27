with open('7.txt') as f:
    s = f.read()
    counter = 0
    counter_max = 0
    for i in range(len(s) - 1):
        if s[i] != '0':
            counter += 1
        else:
            if s[i + 1] != '0':
                counter += 1
            else:
                if s[i + 2] != '0':
                    counter += 1
                else:
                    counter_max = max(counter, counter_max)
                    counter = 0

print(counter_max)
