# 백준1934
# 시간 초과

t = int(input())
cmn = 0

for i in range(t):
    a, b = map(int, input().split())

    data1 = []
    data2 = []

    for i in range(1, b + 1):
        data1.append(i * a)
    for i in range(1, a + 1):
        data2.append(i * b)

    for i in data1:
        if i in data2:
            cmn = i
            break
    print(cmn)