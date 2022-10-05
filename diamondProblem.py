
class Parent:
    def sayhi(self):
        print("Hi from class Parent")
    pass

class ParentOne(Parent):
    # def sayhi(self):
    #     print("Hi from class ParentOne")
    pass

class ParentTwo(Parent):
    # def sayhi(self):
    #     print("Hi from class ParentTwo")
    pass


class Child(ParentOne, ParentTwo):
    # def sayhi(self):
    #     ParentOne.sayhi(self)
    #     ParentTwo.sayhi(self)
    #     Parent.sayhi(self)
    pass

c = Child()
c.sayhi()