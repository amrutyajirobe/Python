
from abc import abstractmethod,ABC          # necessary for abstraction. This helps create abstract classes(here,BMW)
                                            # threeseries, fiveseries are interfaces cum subclasses used for method implementation

class bmw(ABC):

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod
    def start(self):
        #print('starting the car')
        pass

    @abstractmethod
    def stop(self):
        #print('stopping the car')
        pass

    @abstractmethod
    def drive(self):            # parameters can also be passed
        pass                    # this is necessary, and this method has to be implemented in subclassses

class threeseries(bmw):

    def __init__(self,cruiseControlEnabled,make,model,year):
        bmw.__init__(self,make,model,year)                   #         super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print('button start')


    def stop(self):
        super().stop()
        print('button stop')


    def drive(self):
        print('threeseries DRIVE')



class fiveseries(bmw):

    def __init__(self,parkingAssist,make,model,year):
        bmw.__init__(self,make,model,year)          #         super().__init__(make,model,year)
        self.parkingAssist=parkingAssist


    def display(self):
        print(self.parkingAssist)

    def start(self):
        super().start()
        print('remote start')

    def stop(self):
        super().stop()
        print('remote stop')

    def drive(self):
        print('fiveseries DRIVE')



threeseries=threeseries(True,'bmw','324i','2018')
print(threeseries.cruiseControlEnabled)
print(threeseries.model)
print(threeseries.make)
print(threeseries.year)
threeseries.start()
threeseries.stop()



fiveseries=fiveseries(True,'volvo','2342l','2022')
print(fiveseries.parkingAssist)
print(fiveseries.model)
print(fiveseries.year)
print(fiveseries.make)
fiveseries.start()
fiveseries.stop()
