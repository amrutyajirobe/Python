try:

    
    f=open("myfile","w")
    a,b=[int(x)for x in input('enter two integers').split()]
    c=a/b
    f.write("writing %d into file" %c)

except ZeroDivisionError:
    print("zero division error detected")

else:
    print('you have entered a non zero number')

finally:
    f.close()
    print('file closed')
print('code after the exception')