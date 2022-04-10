# 백준9093
# 876ms?

for _ in range(int(input())):
    line = list(map(str, input().split()))
    new_line = ""

    for i in range(len(line)):
        i = line[i][::-1]
        new_line += i + " "

    print(new_line)
