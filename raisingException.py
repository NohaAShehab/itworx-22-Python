""" handle exception

    try:
        dosomething
    except:
        do something
    else:
        ----
    finally:
        ------

#################### you must raise exception
"""
def divNums():
    x = input("please enter num1 : ")
    y = input("please enter num2 : ")
    if y =="0":
        # raise Exception("please try again , Cannot divide by zero ")
        print("------------ provide suitable num2: ")
        return divNums()

    if x.isdigit():
        x = int(x)
        if y.isdigit():
            y = int(y)
            return x/ y

    return None


s = divNums()
print(s)
