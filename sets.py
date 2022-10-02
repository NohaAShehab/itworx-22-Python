"""

    sets  0----> based on sequence

    un-ordered data type 000> no index ,  don't allow duplicates
"""

"1- to define a set"
s = {"Ahmed", "Ahmed", "Mostafa", "Aya", "Carol","Shrouk", "AbdAllah", "Yahia", "Shehab"}
print(type(s))
print(s)

"to define an empty set "
m = {} # this is a dict
m = set([]) # this is an empty set

"3- pop random elements from the set "
# popped =s.pop()
# print(popped)
# "4- remove element "
# s.remove("Ahmed")
# print(s)

"5- add item to the set "
s.add("added")

s.add("added")

"check existance "
if "added" in s:
    print('found')

"loop over the set"
for item in s:
    print(f"----> {item}")

s.add(10)


"casting to a list/ typle"

s = list(s)


mys = {1,5,3,4, 6,7,80,9, 'iti', 'ahmed'}
print(mys)