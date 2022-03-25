# 백준2884

H, M = map(int, input().split())

if M < 45:
    H -= 1
    M = M + 60
    if H < 1:
        H = 23

print(H, M - 45)