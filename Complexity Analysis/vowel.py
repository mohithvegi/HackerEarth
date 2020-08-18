# https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/vowel-game-f1a1047c/

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def Substrings(s, n):
    A = []
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            A.append(temp)
    return A

def countVowels(string):
    count = 0
    for index in range(len(string)):
        if string[index] in vowels:
            count += 1
    return count

if __name__ == '__main__':

    T = int(input())
    for t in range(T):
        string = input()
        res = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
        # substrings = Substrings(string, len(string))
        count = 0
        for s in res:
            count += countVowels(s)

        print(count)