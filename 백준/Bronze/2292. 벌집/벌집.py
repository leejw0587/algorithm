N = int(input())

house = 1
repeat = 1

while N > house:
    house += 6 * repeat
    repeat += 1

print(repeat)
