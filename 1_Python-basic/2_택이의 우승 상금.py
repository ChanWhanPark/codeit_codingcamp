money = 50000000
year = 1988

while (year < 2016):
    money = money * 1.12
    year += 1

apart = 1100000000
if money > apart:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(money - apart)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(apart - money)))