H, M = map(int, input().split())

M = M - 45

if(M < 0):
    H = H - 1
    M = M + 60

if(M > 60):
    M = 0
    H = H + 1

if(H < 0):
    H = H + 24

print(H, M)