#list

my_list = [1,2,3,'a','b','c']

my_list.append('d')
print(my_list)

my_list.remove(2)
print(my_list)

print(len(my_list))

print(my_list)

my_list[2]= 5
print(my_list)


#tuples 

my_tuple = (10,20,30,40)

print(my_tuple[1])

my_tuple[2]= 35

print (my_tuple)

#sets

my_set = {1,2,2,3,4,4,5}

my_set.add(6)


my_set.remove(3)
print(my_set)

print( 4 in my_set)

#dictionaries

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'NewYork'
}

my_dict['job']= 'Engineer'
my_dict.update({'age':25})
my_dict.pop('city')
my_dict['city']= 'NewYork'
del my_dict ['city']
print(my_dict)

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x in my_dict.items():
    print(x)