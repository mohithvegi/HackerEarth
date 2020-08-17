# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisibe-or-2d8e196a/

N = int(input())
L = list(input().split())

L1 = []
L2 = []

middle = int(N/2)

for i in range(middle):
    L1.append(L[i])

for j in range(middle, len(L)):
    L2.append(L[j])

result = "NON"

try:
    n1 = ""
    n2 = ""
    for l1 in L1:
        n1 += l1[0]
    for l2 in L2:
        n2 += l2[len(l2)-1]

    number = int(n1+n2)
    if(number%11 == 0):
        result = "OUI"

except:
    print("Error.....")

finally:
    print(result)