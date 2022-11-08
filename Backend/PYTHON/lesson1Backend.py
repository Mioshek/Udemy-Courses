#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:



def arrayCheck(nums):
    # CODE GOES HERE
    if (1 and 2 and 3 in nums):
        print(True)
    else: print(False)
    
arrayCheck([1, 1, 2, 3, 1]) 
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])
print(" ")
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

def stringBits(str):
  print(str[::2])

stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')
print(" ")

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#

def end_other(a, b):
    length_Of_A = len(a)
    length_Of_B = len(b)
    converted_A = a[length_Of_B:]
    converted_B = b[length_Of_A:]
    if (converted_A.lower() in b): print(True)
    elif (converted_B.lower() in a): print(True)
    else: print(False)

end_other('Hiabc', 'abc') 
end_other('AbC', 'HiaBc') 
end_other('abc', 'abXabc')
print(" ")
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.



def doubleChar(some_string):
  final_string = ""
  for element in some_string:
      final_string = final_string + element + element
  print(final_string)
  
doubleChar('The') 
doubleChar('AAbb') 
doubleChar('Hi-There') 
print(" ")
#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#

def is_not_teen (value):
  if (value<13 or value == 15 or value == 16 or value >19):
    return False
  else: return True
    
def no_teen_sum(a,b,c):
  if is_not_teen(a):
    a = 0
  if is_not_teen(b):
    b = 0
  if is_not_teen(c):
    c = 0
  print(a+b+c)

no_teen_sum(1, 2, 3) 
no_teen_sum(2, 13, 1) 
no_teen_sum(2, 1, 14) 
print(" ")
####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  evens = 0
  for el in nums:
    if (el%2==1):
      evens += 1
  print(evens)

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0]) 
count_evens([1, 3, 5]) 