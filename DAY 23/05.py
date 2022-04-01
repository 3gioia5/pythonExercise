# 백준5355

t = int(input())

for _ in range(t):
    line = list(map(str, input().split()))
    ans = 0

    for i in range(len(line)):

        if i == 0:
            ans += float(line[i])

        elif line[i] == "@":
            ans *= 3
        elif line[i] == "%":
            ans += 5
        elif line[i] == "#":
            ans -= 7

    print("%0.2f" % ans)
