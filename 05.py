# 합이 400이고, 피타고라스 정리를 만족하는 세 자연수 쌍

for a in range(400):
    for b in range(400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)