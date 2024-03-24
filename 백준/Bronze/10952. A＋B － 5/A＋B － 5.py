A = 1
B = 1

while True:
    A, B = map(int, input().split())
    if A + B > 0:
        print(A+B)
    else:
        break