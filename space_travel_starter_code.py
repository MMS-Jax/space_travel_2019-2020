# Space Travel Calculator by <YOUR FIRST NAME and LAST INITIAL> on <DATE YOU WRITE THE CODE>.
# This example code should help get you started on the project.  You may have to remove # on some lines to use the code.


# Almost all computer programs should print information on the screen to explain what the program does.  

print("Replace this string with your own example.\n") # \n is a special character which means NEW LINE.  It is the same as pushing the ENTER key on the keyboard.

# Your program might say, "Hello, I am the NASA Space Travel Calculator.  I will help determine if it is possible for humans to survive a trip to different places in space."
# Print at least two sentences worth of instructions.  


# Declare variables for MILLION, BILLION, and TRILLION.  These will be used to convert distances later in the program.
million = 1000000 # Do not use commas here.  
# billion = ? # Replace the ? with the correct value for billion. 
# trillion = ? # Replace the ? with the correct value for trillion. 

# Next we need to declare the variables that will store the AVERAGE distances to each object in the Solar system.  Use Kilometers (Km) for your unit of measure.
# Mars is 225 million Km from Earth on average.  So we create a variable dist_to_mars and set it equal to 225 multiplied by the million variable. 

dist_to_mars = 255 * million 
print("The distance to Mars is", dist_to_mars, "kilometers.") # Use this to check the math is correct.

# Create two more variables for objects INSIDE OUR SOLAR SYSTEM.  Make sure to convert the distances using million, billion, or trillion.  print() the variables 
# to check that they are correct. 

# dist_to_? =
# print()
# dist_to_? =
# print()

# Next we need to find the distances to three objects OUTSIDE of our Solar System.  I have given one example for you.  This example uses scientific notation since the
# distance is so far from Earth.  If you use scientific notation you do not need to multiply the distance by million, billion, or trillion.    

dist_to_alphaCentauri = 4.4465433e13 
print("The distance to Alpha Centauri is", dist_to_alphaCentauri, "kilometers.")
# dist_to_? =
# print()
# dist_to_? =
# print()

# Next, we need to allow the program's user to select a location for travel calculations.

print("Replace this string with instructions explaining what the program will do.\n")
print("To travel to Mars select 1.\n")
print("To travel to ? select 2.\n")
print("To travel to ? select 3.\n")
print("To travel to ? select 4.\n")
print("To travel to ? select 5.\n")
print("To travel to ? select 6.\n")

where_to_travel = input("Please type a number from the list above and press ENTER.\n")  # This will print the string on the screen and wait for the user to type a number.
print("You have selected:", where_to_travel,".\n") # Print their selection back onto the screen.

# Next we will use an if/elif/else: statement to assign a value to our travel_distance variable.
travel_distance = 0 # Make the variable and set it equal to 0 to start with.

if where_to_travel == 1:
    print("You have chosen to travel to Mars.\n")
    travel_distance = dist_to_mars # Set the travel distance equal to the distance to Mars.
elif where_to_travel == 2:
    print("You have chosen to travel to ?.\n") # Change this match your choice for 2.
    # travel_distance = dist_to_? Change this set travel_distance equal to the distance for location 2.
elif where_to_travel == 3:
    print("You have chosen to travel to ?.\n") # Change this match your choice for 3.
    # travel_distance = dist_to_? Change this set travel_distance equal to the distance for location 3.
elif where_to_travel == 4:
    print("You have chosen to travel to ?.\n") # Change this match your choice for 4.
    # travel_distance = dist_to_? Change this set travel_distance equal to the distance for location 4.
elif where_to_travel == 5:
    print("You have chosen to travel to ?.\n") # Change this match your choice for 5.
    # travel_distance = dist_to_? Change this set travel_distance equal to the distance for location 5.
else:  # If it's none of these, it must be option 6.

# Next figure out how fast they want to go!
speed = input("How fast will you travel?  Type numbers only and press enter.  Your speed should is measured in Km / s.\n") # Ask the user to input a value for speed.
print("You entered: " ,speed," Km / s.\n") # Print the value back to double check.



    
    
