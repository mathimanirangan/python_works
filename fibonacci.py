


# def fibonnaci(num):
#     prev = 0
#     curr = 1
#     if num == 0:
#         print(0)
#     elif num == 1:
#         print(prev)
#         print(curr)        
#     elif num > 1:
#         print(prev)
#         print(curr)
#         for i in range(2,num):
#             print(curr+prev)
#             prev1=curr
#             curr=prev+curr
#             prev=prev1

def feb(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a
    
for i in feb(20):
    print(i)

    

    
    
    
# fibonnaci(19)