import sys

n,k = map(int, input().split())

l = list(map(int, input().split()))

if len(l) != n:
    print("Wrong Input !!!")
    sys.exit()

Sum = 0

for i in range(0,k):
    Sum += l[i]

print(Sum)
