# 백준10807

n = int(input())
ans = 0

numbers = list(map(int, input().split()))
v = int(input())

for i in range(len(numbers)):
    if v == numbers[i]:
        ans += 1

print(ans)
