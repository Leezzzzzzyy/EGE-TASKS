with open('6.txt') as f:
    s = f.read()
    counter = 0
    counter_max = 0
    for i in range(len(s) - 1):
        if s[i] in "QRS":
            counter += 1
        else:
            counter += 1
            if s[i + 1] == "P":
                counter_max = max(counter, counter_max)
                counter = 0

print(counter_max)
