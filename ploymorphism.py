class Parent:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print("Hi from class Parent")


class Child(Parent):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    # overriding
    def sayhi(self):
        # call (say_hi)parent function here
        # super(Child, self).sayhi()
        super().sayhi()
        print(f"you can reach at me at {self.email}")

    def test(self,message, num=0):
        print(message)

    # def test(self, message:int, num ):
    #     print(message)


c = Child("Ahmed", 'Ahmed@gmail.com')
c.sayhi()
c.test("abc", 10)
c.test('abc')
