N=int(input())
A=input()
L=A.split()
X=int(input())
L.pop(X-1)
for i in range(len(L)):
    print(L[i],end= " ")

