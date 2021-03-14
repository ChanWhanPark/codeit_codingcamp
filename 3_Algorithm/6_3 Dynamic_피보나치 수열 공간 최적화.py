def fib_optimized(n):
    # 코드를 작성하세요.
    current = previous = 1

    for i in range(3, n+1):
        current = current + previous
        previous = current - previous

    return current


# 테스트
print(fib_optimized(1))
print(fib_optimized(10))
print(fib_optimized(210))
