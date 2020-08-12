# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

L = int(input())
N = int(input())

upload_status = ""

for n in range(N):
    W,H = map(int, input().split())

    try:
        if(W<L or H<L):
            upload_status = "UPLOAD ANOTHER"
        elif(W>=L and H>=L):
            if(W == H):
                upload_status = "ACCEPTED"
            else:
                upload_status = "CROP IT"


    except:
        print("Error!!!")

    finally:
        print(upload_status)