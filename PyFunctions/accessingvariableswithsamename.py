
#   using globals for accessing variables with same name declared globally as well as locally

x=123

def display():
    x=3245
    print(globals()['x'])
    print(x)

print(x)
#   display()
z=display()
z()         #   to invoke display function
