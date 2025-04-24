from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def cap(name):
    return name.capitalize()

print(list(map(cap,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()

zip_list = list(zip(my_strings,my_numbers))
print(zip_list)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def pass_check(mark):
    return (mark*100)/100 > 50

print(list(filter(pass_check,scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def agg(acc,num):
    return acc+num

print(my_numbers+scores)
acc1 = reduce(agg,my_numbers,0)

acc2 = reduce(agg,scores,acc1)

print(acc2)