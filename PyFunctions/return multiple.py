def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    t=a/b
    return x,y,z,t   #  returns result in tuple-format

res = calc(13,43)
for i in res:
    print(i)