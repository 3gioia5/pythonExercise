# 백준1085

x, y, w, h = map(int, input().split())

distance = list()

distance.append(w - x)
distance.append(h - y)
distance.append(x)
distance.append(y)

print(min(distance))
