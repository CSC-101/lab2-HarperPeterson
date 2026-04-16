# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("hpeter21@calpoly.edu")
print(message)

def smallest(n:float,m:float):
   if n < m:
      return n #This statement isn't evaluated for any of the calls below
   else:
      return m

first = smallest (3,2) # The value of first is 2
second = smallest (2,2) # The value of second is 2. This isn't a reasonable result since we know that 2=2, so it would be smart to have an elif for when n = m
print()

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b #This will be called when a is the greatest integer
   elif b > c:
      return b + c #This will be called when b is the greatest integer
   else:
      return 2 * c #This will be called when c is the greatest integer

answer1 = function2(3,2,1) #The value of answer1 is 1
answer2 = function2(2,3,1) #The value of answer2 is 4
answer3 = function2(2, 1, 3) #The value of answer3 is 6
from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L) #test is false on the first call, and true on the second call
   if test: #this check makes sure we only return a result when we have an index we can take
      return L[idx]
   else:
      return None

first = checked_access([1, 0, 1], 9) # first = None, no value
second = checked_access([1, 0, 1], 2) # second = 1

def length_sum(L:list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2]) #Evaluated for first call, 4, 2, and 3 are added
   elif len(L) > 1:
      result = len(L[0]) + len(L[1]) #Evaluated for third call, 7 and 4 are added
   elif len(L) > 0:
      result = len(L[0]) # Evaluated for second call, only 11 is added
   else:
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])

def surprising(L:list[str], other:str) -> list[str]:
   L.append(other.upper())
   return L

words = ['this', 'is', 'confusing', 'code.'] #words is the list "this is confusing code."
first = surprising(words, "Avoid") # first is ["this", "is", "confusing", "code.", "AVOID"]
second = surprising(words, "such.") # second is ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
# The code added the words "avoid" and "such." to the end of the list in an uppercase form, and no errors were raised when making "such." uppercase, despite the period.
