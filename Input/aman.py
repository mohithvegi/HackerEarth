# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/aman-mrsharma/

D = int(input())

pi = 22/7
toffees = 0

for d in range(D):
    L = list(map(int, input().split()))
    r = L[0]
    x = L[1]
    circumference = (2*pi*r)
    capacity = x*100
    circles = int(capacity/circumference)
    if(circles>=1):
        toffees += 1

print(toffees)