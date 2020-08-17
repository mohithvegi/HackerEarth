# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

numbers = list(map(int, input().split()))
l = numbers[0]
r = numbers[1]
k = numbers[2]

count = 0

try:
    for n in range(l, r+1):
        if(n%k == 0):
            count += 1

except:
    print("Error!!!!!")

finally:
    print(count)