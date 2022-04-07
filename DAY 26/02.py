# 백준10797

day = int(input())
cars = list(map(int, input().split()))
ban = 0

for i in cars:
    if day == i:
        ban += 1

print(ban)
