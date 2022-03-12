# 백준2675

t = int(input())

for i in range(t):
    R, S = input().split()
    R = int(R)

    for j in range(len(S)):
        print(S[j] * R, end='')
    print()
