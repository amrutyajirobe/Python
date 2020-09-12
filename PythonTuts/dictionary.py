#   Dictionary is nothing but key value pairs
d = {}
#   print(type(d)) -----   o/p = <class 'dict'>
d1 ={"harry":"burger","amar":"pasta","parth":"roti"}
#   print(d1["amar"])   case sensitive

d1 ={"harry":"burger","amar":"pasta","parth":"roti","harish":{"bf":"maggi","lunch":"roti","dinner":"chicken"}}
#   print(d1["harish"]["dinner"])

d1["ankit"] = "junk food"

d1[345]="kabab"
#    print(d1)
#   del d1[345]
#   print(d1)

d3 = d1      #d3,d1 act as pointers, which references d1, removing an element from d1 doesnt affect d1
d0 = d1.copy()      #d0 acts as another dictionary copy of d1 with the same elements in it. d0 can now me modified without affecting d1
#   print(d1.get("kabab"))
d1.update({"leena":"sandwich"})
#   print(d1)
#    print(d1.keys())
#    print(d1.items())