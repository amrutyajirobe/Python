

#append()
#extend()
#insert()
#remove()
#clear()
#################       since tuples are immutable, slicing cannot be done

tpl = ()
print(tpl)
tp1 = (12,324,543,'XYZ')
print(tpl.count(12))            #counts the no. of occurances of the element passed
print(tpl.index('XYZ'))
print(tp1)
tp=(3,)                 #when just one element is defined, comma needs to be specified after the element
print(tp)

#while

t=(234)
print(type(t))        #considers the tuple as an integer