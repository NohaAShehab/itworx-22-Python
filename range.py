"""

    range ===> create range object- > iterable  ----> get set of values

"""

r = range(10)  # start =0, stop = 10 , step=1
print(r)

"cast range to a list "
# r = list(r)
# print(r)  # generate set of values from start to stop-step


# for i in range(10):
#     print(i)
#
#
#
# ## geneerate range
# myr =  range(10, 1, -1)
# print(list(myr))

##################################3333


for i in range(10):
    # if i ==9:
    #     continue

    print(i)
else:
    "this block will be executed only when loop finishes all the iterations"
    print("----------- loop completed the iterations ------------------------")


"""
    if(){}

"""

if True:
    pass


# while True:
#     pass


# n = int(input("please enter your number  : "))
n = input("please enter your number  : ")
if n.isdigit():
    n = int(n)

