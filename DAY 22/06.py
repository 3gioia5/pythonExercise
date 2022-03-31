# 백준9506

while True:
    n = int(input())

    if n == -1:
        break

    divisor = list()
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    ans = str(n) + " = " + str(divisor[0])
    if sum(divisor) == n:
        for j in range(1, len(divisor)):
            ans += " + " + str(divisor[j])
        print(ans)
    else:
        print(n, "is NOT perfect.")
