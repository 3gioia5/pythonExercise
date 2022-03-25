# 숫자 야구

from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)

    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    guess = []
    while len(guess) < 3:
        number = int(input("{}번째 숫자를 입력하세요: ".format(len(guess) + 1)))
        if number < 0 or number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif number in guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            guess.append(number)

    return guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution and guesses[i] != solution[i]:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    strike, ball = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(strike, ball))
    tries += 1

    if strike == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))

