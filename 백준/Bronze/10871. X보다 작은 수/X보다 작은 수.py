N, X = map(int, input().split())
A = list(map(int, input().split()))
Res = []

for i in range(N):
    if X - A[i] > 0:
        Res.append(A[i])
    else:
        i = i + 1

print(' '.join(str(x) for x in Res))
