# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/i-am-easy/

N = int(input())

try:
    for n in range(1,11):
        print(n*N)

except:
    print("Error reading input...")