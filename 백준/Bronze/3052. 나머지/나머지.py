rem = []
dict = {}
for i in range(10):
    rem.append(int(input()) % 42)

rem = set(rem)
print(len(rem))
