# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

string = input()

result = "YES"

try:
    N = len(string)
    for i in range(N):
        if(string[i] != string[N-1-i]):
            result = "NO"
            break

except:
    print("Something went wrong!!!")

finally:
    print(result)