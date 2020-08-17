# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/back-to-school-1/

numbers = list(map(int, input().split()))

try:
    print(max(numbers))
except:
    print("Error....")