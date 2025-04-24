# a = 1
# sum= 5
# def parent():
#     a = 10
#     def confusion():
#         # a = 5
#         return sum
#     return confusion()

# print(parent())
# # print(confusion())
# print(a)

# def confusion(b):
#     print(b)

# total = 0

# def count(total):
#     # global  total 
#     total += 1
#     return total

# print(count(total))
# print(total)


# x = 2.8

x = {"mathi","Banana","apple","mathi"}
y = ("mat","mani","mat")

print(x,y)


# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:",x)
#     inner()
#     print("outer:",x)

# outer()