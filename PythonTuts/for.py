list = ['harry','lemta','ajbdjw','siddu']
list1 = [['harry',1],['lemta',2],['ajbdjw',3],['siddu',4]]

#for item in list:
 #   print(item)
#for item,lollypop in list1:
 #   print(item,'eats ',lollypop)


dict1 = dict(list1)
#print(dict1)

for item,lollypop in dict1.items():         # for item,lollypop in dict1:   doesnt work,throws error
    print(item,'eats ',lollypop)
list = [int,float,'amar',234,2,1,2,3,4,12,4,43,4]
for item in list:
    if str(item).isdigit() and item>6:                  #   item.isnumeric()  also yields the same output
        print(item)


