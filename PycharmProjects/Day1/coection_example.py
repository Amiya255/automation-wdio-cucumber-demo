# lists are mutable

names = ['Frank','Kirt','Scott']

print(f"The lenght of the list is {len(names)}")

print(type(names))
names.append('Andrea')

print(f"The lenght of the list is {len(names)}")
print(names[0])
print(names[-1])
print(names[-2], names[1])

print(names[2:4])

# Keywords: True False None

x = 0
person = None

# tuples

names_tuple = 'Tommy','Amiya','Anand'
print(type(names_tuple))

tuple_of_one = 'Scott',
print(type(tuple_of_one))

names_tuple_clearer = ('Tommy','Amiya','Anand','Tommy')

tommmies = names_tuple_clearer.count('Tommy')
print(tommmies)

print(names_tuple_clearer[1])
# names_tuple_clearer[-1] = "Victoria"
names[-1]="Victoria"

tuple_as_list = list(names_tuple_clearer)
tuple_as_list[-1] = "Me"

#dict
country_capitals = dict(Australia= 'Canberra',Eire= 'Dublin',France= 'Paris')
print(country_capitals['Australia'])

#Set
unique_places = {'London', 'Liverpool', 'Leeds', 'leeds', 'leeds'}
print(type(unique_places))
print(len(unique_places))
print(unique_places)

places = set(['Leeds','leeds'])
print(places)
set_as_list = list(places)


country_capitals['UK'] = 'London'
print(country_capitals)

# functions -> freestanding
len(country_capitals)

#method -> function that belongs to an object
anand_count =names_tuple.count('Anand')
print(anand_count)

var = '123'
print(var.isdecimal())

