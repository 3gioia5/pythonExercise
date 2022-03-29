# 백준15969

n = int(input())
scores = list(map(int, input().split()))

print(max(scores) - min(scores))
