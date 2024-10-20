my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print(my_cat)
my_cat['age']=2
print(my_cat)

print(my_cat['color'])

print(my_cat.values())
for value in my_cat.values():
    print(value)

print(my_cat.keys())
for k in my_cat.keys():
    print(k)

for k in my_cat:
    print(k)

print(my_cat.items())



