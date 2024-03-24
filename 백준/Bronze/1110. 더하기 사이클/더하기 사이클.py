N = int(input())
M = N
c = 1

while True:
    if N < 10:
        N1 = N * 10
        N1 = sum(map(int, str(N)))
        N = str(N % 10)+str(N1 % 10)
        N = int(N)
        if N == M:
            break
        else:
            c = c + 1
    else:
        N1 = sum(map(int, str(N)))
        N = str(N % 10)+str(N1 % 10)
        N = int(N)
        if N == M:
            break
        else:
            c = c + 1
print(c)
