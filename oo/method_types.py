class A():
    count = 0

    # instance method (because it has the initial self argument)
    def __init__(self):
        A.count += 1

    # instance method
    def exclaim(self):
        print('I am an A!')

    # a class method affects the class as a whole
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")

a = A()
b = A()
c = A()
A.kids()
