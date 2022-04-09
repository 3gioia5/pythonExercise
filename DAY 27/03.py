# 백준3062

for _ in range(int(input())):
    s = input()
    n = str(int(s) + int(s[::-1]))

    if n == n[::-1]:
        print("YES")
    else:
        print("NO")
