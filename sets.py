
s = set()
#   doesnt allow duplicates, doesnt support indexing(setname.index(index))--is not permitted in sets
#   print(type(s))

s_from_list = set([1,2,3,4])
s_from_list.add(4)
s_from_list.remove(2)
#   print(s_from_list)


s1=s.union({1,2,3,4})
#   print(s1)
s2=s1.intersection({43,23,4321,2345})
print(s2)                   #set()


                #FROZEN-SET#
#   doesnt allow data-remove operations,like update() function

