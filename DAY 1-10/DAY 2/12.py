# 로또 시뮬레이션

import random

# 랜덤 번호 생성기
def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        number = random.randint(1, 45)
        if number not in numbers:
            numbers.append(number)

    return numbers


# 당첨 번호 + 보너스 번호 추첨, 당첨 번호는 정렬
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    non_bonus = winning_numbers[0:5]
    non_bonus = sorted(non_bonus)
    winning_numbers = non_bonus + winning_numbers[6:]

    return winning_numbers


# 겹치는 번호 개수 리턴
def count_matching_numbers(list_1, list_2):
    count = 0

    for i in list_1:
        for j in list_2:
            if i == j:
                count += 1

    return count


# 당첨금 확인
def check(numbers, winning):
    count = count_matching_numbers(numbers, winning[:6])
    bonus_count = count_matching_numbers(numbers, winning[6:])

    if count == 6:
        print(1000000000)
    elif count == 5 and bonus_count == 1:
        print(50000000)
    elif count == 5:
        print(1000000)
    elif count == 4:
        print(50000)
    elif count == 3:
        print(5000)
    else:
        exit()
