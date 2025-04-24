


def fibonnaci(num):
    prev = 0
    curr = 1
    if num == 0:
        print(0)
    elif num == 1:
        print(prev)
        print(curr)        
    elif num > 1:
        print(prev)
        print(curr)
        for i in range(2,num):
            print(curr+prev)
            prev1=curr
            curr=prev+curr
            prev=prev1
    

    
    
    
fibonnaci(19)