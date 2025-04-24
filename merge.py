A=[-1,2,4]
B=[-1,-1,1,3,5]
ans = []
i=0
j=0
while i < len(A) or j < len(B):
    print(A[i],B[j])
    if A[i] >= B[j]:
        ans.append(B[j])
        j+=1
    else:
        ans.append(A[i])
        i+=1
print(ans)
