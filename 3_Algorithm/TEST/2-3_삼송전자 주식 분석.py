'''
태호는 주식 분석이 취미입니다.

요즘 제일 핫한 종목은 삼송전자인데요. 삼송전자의 주식을 딱 한 번 사고 팔았다면 최대 얼마의 수익이 가능했을지 궁금합니다. 그것을 계산해 주는 O(n)O(n) 함수 max_profit을 작성하세요.

max_profit은 파라미터로 일별 주식 가격이 들어 있는 리스트 stock_prices를 받고 최대 수익을 리턴합니다. 주식은 딱 한 번만 사고 한 번만 팝니다. 그리고 사는 당일에 팔 수는 없습니다.

하나의 예시로, 지난 6일간 삼송전자의 주식 가격이 이렇다고 가정합시다.
'''

def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 현재까지의 최소 주식 가격
    min_so_far = min(stock_list[0], stock_list[1])

    # 주식 가격을 하나씩 확인한다
    for i in range(2, len(stock_list)):
        # 현재 파는 것이 좋은지 확인한다
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

        # 현재 주식 가격이 최솟값인지 확인한다
        min_so_far = min(min_so_far, stock_list[i])

    return max_profit_so_far

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))