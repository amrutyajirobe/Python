
class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class engine:
        def __init__(self,number):
            self.number=number
        def starts(self):
            print('engine started')


c=car('BMW',2017)

e=c.engine(234)
e.starts()