with open('data/chicken.txt', 'r') as f:
    total = 0
    count = 0
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])
        total += revenue
        count += 1

    print(total / count)
