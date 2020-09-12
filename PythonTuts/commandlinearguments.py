#   COMMANDLINE ARGUMENTS


#   python          filename.py         123 abc xyz
#   FileLocation    Database            Remote IP

# argv is a list that contains all our commandlinearguments, argv is present inside the sys module
# to access the elements, sys.argv is used. Fo ex., sys.argv[0]

import sys

lst = sys.argv
for i in lst: print(i)
#   print(len(lst))

#   print(lst[0])           #display the complete path

print('product is :',int(lst[1])*int(lst[2]))
