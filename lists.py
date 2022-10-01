
""" lists ----> variable can hold different values from different datatypes
even if values 000> is another lists
lists are mutable datatypes ----> its values can be updated in the runtime


"""

"1- to define a list "
l = []
myl = list([3,5,6, "iti", True, 'Ahmed', "Carol",'Aya', ])
print(l, myl)
"2- access list elements using the index ---> start from 0 "
print(myl[2])

"3- get length of the list "
myl = [3,5,6, "iti", True, 'Ahmed', "Carol",'Aya',['python', 'django', 'flask'], 'iti']
print(len(myl))

"4- count element in the list "
print(myl.count('iti'))

'5- get index of the element in the list '
print(myl.index('iti'))

"6- update the list content  ((existing element)) "
myl[5]='updated'

'7- append element to the list ((append at the end of the list)))'
myl.append("new item added ")

"8- insert item at certain index in the list"
myl.insert(5, 'abc inserted ')

# myl.insert(50, 'Shehab')  # add it at the end of the list

# myl[20] = 'Addedddddddddddddddddd'  # must be existing index

###################
"9- pop element from the list "
popped=myl.pop()
print(popped)
print(myl)

"9- pop item at certain index "

courses = myl.pop(9)

"10- remove the element"
myl.remove('iti')  # remove the first occurrence of the value

"11- list concatenation"
courses = ["redhat", 'shell scripting', 'apache']
python = ['python', 'django', 'flask', 'odoo']
# track = courses + python
# print(track)

"12- extend A LIST"

courses.extend(python)
print(courses)

"13- sort items in the list ----> list items must be from the same type "

# courses.sort()# sort the existing list
# print(courses)

courses.sort(reverse=True)# sort the existing list
print(courses)

"14- reverse the list---> reverse the list only "
courses.append(10)
courses.reverse()
print(courses)

"15- loop over the list  000> iterable "
# for item in courses:
#     print(item)

"16-  check membership"
print("iti" in courses)
print('django' in courses)


mm = []  # this is a falsy value
if mm:
    print('found')
else:
    print('not found')