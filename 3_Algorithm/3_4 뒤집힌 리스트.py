'''
파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해 주는 재귀 함수 flip을 쓰세요.
'''

def flip(some_list):
    # Basic
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    # Recursive
    return some_list[-1:] + flip(some_list[:-1])
    # some_list의 끝원소와 남은 원소를 뒤집은 것을 더함


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flip_list = flip(list)
print(flip_list)