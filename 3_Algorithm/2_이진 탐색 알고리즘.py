'''
‘이진 탐색(Binary Search)’ 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.
이진 탐색 알고리즘은 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 합니다. 정렬된 리스트가 아니면 이 알고리즘은 적용이 불가능합니다.

왜 이 알고리즘의 이름이 ‘이진 탐색’일까요? 1회 비교를 거칠 때마다 탐색 범위가 (대략) 절반으로 줄어들기 때문입니다.
'''

### 사용하기 위해서는 리스트가 정렬되어 있어야 함
def binary_search(element, some_list):
    # 코드를 작성하세요.
    n = 0
    length = len(some_list)
    while length != 0:
        find_index = (n + length) // 2
        if element == some_list[find_index]:
            return find_index
        elif element > some_list[find_index]:
            n = find_index
        else:
            length = find_index
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))