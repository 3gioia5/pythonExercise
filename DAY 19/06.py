# 백준9093
# 미완성

t = int(input())

for i in range(t):
    line = list(map(str, input().split()))

    new_line = list()

    for word in line:
        for left in range(len(word)):
            right = len(word) - left - 1
            new_line.append(word[right])

    print(''.join(new_line))
