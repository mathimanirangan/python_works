n=int(input())
print(n)
p=0
if n==1:
    print(0)
else:
    while n!=1:
        if (n%2==0):
            n//=2
            p+=1
        else:
            print(0,p)
    print(1,p)
