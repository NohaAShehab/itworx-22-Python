"""
    --> built-in modules (()) os , re ---> import python
    userdefined modules ---> our own scripts
    external --> functionalities ---> install then import


    pip ---> tool ---> python package manager

    pip install ---> something
"""

"""
    dispatch 
"""


from multipledispatch import  dispatch

@dispatch(int, int)
def multuiplyInt(x, y):
    print(type(x))

@dispatch(str, int)
def multuiplyInt(x, y=100):
    print(type(x), type(y))


# multuiplyInt(10,10)
multuiplyInt("iti", 100)