# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/vc-pairs/

T = int(input())

for t in range(T):
    N = int(input())
    word = input()

    vowels = ['a','e','i','o','u']

    count = 0

    try:
        for i in range(N-1):
            if(word[i] not in vowels):
                if(word[i+1] in vowels):
                    count += 1

    except:
        print("Error....")

    finally:
        print(count)