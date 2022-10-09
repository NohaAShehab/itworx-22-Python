""" open file """

# try:
#     with open("mycv.txt", 'w') as myfile:
#         myfile.write("This is mycv file")
#
# except Exception as e :
#     print(e)

""" list comprehension """

### list of even number from 0 to 100
# l  = []
# for i in range(101):
#     if i %2 ==0:
#         l.append(i)
#
# print(l)

# l = [i for i in range(11) if i%2 ==0]
# print(l)

l = [i*i for i in range(11) if i%2 ==0 ]
print(l)