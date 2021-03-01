'''
화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.
섭씨와 화씨의 관계식은 다음과 같습니다:

{\degree}C = \frac{({\degree}F - 32) * 5}{9}

화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수를 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.

'''


# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    index = 0
    while (index < len(fahrenheit)):
        fahrenheit[index] = (fahrenheit[index] - 32) * 5 / 9
        fahrenheit[index] = round(fahrenheit[index], 1) # 소수점을 1자리로 제한
        index += 1

    return fahrenheit


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

fahrenheit_to_celsius(temperature_list)
# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

