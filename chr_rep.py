A=[0 for i in range(26)]
print(A)
L=input()
for i in L:
    for j in range(26):
        if i==chr(j+97):
            A[j]+=1
print(A)
Max=25
for i in range(25,-1,-1):
    if A[i] >= A[Max] and A[i] != 0:
        Max=i
    print(A[i],Max,A[Max])
print(Max+97,chr(Max+97))
