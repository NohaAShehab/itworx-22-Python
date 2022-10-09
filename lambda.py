"""
    use function ----> one time ---->
"""

# num =  lambda x : x*4  # callable object
#
# print(num) #
#
# print(num(3))

# ### return with a function

# def sumnum(num):
#     print(f"num =  {num}")
#     return lambda x : x+num
# # m = sumnum(10)
# # print(m(6))
# m = sumnum(10)(7)
# print(m)
##############################################################

l = [3,4,5] # multiply list elements by 3

# newl = map(lambda x:x*3, l)
# print(newl)
# newl = list(newl)
# print(newl)

# newl = map(lambda x:x*3, [x for x in range(10)])
# newl = list(newl)
# print(newl)

###################################
""" filter """


l = list(range(0,11))

newl = filter(lambda x : x%2==0, l)
print(newl) # filter object
newl = list(newl)
print(newl)


