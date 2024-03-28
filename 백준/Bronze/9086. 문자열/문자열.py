test = int(input())

for i in range(test):
    str = input()
    length = len(str)

    print(f'{str[0]}{str[length-1]}')