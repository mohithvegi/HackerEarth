# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

def fact(N):
    if(N==0 or N==1):
        return 1
    else:
        return N*fact(N-1)

if __name__ == '__main__':

    N = int(input())

    try:
        print(fact(N))
    except:
        print("Error")