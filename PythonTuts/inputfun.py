s=input()
print(s)
s=input('enter your name :')
print(s)

i=int(input("enter an integer value"))
print(type(i))

#       reading multiple inputs
lst = [x for x in input('enter 3 integers seperated by space:').split()]
print(lst)

lyst = [x for x in input('enter 3 integers seperated by comma:').split(',')]
print(lyst)

lt = [int(x) for x in input('enter 3 integers seperated by space:').split()]        #float(x) can also be used for float values
print(lt)