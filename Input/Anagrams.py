# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

T = int(input())

for t in range(T):
    string1 = list(input())
    string2 = list(input())

    d1 = {}
    d2 = {}

    for i in string1:
        d1[i] = 0
    for i in string2:
        d2[i] = 0

    count = 0

    for s1 in string1:
        d1[s1] += 1
    for s2 in string2:
        d2[s2] += 1

    try:
        for c in d1:
            if c not in d2:
                count += d1[c]
            else:
                count += abs(d1[c] - d2[c])
        for c in d2:
            if c not in d1:
                count += d2[c]

    except:
        print("Error Occured!!!!")

    finally:
        print(count)