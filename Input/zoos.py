# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

word = input()

result = "No"

try:
    x=0
    y=0
    for i in range(len(word)):
        if(word[i] == 'z'):
            x = x+1
        else:
            y = y+1

    if(2*x == y):
        result = "Yes"
except:
    print("Something went wrong!!!")
finally:
    print(result)