'''솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다.
그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...
가능한 최대 수익을 리턴시켜 주는 함수 max_profit_memo를 Memoization 방식으로 작성해 보세요.
max_profit_memo는 파라미터 세 개를 받습니다.

price_list: 개수별 가격이 정리되어 있는 리스트
count: 판매할 새꼼달꼼 개수
cache: 개수별 최대 수익이 저장되어 있는 사전
예를 들어 price_list가 [0, 100, 400, 800, 900, 1000]이라면,

새꼼달꼼 0개에 0원
새꼼달꼼 1개에 100원
새꼼달꼼 2개에 400원
새꼼달꼼 3개에 800원
새꼼달꼼 4개에 900원
새꼼달꼼 5개에 1000원
이렇게 가격이 책정된 건데요. 만약 솔희가 새꼼달꼼 5개를 판매한다면 최대로 얼마를 벌 수 있을까요?

한 친구에게 3개 팔고 다른 친구에게 2개를 팔면, 800 + 400800+400을 해서 총 1200원의 수익을 낼 수 있겠죠.'''
def max_profit_memo(price_list, count, cache):
    # Base Case
    if count <= 1:
        cache[count] = price_list[count]
        return price_list[count]

    # Recursive Case
    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # 조합들을 비교하여, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
