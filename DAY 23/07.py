#백준1225
# 시간 초과

a, b = map(str, input().split())
ans = 0

for i in range(len(a)):
    for j in range(len(b)):
        ans += int(a[i]) * int(b[j])

print(ans)
