# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

string = input()
result = ""

try:
    length = len(string)
    for i in range(length):
        c = string[i]
        if(c.isupper()):
            result += c.lower()
        elif(c.islower()):
            result += c.upper()

except:
    print("Error!!!!!!!")

finally:
    print(result)