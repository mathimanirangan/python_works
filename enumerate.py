# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (dict(enumerate(l1)))
print (list(enumerate(l1,100)))
  
# changing start index to 2 from 0
print (dict(enumerate(s1, 2)))
