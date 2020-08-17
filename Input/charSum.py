# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/char-sum-2d3a6ab5/

# 97 to 122

d = {}
position = 1

for i in range(97, 123):
    d[chr(i)] = position
    position += 1

charSum = 0

string = list(input())

try:
    for c in string:
        charSum += d[c]

except:
    print("Key error....")

finally:
    print(charSum)