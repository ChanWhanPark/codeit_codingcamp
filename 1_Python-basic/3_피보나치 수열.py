prev = 1
curr = 1
index = 0

print(prev)
print(curr)

while (index <= 23):
    prev = prev + curr
    print(prev)
    curr = curr + prev
    print(curr)
    index += 1