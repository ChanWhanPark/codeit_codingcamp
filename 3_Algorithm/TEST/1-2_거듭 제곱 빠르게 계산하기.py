'''
거듭 제곱을 계산하는 함수 power를 작성하고 싶습니다.
power는 파라미터로 자연수 x와 자연수 y를 받고, x^y를 리턴합니다.
 이 알고리즘의 시간 복잡도는 O(y)인데요. O(lgy)로 더 빠르게 할 수는 없을까요?
'''

def power(x, y):
    # 코드를 작성하세요.
    product = 1
    if y == 1:
        return x
    else:
        product *= x
        y -= 1
        product *= power(x, y)
    return product


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))