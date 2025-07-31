# decorator is a function that accepts arguments as functions, example

def mydecorator(func):
    def start_to_end():
        print('start')
        func()
        print('end')
        
    return start_to_end

@mydecorator
def funct():
    print('Taran')

funct()

