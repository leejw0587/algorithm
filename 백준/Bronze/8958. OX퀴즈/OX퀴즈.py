T = int(input())

for i in range(T):
    point = 0
    cons = 0
    test = input()
    for j in range(len(test)):
        if test[j] == 'O':
            cons += 1
            point += 1 * cons
        else:
            cons = 0
    print(point)
