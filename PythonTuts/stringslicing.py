#   myst= "enter your name"
#   print(myst)
#   print(myst[0:4])    which is equivalent to print(myst[:4])
#
#
#   by default, print(myst[::]) is equivalent to print(myst[0:len(myst):1])
#   print(myst(::556778))
#   output - e
#
#
#   print(myst([::-1]))       prints the string in reverse order
#   print(myst.isalnum())           o/p = false
#   print(myst.isalpha())           o/p = false


#   print(myst.endswith("name"))        o/p = true

#   print(myst.count("e"))          o/p = 3

#   print(myst.capitalize())           o/p =   ENTER YOUR NAME

#   print(myst.find("name"))       o/p = 11

#   print(myst.upper())
#   print(myst.lower())

 #  print(myst.replace("name","rollno"))    o/p = enter your rollno


#  capitalize() - Converts the first character to upper case
#  casefold() - Converts string into lower case
#  center() - Returns a centered string
#  count() -  Returns the number of times a specified value occurs in a string
#  encode() - Returns an encoded version of the string
#  endswith() - Returns true if the string ends with the specified value
#  expandtabs() - Sets the tab size of the string
#  find() - Searches the string for a specified value and returns the position of where it was found
#  format() - Formats specified values in a string
#  format_map() - Formats specified values in a string
#  index() -  Searches the string for a specified value and returns the position of where it was found
#  isalnum() -  Returns True if all characters in the string are alphanumeric
#  isalpha() -  Returns True if all characters in the string are in the alphabet
#  isdecimal() -  Returns True if all characters in the string are decimals
#  isdigit() -  Returns True if all characters in the string are digits
#  isidentifier() - Returns True if the string is an identifier
#  islower() -  Returns True if all characters in the string are lower case
#  isnumeric() -  Returns True if all characters in the string are numeric
#  isprintable() -  Returns True if all characters in the string are printable
#  isspace() -  Returns True if all characters in the string are whitespaces
#  istitle() -  Returns True if the string follows the rules of a title
#  isupper() -  Returns True if all characters in the string are upper case
#  join() - Joins the elements of an iterable to the end of the string
#  ljust() -  Returns a left justified version of the string
#  lower() -  Converts a string into lower case
#  lstrip() - Returns a left trim version of the string
#  maketrans() -  Returns a translation table to be used in translations
#  partition() -  Returns a tuple where the string is parted into three parts
#  replace() -  Returns a string where a specified value is replaced with a specified value
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
#  rindex() - Searches the string for a specified value and returns the last position of where it was found
#  rjust() -  Returns a right justified version of the string
#  rpartition() - Returns a tuple where the string is parted into three parts
#  rsplit() - Splits the string at the specified separator, and returns a list
#  rstrip() - Returns a right trim version of the string
#  split() -  Splits the string at the specified separator, and returns a list
#  splitlines() - Splits the string at line breaks and returns a list
#  startswith() - Returns true if the string starts with the specified value
#  strip() -  Returns a trimmed version of the string
#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
#  title() -  Converts the first character of each word to upper case
#  translate() -  Returns a translated string
#  upper() -  Converts a string into upper case
#  zfill() -  Fills the string with a specified number of 0 values at the beginning


##          defining strings across lines
s="""this is amrutya
who believes that everyman is 
the creator of his own destiny"""
print(s)
print(s[0])
print(s*2)      ##displays the string twice
print(len(s))
print(s[0:8])