def sf(name,*args,i=1,**kwargs):
    print(name,i,args,kwargs)
    return sum(args) + sum(i for i in kwargs.values())

print(sf('mathi',1,2,3,4,5,num1=5,num2=10))