s=['a','b','n','c','b','d','m','n','n','b']
result=[]
master=[]
c=0

for v in s:
    if s.count(v) > 1:
        if v not in result:
            for x in s:
                if x == v:
                    result.append(x)
     

# while c < len(s):
#     check=[]
#     check.append(s[c])
#     if s[c] in master:
#         c+=1
#         continue
#     else:
#         master.append(s[c])
#     d=c+1
#     while d < len(s):
#         # print(s[c],s[d])
#         if s[c] == s[d]:
#             check.append(s[d])
#         d+=1
#     if len(check) > 1:
#         result.extend(check)    
#     c+=1

print(result)