# 피보나치 수열의 첫 50개 항을 차례대로 출력하기

i = 1
current = 1
previous = 0

while i <= 50:
    print(current)
    temp = previous
    previous = current
    current = temp + current
    i += 1