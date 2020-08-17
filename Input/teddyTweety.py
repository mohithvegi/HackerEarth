# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/teddy-and-tweety/

N = int(input())

result = "NO"

try:
    if(N%3 == 0):
        result = "YES"

except:
    print("Error....")

finally:
    print(result)