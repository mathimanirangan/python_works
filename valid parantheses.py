s="()[]{}"
l=len(s)
print(l)
m=int(l/2)
if l%2 != 0:
    print(False)
print(s[0:m],s[m::])
s1=s[m-1::-1]
s2=s[m:l]
print(s1,s2)

for i in range(m-1):
    print(i,s1[i],s2[i])
    if s1[i]!=s2[i]:
        print(False)
    
print(True)
