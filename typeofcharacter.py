A=input()
c=0
n=0
for i in range(len(A)):
    if ord(A[i]) < 58:
        n+=1
    else:
        c+=1
print(c,n)
