# 백준2839

n = int(input())
ans = 0

while n >= 0:
    if n % 5 == 0:
        ans += n // 5
        print(ans)
        break

    n -= 3
    ans += 1

else:
    print(-1)
