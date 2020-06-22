t = int(input())
for i in range (t):
    n = int(input())
    x = 0
    if n >= 5:
        while n >= 5:
            n = n//5
            x = x+n
        print(x)
    else:
        print('0')