l1 = int(input())
l2 = int(input())

l3 = (l2 % 10) * l1
l4 = int(((l2 / 10) % 10)) * l1
l5 = int(((l2 / 100) % 10)) * l1
l6 = l3 + (10 * l4) + (100 * l5)

print(l3)
print(l4)
print(l5)
print(l6)