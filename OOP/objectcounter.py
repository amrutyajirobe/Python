

class objectcounter:
    noofobjs=0

    def __init__(self):
        objectcounter.noofobjs+=1


    #@staticmethod
    def display():
        print(objectcounter.noofobjs)

o1=objectcounter()
o2=objectcounter()

objectcounter.display()
