"""
    tuple like lists ----> immutable datatype
    ---> can hold different values from different datatypes
    --->
"""

"1- to define a tuple "
t = ()
myt = tuple([3,5,6, "iti", True, 'Ahmed', "Carol",'Aya', ])
print(t, myt)


"2- access tuple elements using the index ---> start from 0 "
print(myt[2])

"3- get length of the tuple "
myt = (3,5,6, "iti", True, 'Ahmed', "Carol",'Aya',
       ['python', 'django', 'flask'], 'iti')
# print(len(myt))
#
# myt[8].append("itworx")
#
# "4- count element in the tuple "
# print(myt.count('iti'))
#
# '5- get index of the element in the tuple '
# print(myt.index('iti'))
#
#
# "6- tuple concatenation"
courses = ("redhat", 'shell scripting', 'apache')
python = ('python', 'django', 'flask', 'odoo')
# track = courses + python

"7- loop over the tuple  000> iterable "

for i in myt:
    print(i)

"8-  check membership"
print("iti" in courses)
print('django' in courses)
"9- empty tuple is a falsy value "

t = ()
if t:
    print("found")
else:
    print('not found ')

"10 - tuple of one item"

# names = ('AbdAllah',)
# print(type(names))

names = tuple(["Mostafa"])

# nums  = (3)

"11- convert tuple to list  "
print(courses, type(courses))
courses = list(courses)
print(courses, type(courses))  # list

t = tuple(courses)
print(t)

"del- ----> works with any varaible ----> from any type "

del courses[1]
del python


""" No null but None """