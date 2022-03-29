# 백준1934
# 유클리드 호제법 이용
import math

t = int(input())
cmn = 0

for i in range(t):
    a, b = map(int, input().split())

    gcd = 0

    if b == 0:
        print(a)
    else:
        gcd = math.gcd(b, a % b)

    cmn = (a * b) // gcd
    print(cmn)
