from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    num_list = []
    while len(num_list) < n:
        num = randint(1, 45)
        # 중복된 경우수 제거
        if num not in num_list:
            num_list.append(num)

    return num_list

def draw_winning_numbers():
    win_list = generate_numbers(7)
    return sorted(win_list[:6]) + win_list[6:]


def count_matching_numbers(list_1, list_2):
    count = 0
    '''
    list_1.sort()
    list_2.sort()
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                count += 1
    '''
    for num in list_1:
        if num in list_2:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = count_matching_numbers(numbers, winning_numbers[0:6])
    bonus = False
    for i in range(len(numbers)):
        if winning_numbers[6] == numbers[i]:
            bonus = True

    if count == 6:
        return 1000000000  # 1등
    elif count == 5:
        if bonus == True:  # 2등
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

print(generate_numbers(6))
