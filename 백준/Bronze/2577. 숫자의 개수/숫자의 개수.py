A = int(input())
B = int(input())
C = int(input())

mul = A * B * C

numbers = list(map(int, str(mul)))
numbers.sort()

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0


for i in numbers:
    if i == 0:
        n0 = n0 + 1
    if i == 1:
        n1 = n1 + 1
    if i == 2:
        n2 = n2 + 1
    if i == 3:
        n3 = n3 + 1
    if i == 4:
        n4 = n4 + 1
    if i == 5:
        n5 = n5 + 1
    if i == 6:
        n6 = n6 + 1
    if i == 7:
        n7 = n7 + 1
    if i == 8:
        n8 = n8 + 1
    if i == 9:
        n9 = n9 + 1

print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
