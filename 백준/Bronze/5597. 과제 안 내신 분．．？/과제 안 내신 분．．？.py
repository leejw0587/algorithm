students = list(range(1, 31))

for i in range(28):
    num = int(input())

    if num in students:
        students.remove(num)
    
students.sort()

for i in students:
    print(i)