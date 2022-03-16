# 백준1789

s = int(input())
i = 1

while i * (i + 1) / 2 <= s:
    i += 1

print(i - 1)
