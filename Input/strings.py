# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/

T = int(input())

for t in range(T):
    words = list(input().split())

    word1 = list(words[0])
    word2 = list(words[1])
    length1 = len(word1)
    length2 = len(word2)

    result = "YES"

    d1 = {}
    d2 = {}

    for c1 in word1:
        d1[c1] = 0
    for c2 in word2:
        d2[c2] = 0

    try:
        for c1 in word1:
            d1[c1] += 1
        for c2 in word2:
            d2[c2] += 1

        for c in d1:
            if c not in d2:
                result = "NO"
                break
            elif(d1[c] != d2[c]):
                result = "NO"
                break

        for x in d2:
            if x not in d1:
                result = "NO"
                break

    except:
        print("Error!")

    finally:
        print(result)