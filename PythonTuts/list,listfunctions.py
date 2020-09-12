
#mutable -- can change(list)
#immutable -- cannot change(tuple)


grocery = ["harpic","bhindi","deo","lollypop","amul"]

#   print(grocery)
#   print(grocery[0])
numbers = [32,324,23,21312,23,3,434,2,4,234,532,4,32,5]
#   numbers.sort()
#   numbers.reverse()
#   numbers.sort(reverse=True)      prints the list in reverse order in decreasing order
#   numbers.append(7)
#   numbers.insert(1,43)
#   numbers.clear()             empties the list
#   print(max(numbers))                returns the max element from the list
#   inserting 43 at ith index, also note that the elements arent eliminated, only moved to either side,but, -->
#   numbers[1] = 9897       replaces the integer at that index
#   numbers.pop() -----------removes the last index element
#   numbers.remove(some integer)        removes that integer from the list
#
#
#   print(numbers)

                    #SLICING#


#   print(numbers[::-2])        is acceptable, wont give [] as an output
#                    |
#               any -ve number passed over here is accepted until there are no limits passed before
#
#   print(numbers[1:2:-3]       returns [] as an ouput



                    #TUPLE#
    #to make tuple of only one element, use tp = (1,)
tp = (1,2,3)
#   print(tp)
#

#       to swap two or more integers.,for ex .,
#   a=1
#   b=4
#   a,b=b,a             numbers are swapped now


#   list can be converted to tuple, for ex.,
list=[1,23,32,34,3]
tpl= tuple(list)
print(type(tpl))