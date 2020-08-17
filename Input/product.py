# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

N = int(input())

numbers = list(map(int, input().split()))

product = 1
modulo = 1000000007

try:
    for n in numbers:
        product = product*n

except:
    print("Error occured!!!")

finally:
    print(product%modulo)