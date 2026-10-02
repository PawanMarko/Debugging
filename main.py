#DAY 13 TODAY WE ARE GO TO LEAR DEBUDDING!!

def my_function():
  for i in range(1, 21): # in range it gose for 1 to 19 so ans is in range is 1 to 21..
    if i == 20:
      print("you got it")
      
my_function()
"""
# Reproduce the bug..
"""
from random import randint
dice_image = ["1", "2", "3", "4", "5", "6"]  #(In Python, list indexes start at 0, not 1. 
dice_num = randint(0, 5)             # Make the random number generate values from 0 to 5 instead of 1 to 6 so it work.)
print(dice_image[dice_num]) 

# PLAY COMPUTER..
year = int(input("What's your year of birth??"))

if year >= 1980 and year <= 1994:
  print("YOU ARE A MILLENNIAL")  # You wrote if year > 1980 and year < 1994:# → This excludes people born in 1980 and 1994.
                                
elif year > 1994:            # ✅ Fix: Use >= and <= instead of > and < if you want to include boundary years:
  print("you are a Gen Z..") 

else:
  print("You are older than a Millennial!")
  
# FIX THE ERRORS.. 

try:
   age = int(input("How old you are??"))
  
except ValueError:
   print("You have typed in a invalid number. Please try it again with a numerical responce such as 15")
   age = int(input("How old you are??"))

if age > 18:
   print(f"You can drive at age {age}.")  