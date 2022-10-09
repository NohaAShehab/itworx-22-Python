# shorthand if



"""
     do something  if condition  else ---> something else

"""

# day= 'Sunday'
#
# mood = 'happy' if day=='Thurday' else 'motivated'
#
# print(mood)



# """
#     swap functions
#
#     m = 'itworx'
#     n = 'python'
#
#     ##########################
#
#     temp = m ----> itworx
#     m = n
#     n = temp
# """
# m = 'itworx'
# n = 'python'
# print(f"m={m}, n= {n}")
# m,n = n,m
# print(f"m={m}, n= {n}")

########################

# """ enhanced print """
# print("I love python", end=' $ ')
# print("I love itworx")

###################################
"split , join "

""" split string to a list using sperator """

# info = 'noha:itworx:2022'
#
# info = info.split(":")
# print(info)
#
#
# """ join list (iterable items) to  a string """
#
# coursesinfo = ["django", 'python', 'postgres']
# coursesinfo = "&".join(coursesinfo)
#
# print(coursesinfo)



##################### enumerate function ##############


names = ["Yahia", "Shehab", "Ahmed", "Aya", "Carol", "Shrouk"]


# print(names)
"create index for the iterable"
names = enumerate(names) # enumerate object
print(names)
#
# for index, val in names:
#     print(f"{index}: {val}")



myinfo = {"name":"noha", "works":'itworx'}

# myinfo = enumerate(myinfo)

# for index, item in myinfo:
#     print(f"{index}:{item}")


# for index, item  in enumerate(myinfo):
#     print(f"{index}:{item}:{myinfo[item]}")


# l = range(1, 10)
#
# for i in enumerate(l[2:8]):
#     print(i)
#
# """ all , any """
# l =[2,3, True, 9, 0, "iti", [34,5] ]
# print(all(l))
# print(any(l))

# """ sequence unpacking """
# names = ["Yahia", "Shehab", "Ahmed", "Aya", "Carol", "Shrouk"]
#
# # a,b,c,d,e,f  = names
#
# # a, *b, c = names
# a, b, *c = names



"""

    is vs ==
"""
# x =  True
# print(x == True)
#
# print(x is 1)   # check datatype

# print("1" is 1 )
# print("1" == True)
# print(1 == True)


# x = 10
# y = 10
# print(x == y)
# print(x is y)

#
# l1 = [2,3,4]
# l2 = [2,3,4]
# print(l1 ==  l2)
# print(l1 is l2)
#


x = "10"
y = "10"
print(x == y)
print(x is y)



