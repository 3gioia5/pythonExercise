# 백준2711

t = int(input())

for i in range(t):
    n, word = map(str, input().split())
    result = ""

    for j in range(len(word)):
        if j == int(n) - 1:
            continue

        result += word[j]

    print(result)
