"""
    Access modifiers
    public
    protected ---> _varname ---> to have protected scope
    private ---> __varname ---. can be accessed only in the class
    default
    internal



"""


class Engineer:

    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        self.__salary = salary


e = Engineer("Ahmed", 'ahmed@gmail.com', 60000)
print(e.name)
e.name= 'AhmedMohamed'

print(e._email)  # ethically don't do that
# print(e.__salary)
# print(e._Engineer__salary)
e._salary = 5000
print(e._salary)