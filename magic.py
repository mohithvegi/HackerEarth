# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/its-magic/

N = int(input())
numbers = list(map(int, input().split()))

S = sum(numbers)

d = {}

try:
    for index in range(N):
        diff = S - numbers[index]
        if(diff%7 == 0):
            d[index] = numbers[index]

except:
    print("Error occured...")

finally:
    if(len(d) == 0):
        print("-1")
    else:
        index_min = 99999999
        min_value = 99999999
        for i in d:
            if(d[i] < min_value):
                index_min = i
                min_value = d[i]
        print(index_min)