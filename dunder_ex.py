class SuperList(list):
    lis = [0 for i in range(1000)]
   

super_list1 = SuperList()

print(len(super_list1.lis))

super_list1.lis.append(5)

print(super_list1.lis)