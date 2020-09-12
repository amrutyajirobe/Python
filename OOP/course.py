
class course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings

    def average(self):
        noofRatings=len(self.ratings)
        average=sum(self.ratings)/noofRatings
        print("average : ",average)

s1=course('python',[12,3,13,4])
print(s1.name,s1.ratings)
s1.average()

s2=course('java',[1,32,1233,42])
print(s2.name,s2.ratings)
s2.average()