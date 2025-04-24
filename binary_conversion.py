n=int(input())
i=0
a=''
while n!=0:
    a=str(n%2)+a
    n=n//2
    i+=1
print(a)
