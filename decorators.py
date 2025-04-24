

# def my_decorator(func):
#     def wrap_func(*args,**kwargs):
#         print(f'the function to print \'{args[0]}\' is starting')
#         func(*args,**kwargs)
#         print('**************')
#     return wrap_func


# @my_decorator
# def hello(greeting,emoji=':('):
#     print(greeting,emoji)



# hello('hello mathi')

# from time import time

# def performance(func):
#     def wrap_func(*args,**kwargs):
#         t1=time()
#         result = func(*args, **kwargs)
#         t2=time()
#         print(f'it took {t2-t1} s')
#         # return result
#     return wrap_func
    


# @performance
# def long_time():
#     print('1')
#     for i in range(100):
#         print(i*5)

# long_time()

# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100)):
#         print(i*5)

# long_time2()

class MyGen:
    
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.first < self.last:
            num = self.first
            self.first +=1
            return num
        raise StopIteration
    

gen = MyGen(5,100)

# geni = iter(gen)

print(next(gen))
# for i in gen:
#     print(i)

