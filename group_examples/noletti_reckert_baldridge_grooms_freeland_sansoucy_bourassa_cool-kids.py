# Space Travel Calculator, Ryan Kelley, 02/10/20 12:45PM, Version 1.0
import time
print("""
.▄▄ ·  ▄▄▄· ▄▄▄·  ▄▄· ▄▄▄ .                              
▐█ ▀. ▐█ ▄█▐█ ▀█ ▐█ ▌▪▀▄.▀·                              
▄▀▀▀█▄ ██▀·▄█▀▀█ ██ ▄▄▐▀▀▪▄                              
▐█▄▪▐█▐█▪·•▐█ ▪▐▌▐███▌▐█▄▄▌                              
 ▀▀▀▀ .▀    ▀  ▀ ·▀▀▀  ▀▀▀                               
▄▄▄▄▄▄▄▄   ▄▄▄·  ▌ ▐·▄▄▄ .▄▄▌                            
•██  ▀▄ █·▐█ ▀█ ▪█·█▌▀▄.▀·██•                            
 ▐█.▪▐▀▀▄ ▄█▀▀█ ▐█▐█•▐▀▀▪▄██▪                            
 ▐█▌·▐█•█▌▐█ ▪▐▌ ███ ▐█▄▄▌▐█▌▐▌                          
 ▀▀▀ .▀  ▀ ▀  ▀ . ▀   ▀▀▀ .▀▀▀                           
 ▄▄·  ▄▄▄· ▄▄▌   ▄▄· ▄• ▄▌▄▄▌   ▄▄▄· ▄▄▄▄▄      ▄▄▄      
▐█ ▌▪▐█ ▀█ ██•  ▐█ ▌▪█▪██▌██•  ▐█ ▀█ •██  ▪     ▀▄ █·    
██ ▄▄▄█▀▀█ ██▪  ██ ▄▄█▌▐█▌██▪  ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄     
▐███▌▐█ ▪▐▌▐█▌▐▌▐███▌▐█▄█▌▐█▌▐▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌    
·▀▀▀  ▀  ▀ .▀▀▀ ·▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀    
                by
            Ryan Kelley
            February 10, 2020
            Version 1.0
""")
print("This Space Travel Calculator determines if an outerspace mission will take more or less than three years.")
user_name = input("What is your name? [Please type your name and press ENTER.]  ")
print("Hello, how are you?  It is nice to meet you", user_name,"!")
time.sleep(3)
# Units of Measurement
million = 1000000
billion = 1000000000
trillion = 1000000000000

# Distances in Solar System [Measured in kilometers.]
dist_sun = 150 * million
dist_mars = 225 * million
dist_pluto = 5.89 * billion

# Distances Outside of Solar System [Measured in kilometers.]
light_year = 9460730000000 # Kilometers in a light year.  

dist_alpha_centauri = 4.3 * light_year
dist_eps_eridani_b = 10.44 * light_year
dist_v616_mon = 2800 * light_year

print("#------------------------------------------------------------------------#")
print("# Please select from the following objects:                              #")
print("#                                                                        #")
print("# [0] The Sun                                                            #")
print("# [1] Mars                                                               #")
print("# [2] Pluto                                                              #")
print("# [3] Alpha Centauri                                                     #")
print("# [4] Eps Eridani B                                                      #")
print("# [5] V616 Mon                                                           #")
print("#                                                                        #")
print("# Once you have made your selection this program will determine the      #")
print("# distance between the Earth and your chosen object.                     #")
print("#                                                                        #")
print("# To make your selection, type in the number from the list above, then   #")
print("# press the ENTER key.                                                   #")
print("#------------------------------------------------------------------------#")
object = int(input("Which object to do you want to select?"))
distance = 0
# if / else statement starts here.
if object == 0:
    distance = dist_sun 
    print("The distance to the Sun is",distance," kilometers.")
elif object == 1:
    distance = dist_mars
    print("The distance to Mars is",distance," kilometers.")
elif object == 2:
    distance = dist_pluto
    print("The distance to Pluto is",distance," kilometers.")
elif object == 3:
    distance = dist_alpha_centauri
    print("The distance to Alpha Centauri is",distance," kilometers.")
elif object == 4:
    distance = dist_eps_eridani_b
    print("The distance to the exoplanet Eps Eridani B is",distance," kilometers.")
elif object == 5:
    distance = dist_v616_mon
    print("The distance to blackhole V616 Mon is",distance," kilometers.")
else: 
    print("Error!  You did not enter a valid number from the menu.  Please restart the program.") 
    exit() 
time.sleep(3)

kachow = int(input("Kachow!  How fast will you travel?  Your speed is measured in Km / s.  You only need to enter the number, no commas!"))
speed_of_light = 299792

if kachow > speed_of_light:
    kachow = int(input("You cannot go faster than the speed of light!  Enter a number less than 299792."))
    if kachow > speed_of_light:
        print("Apparently you cannot read.  Please restart the program.")
        exit()
    else:
        print("Ok, thank you for entering a speed slower than light.")
else: 
    print("You entered",kachow,"Km / s for the speed.")
time.sleep(3)

distance = int(distance)
travel_time = distance / kachow
# print(travel_time)
seconds_in_year = 31536000
max_time = seconds_in_year * 3

if travel_time > max_time:
    print("Your speed is not high enough.  The trip will take longer than three years and will most likely fail.")
else:
    print("Your trip will take less than the maximum of three years.  Your trip should be successful.")

print("This program will exit in five seconds.")
time.sleep(5)
exit() 
# Extra Credit -- Print your actual trip time in number of days.


    



