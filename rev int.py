def reverse(x):
    # max=2**31-1
    # min=-2**31
    # y=str(x)
    # if y[0] == '-':
    #     s=y[0]
    #     n=y[1:]
    # else:
    #     s=''
    #     n=y
    # r=n[::-1].lstrip('0')
    # # print(s,r)
    # op=s+r
    # if op == '':
    #     op='0'
    # op = int(op)
    # print(max,min)
    # if op > min and op < max:
    #     return op
    # else:
    #     return 0
    # # print(op,type(op),int(op),type(int(op)))
    while x%10 == 0:
            x = x//10
    print(x)   
    sign = 1
    if x<0:
        sign = -1
        x = x*sign
    print(x)
        
    num = 0
        
        
    while x>0:
        num = (num * 10) + (x % 10)
        print(num,x)
        x = x // 10
        print(x)
    if num*sign > 2147483647 or num*sign < -2147483648:
        return 0
            
        
    return num*sign


print(reverse(1534236461))

# 9646324351
# 2147483648

