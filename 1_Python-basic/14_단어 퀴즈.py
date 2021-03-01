with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        eng, kor = data[0], data[1]
        guess = input("{}: ".format(kor))
        if eng == guess:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng))