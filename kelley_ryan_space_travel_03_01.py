# Space Travel Calculator, Ryan Kelley, Code Written 01/21/20 12:46PM, Version 0.4
print("/*************************************************************************\\")
print("|                                                                         |")
print("|                                                                         |")
print("|                              SPACE TRAVEL CALCULATOR                    |")
print("|                                   Version 0.25                          |")
print("|                                       by                                |")
print("|                                   Ryan Kelley                           |")      
print("|                                                                         |")
print("|                                                                         |")
print("|                                                                         |")
print("\\*************************************************************************/")
print("Hello, I am the Space-Travel Calcubot.  I will help you determine if a mission will take more or less than three years.")  
name = input("By what name do you want to be called? [Type your name and press ENTER.]")
# print(name)
print("Hello!  It is nice to meet you,",name,".")

# Units of Measurement 
million = 1000000 # Six Zero's 
billion = 1000000000 # Nine Zero's 
trillion = 1000000000000 # Twelve Zero's 

# Averages Distances Inside Solar System [Kilometers] 
distance_mars = 225 * million 
# print(distance_mars) 

print("Mars is ", distance_mars, "kilometers away.") 
distance_sun = 150 * million
print("The Sun is ", distance_sun, "kilometers away.") 
distance_uranus = 2.9 * billion  
print("Uranus is ", distance_uranus, "kilometers away.") 