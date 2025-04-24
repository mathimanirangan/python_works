some_list = ['a','b','c','b','d','m','n','n']


duplicates = list({i for i in some_list if some_list.count(i) > 1 })

print(duplicates)