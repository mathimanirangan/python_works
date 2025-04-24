def highest_even(li):
    li.sort(reverse=True)
    for i in li:
        if i%2 == 0:
            return i
    # return op

print(highest_even([10,2,3,4,8,11]))