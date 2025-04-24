def myAtoi(s):
    signcheck = 0
    spacecheck = 0
    zerocheck = 0
    op=''
    for i in s:
        if i == ' ' and spacecheck == 0:
            continue
        elif i == '-' and signcheck == 0:
            spacecheck = 1
            signcheck = 1
            op=i
        elif i == '+' and signcheck == 0:
            spacecheck = 1
            signcheck = 1
            continue
        elif i == '0' and zerocheck == 0:
            spacecheck = 1
            signcheck = 1
            continue
        elif i.isnumeric():
            spacecheck = 1
            signcheck=1
            zerocheck = 1
            op+=i
        elif not i.isnumeric():
            break
    
    if len(op) > 1:
        return int(op)
    else:
        return 0

print(myAtoi('   -042'))