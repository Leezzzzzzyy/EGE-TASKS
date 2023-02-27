with open('3.txt') as f:
    string = f.read()
    counter_max = -10
    counter = 1
    for i in range(len(string) - 1):
        if string[i] <= string[i + 1]:
            counter += 1
        else:
            if string[i] == "Z":
                counter_max = max(counter, counter_max)
                counter = 1
            else:
                counter = 1

print(counter_max)
