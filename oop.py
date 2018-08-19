class Greeter(object):
    def __init__(self,namee):
        self.namee = namee
    
    def greet(self,b,loud = False):
        if loud:
            print('HELLO, %s %d' % (self.namee.upper(),b))
        else:
            print('Hello, %s %d' % (self.namee, b))



g = Greeter('Cheryl')
g.greet(5)