for i in range(10):
    print(i, end="  ")
print()
for i in range(0, 10):
    print(i, end="  ")
print()
for i in range(0, 10, 1):
    print(i, end="  ")
print()

for i in range(10-1, -1, -1):
    print(i, end="  ")
print()

for i in reversed(range(10)):
    print(i, end=" ")
print()


s = 0
for i in range(5):
    s+=i
    print(s)

s = ''
for i in range(5):
    s +=str(i+1) + " "
    print(s)
#
