# 백준13410

n, k = map(int, input().split())
ans = list()

for i in range(1, k + 1):
    new_number = str(n * i)[::-1]
    ans.append(int(new_number))

print(max(ans))
