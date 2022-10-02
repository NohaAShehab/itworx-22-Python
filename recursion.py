
#
# def askfornum():
#     while True:
#         num = input("please enter number : ")
#         if num.isdigit():
#             return  int(num)
#         print("=======> not valid please try again ========")
#
#
# n = askfornum()

def askfornum(m=0):
    print(f"---- old value = {m}")
    m = input(f"please enter number : ")
    if m.isdigit():
        m =int(m)
        return m
    print("=======> not valid please try again ========")
    return askfornum(m)
v=askfornum()
print(v)