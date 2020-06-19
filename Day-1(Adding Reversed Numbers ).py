t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    rev = 0
    rev1 = 0
    final_rev = 0
    while n > 0:
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    # Reverse m
    while m > 0:
        b = m % 10
        rev1 = rev1 * 10 + b
        m = m // 10
    x = (rev + rev1)
    # Reverse x
    while x > 0:
        c = x % 10
        final_rev = final_rev * 10 + c
        x = x // 10
    print(final_rev)