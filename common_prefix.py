strs = ["mathi","mani","mathi"]
r=""
c=0
check=True
s=strs[0]
print(s)
while check and r!=s:
    ch=s[c:c+1]
    for i in strs:
        if ch!=i[0:c+1]:
            check=False
    c+=1
    print(c)
    r+=ch
print(r)
        
