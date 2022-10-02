"""

    dictionary  0----> key, value pair

        key ---> value
        no duplication in the keys ---> values from anytype

"""
"1- to define a dictionary "
d = {}
myd = dict([])


"2- dic can hold values from different datatypes"
d = {
    "name":"Ahmed",
    "track": "Python",
    "company":"itworx"
}

print(d)

"dict doesn't allow key duplication "

d = {
    "name":"Ahmed",
    "track": "Python",
    "company":"itworx",
    "name": "Yahia"
}


# myd= {
#     9: 'Carol',
#     1:"Ahmed",
#     5: "Aya",
#     4: "iti"
#
# }
# print(myd)

"--- add element to the dict "
d["address"] = 'Cairo' # " if the key doesn't exist ---> will add it to the dictionaty
# if the key exists will update the dictionary


"5- get number of key value pairs in the dic"
print(len(d))

"6- check existance of item in the dict "
if 'Yahia'in d:  # in operator ---> check in the dict keys
    print('found')
else:
    print("not found")

"7- get the dict keys "
keys = d.keys()  # dict_keys
print(keys)

# can be casted to list
keys = list(keys)
print(keys)

"8- get the dict values "
values = d.values()  # dict_values
print(values)
vals = list(values)
print(vals)

if 'Yahia' in d.values():
    print('found')


for k in d.keys():
    print(f"key = {k}")


"9- get dict items"
items =  d.items()
print(items) # dict_items ====> can be casted to a list
items = list(items)


"10- loop over the dict 000"
for i in d:
    print(i)
    print(d[i])
    print('------------------------')

for k, v in d.items():
    print(f"{k}:{v}")

"12- remove an element from the dict "
popped=d.pop("address")

del d['company']

"update dict "
info = {"name":"noha", "track":"opensource"}
courses ={
    'c1':"python",
    'c2': 'django'
}
info.update(courses)
print(info)


info.clear()  # empty dict