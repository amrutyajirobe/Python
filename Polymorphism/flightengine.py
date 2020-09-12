# demonstrating working of interfaces
#       engine is a parent interface for airbusengine and boeingengine classes          # basically by ducktyping for dependency-injection

class flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start()                 #  assuming that engine objects will have a start function



class airbusengine:
    def start(self):
        print('starting airbus engine')


class boeingengine:
    def start(self):
        print('starting boeing engine')



ae = airbusengine()

f=flight(ae)
f.startEngine()