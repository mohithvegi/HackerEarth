# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/

numbers = list(input().split())

X = list(numbers[0])
K = int(numbers[1])

length = len(X)
i=0

while(i<length and K>0):
    digit = int(X[i])
    if(digit != 9):
        X[i] = str(9)
        K = K-1
    i += 1

result = ""

for x in X:
    result += x

print(result)