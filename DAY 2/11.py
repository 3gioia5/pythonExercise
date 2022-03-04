# 숫자 맞히기

import random

ANSWER = random.randint(1, 20)
TRY_LIMIT = 4

count = 0
number = 0


while number != ANSWER and count < TRY_LIMIT:
    number = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(TRY_LIMIT - count)))
    count += 1

    if number > ANSWER:
        print("Down")
    elif number < ANSWER:
        print("Up")

if number == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(count))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
