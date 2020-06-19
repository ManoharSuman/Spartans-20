import math
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for i in range(n, m):
        x=math.floor(math.sqrt(i))
        for j in range(2, 1+x):
            if i % j == 0:
                break
        else:
            print(i)