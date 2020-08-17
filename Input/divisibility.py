# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

N = int(input())
L = list(input().split())

last = L[len(L)-1]

result = "No"

try:
    d = list(last)
    digit = int(d[len(d)-1])
    if(digit==0):
        result = "Yes"

except:
    print("Error...")

finally:
    print(result)