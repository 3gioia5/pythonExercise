# 백준2845

l, p = map(int, input().split())
expect = list(map(int, input().split()))

exact = l * p
for i in expect:
    print(i - exact, end=' ')
