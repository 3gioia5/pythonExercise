# 백준2355
# 시간 초과

a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    ans += i

print(ans)
