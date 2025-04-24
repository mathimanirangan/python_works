import math
L='18 6 15 2 19 11 20 15 16 8 10 1 19'
A=L.split()
n=len(A)
print(n)
sum=0
g=3
b=4
for i in range(len(A)):
    sum+=int(A[i])
print(L)
print(A)
print(sum)
print(sum/n)
mu = sum/n
sig_sum=0
for i in range(n):
    print(A[i],(int(A[i])-mu)*(int(A[i])-mu))
    sig_sum+=(int(A[i])-mu)*(int(A[i])-mu)
print(sig_sum)
sig=math.sqrt((sig_sum/n-1))
print(sig)
for i in range(n):
    print(g*((int(A[i])-mu)/sig)+b)
