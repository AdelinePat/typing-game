class Test:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

class Test2(Test):
    def print_name(self):
        print(self.name + '11')

test = Test('baba')
test.print_name()
test1 = Test2('bobo')
test1.print_name()