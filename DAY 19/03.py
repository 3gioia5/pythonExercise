# 백준11365

while True:
    line = input()

    if line == 'END':
        break

    new_line = list()
    for left in range(len(line)):
        right = len(line) - left - 1
        new_line.append(line[right])

    print(''.join(new_line))
