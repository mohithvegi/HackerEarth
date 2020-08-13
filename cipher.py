# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/

message = list(input())
N = int(input())

capital_letters = []
small_letters = []

for i in range(65, 91):
    capital_letters.append(chr(i))
for j in range(97, 123):
    small_letters.append(chr(j))

for i in range(len(message)):
    c = message[i]
    if(c.isalnum()):
        if(c.isnumeric()):
            n = int(c)
            n = (n+N)%10
            message[i] = str(n)
        elif(c.islower()):
            n = ord(c)
            n = n+(N%26)
            if(n>122):
                p = n-122
                message[i] = chr(p+96)
            else:
                message[i] = chr(n)
        elif(c.isupper()):
            n = ord(c)
            n = n+(N%26)
            if(n>90):
                p = n-90
                message[i] = chr(p+64)
            else:
                message[i] = chr(n)


encrypted_message = ""

try:
    for c in message:
        encrypted_message += c
except:
    print("Error..")
finally:
    print(encrypted_message)