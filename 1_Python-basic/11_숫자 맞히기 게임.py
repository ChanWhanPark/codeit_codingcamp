'''
1과 20 사이의 숫자를 맞히는 게임을 만들려고 합니다.
random 모듈과 input 함수를 활용하여 프로그램을 만들어 보세요.
'''

import random

num = random.randint(1, 20)
count = 0
chance = 4

for i in range(chance):
    answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(chance-i)))
    if answer > num:
        print("Down")
        if i == chance - 1:
            print("아쉽습니다. 정답은 {}이었습니다.".format(num))
    elif answer < num:
        print("Up")
        if i == chance - 1:
            print("아쉽습니다. 정답은 {}이었습니다.".format(num))
    else:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i+1))
        break
