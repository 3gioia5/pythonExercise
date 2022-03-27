# 백준1929
# 미완성

m, n = map(int, input().split())

for i in range(m, n + 1):
    print(i)
    print('-----')
    for j in range(2, i):
        print(j)
        print('-----')
        if i % j == 0:
            break
        else:
            print(i)
            print('--*--')
