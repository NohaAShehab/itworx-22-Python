# l = ["Ahmed", "Aya", "Carol", "Shehab", "AbdAllah", "Yahia"]
#
# # for item in l:
# #     print(item)
#
# l = iter(l)
#
# print(l)  # list iterator object
#
# print(next(l))
# print("------------------")
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(next(l))
#
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
#



#
# counter = [i for i in range(100)]
# print(counter)

#### generate number
# def generatenum():
#     for i in range(100):
#         return i
#
# n = generatenum()
# print(n)
# m = generatenum()
# print(m)

###############################


def generatenum():
    for i in range(100):
        yield i

n = generatenum()   ### generator object
print(next(n))

print(next(n))
print(next(n))








