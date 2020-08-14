# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/tds-and-his-breakup/

N = int(input())
X = int(input())

for n in range(N):
    try:
        Y = int(input())
        if(Y >= X):
            print("YES")
        else:
            print("NO")

    except:
        print("Error.........")