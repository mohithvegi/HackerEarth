# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/

binary = list(input())

m = 0

if(int(binary[0]) == 0):
    flag = 0
    count = 0
    for i in range(len(binary)):
        if (int(binary[i]) == flag):
            count += 1
            if (count > m):
                m = count
        else:
            count = 1
            flag = 1
else:
    flag = 1
    count = 0
    for i in range(len(binary)):
        if (int(binary[i]) == flag):
            count += 1
            if (count > m):
                m = count
        else:
            count = 1
            flag = 0

# print(len(binary))
if(m>=6):
    print("Sorry, sorry!")
else:
    print("Good luck!")