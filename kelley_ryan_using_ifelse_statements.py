# Using if / else Statements, Ryan Kelley, February 04, 2020.  Version 0.0

import random # This is a special library built-in to Python.  It has special methods, in this case .shuffle() that I will use in this code. 

print("""
   __    __       _______. __  .__   __.   _______                                                                 
  |  |  |  |     /       ||  | |  \ |  |  /  _____|                                                                
  |  |  |  |    |   (----`|  | |   \|  | |  |  __                                                                  
  |  |  |  |     \   \    |  | |  . `  | |  | |_ |                                                                 
  |  `--'  | .----)   |   |  | |  |\   | |  |__| |                                                                 
   \______/  |_______/    |__| |__| \__|  \______|                                                                 
   __   _______         ___    _______  __           _______. _______                                              
  |  | |   ____|       /  /   |   ____||  |         /       ||   ____|                                             
  |  | |  |__         /  /    |  |__   |  |        |   (----`|  |__                                                
  |  | |   __|       /  /     |   __|  |  |         \   \    |   __|                                               
  |  | |  |         /  /      |  |____ |  `----..----)   |   |  |____                                              
  |__| |__|        /__/       |_______||_______||_______/    |_______|                                             
       _______..___________.    ___   .___________. _______ .___  ___.  _______ .__   __. .___________.    _______.
      /       ||           |   /   \  |           ||   ____||   \/   | |   ____||  \ |  | |           |   /       |
     |   (----``---|  |----`  /  ^  \ `---|  |----`|  |__   |  \  /  | |  |__   |   \|  | `---|  |----`  |   (----`
      \   \        |  |      /  /_\  \    |  |     |   __|  |  |\/|  | |   __|  |  . `  |     |  |        \   \    
  .----)   |       |  |     /  _____  \   |  |     |  |____ |  |  |  | |  |____ |  |\   |     |  |    .----)   |   
  |_______/        |__|    /__/     \__\  |__|     |_______||__|  |__| |_______||__| \__|     |__|    |_______/    
                                                                                                                   
                                       by Ryan Kelley, February 04, 2020 Version 0.1
""")
print("Hello $user, this program will help you learn how to use if / else statements in your code.\n  If you have any questions while using this program please raise your hand.\n")
user = str(input("$user, by what name should I call you?  Please, type your name and then press ENTER on your keyboard.\n")) # Create a variable named user and assign it a value. 


# The following lines of code create three slices of the user name and then rearranges them. 
user1 = user[0:3]
user2 = user[4:7]
user3 = user[8:]
user = user3 + user2 + user1

print("Your parents really named you",user,"?\n")
name_correct = input("Is what really what I should call you?  [Y/N?]\n") # Create the variable name_correct and assign it a value. 
name_correct = name_correct[0] # This assigns the name_correct variable to JUST the first letter of the user's answer. 
name_correct = str.lower(name_correct) # This assigns the name_correct variable to the lower case version of that first letter.
print(name_correct) # Testing the code.  

