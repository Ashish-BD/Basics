dict = {'name':'sameer', 'desig':'s_engineer', 'place':'pune', 'name':'Rahul'}

print(dict['name'])

dict['desig'] = 'senior s_engineer'

print(dict['desig'])

print(dict)

dict['exper']='Big Data'
del dict['place']
print(dict)

for key in dict.keys():
    print(dict[key])

for key in dict.keys():
    print(key)

for v in dict.values():
    print(v)

for k,v in dict.items():
        print(k,v)

if 'name' in dict:
    print(dict.get('name'))

if 'name' in dict:
    print("Available")
else:
    print("Not available")