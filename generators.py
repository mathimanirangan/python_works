
def gen_func(num):
    print('in gen fun')
    for i in range(num):
        print(f'inside for loop{i,num}')
        yield i
        

# for item in gen_func(10):
#     print(item)

g = gen_func(100)

print(g)
print(next(g))
print(next(g))


