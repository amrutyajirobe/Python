
"""class student:

    def __init__(self):
        #self.id=id          #self.__id=id       making it private
        #self.name='John'    #self.__name=name   making it private
        self.__id = 123
        self.__name='john'

    def display(self):
        print(self.__id)
        print(self.__name)

s=student()
#print(s.id)                    # wrong
#print(s.name)                  # wrong
s.display()
print(s._student__id)           # this makes the private variable accessible
print(s._student__name)         # this makes the private variable accessible

"""




class student:

    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    

s=student()
s.setId(1234)
s.setName('john')
print(s.getName())
print(s.getId())

