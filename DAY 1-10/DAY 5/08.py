# 백준4344

C = int(input())

for i in range(C):
    line = list(map(int, input().split()))

    # 평균 구하기
    avg = sum(line[1:]) / line[0]

    # 평균 넘는 학생 수 구하기
    superior = 0
    for s in line[1:]:
        if int(s) > avg:
            superior += 1

    # 평균 넘는 학생의 비율 구하기
    rate = superior / line[0] * 100

    # 퍼센테이지로 환산
    print(f'{rate:.3f}%')
