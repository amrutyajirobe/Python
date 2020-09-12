

def dis():
    def fun():
        return "hello!"
    return fun

a=dis()
print(a())

