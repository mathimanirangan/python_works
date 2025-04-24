from functools import wraps

def log_before_after(fun):
    @wraps(fun)
    def outer(*args,**kwargs):
        print(f"{fun.__name__} called with {args=},{kwargs=}")
        result= fun(*args,**kwargs)
        print(f"{fun.__name__} returned {result=}")
        return result
    return outer
@log_before_after
def average_grade(grades):
    return sum(grades)/len(grades)

print(average_grade([3,4,4,5,5,5,2]))

