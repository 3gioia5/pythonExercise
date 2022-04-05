# 백준2490

for _ in range(3):
    line = list(map(int, input().split()))

    if sum(line) == 1:
        print("C")
    elif sum(line) == 2:
        print("B")
    elif sum(line) == 3:
        print("A")
    elif sum(line) == 4:
        print("E")
    else:
        print("D")
