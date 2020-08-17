# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/doctors-secret/

L = list(map(int, input().split()))

length = L[0]
pages = L[1]

decision = "Don't take Medicine"

try:
    if(length<=23 and pages>=500 and pages<=1000):
        decision = "Take Medicine"

except:
    print("Error......")

finally:
    print(decision)