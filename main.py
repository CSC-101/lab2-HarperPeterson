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
      return a - b #This will be called when a is the greatest interger
   elif b > c:
      return b + c #This will be called when b is the greatest interger
   else:
      return 2 * c #This will be called when c is the greatest interger

answer1 = function2(3,2,1) #The value of answer1 is 1
answer2 = function2(2,3,1) #The value of answer2 is 4
answer3 = function2(2, 1, 3) #The value of answer3 is 6