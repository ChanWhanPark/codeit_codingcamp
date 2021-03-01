import random

vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        eng, kor = data[0], data[1]
        vocab[eng] = kor

# 문제 내기
while True:
    keys = list(vocab.keys())
    index = random.randint(0, len(keys) - 1)
    eng = keys[index]
    kor = vocab[eng]

    guess = input("{}: ".format(kor))

    if guess == 'q':
        break

    if guess == eng:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.".format(eng))