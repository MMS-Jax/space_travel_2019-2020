# Space Travel Calculator, Ryan Kelley, 03/05/20 3:13PM, Version 1.0
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
            March 05, 2020
            Version 1.0
""")
print("This Space Travel Calculator determines if an outerspace mission will take more or less than three years.")
user_name = input("What is your name? [Please type your name and press ENTER.]  ")
print("Hello, how are you?  It is nice to meet you", user_name,"!")
time.sleep(5) 
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

menu_selection = int(input("What is your choice?"))
# print(menu_selection)

distance = 0
time.sleep(5)
if menu_selection == 0:
    distance = dist_sun
    print("You have chosen the Sun.  It is",distance,"kilometers from the Earth.")
elif menu_selection == 1:
    distance = dist_mars
    print("You have chosen Mars.  It is",distance,"kilometers from the Earth.")
elif menu_selection == 2:
    distance = dist_pluto
    print("You have chosen Pluto.  It is",distance,"kilometers from the Earth.")
elif menu_selection == 3:
    distance = dist_alpha_centauri
    print("You have chosen Alpha Centauri.  It is",distance,"kilometers from the Earth.")
elif menu_selection == 4:
    distance = dist_eps_eridani_b
    print("You have chosen the exoplanet Eps Eridani B.  It is",distance,"kilometers from the Earth.")
elif menu_selection == 5:
    distance = dist_v616_mon
    print("You have chosen the blackhole V616 Mon.  It is",distance,"kilometers from the Earth.")
else:
    print("Please make sure to choose an option from the menu.  The program will now exit.")
    exit()

speed = int(input("Please enter a speed in Km / s.  DO NOT enter commas or units of measure."))

light_speed = 299792
time.sleep(5)
if speed > light_speed:
    print("You cannot go faster than light: 299,792 Km / s.")
    speed = int(input("Please enter a speed in Km / s.  DO NOT enter commas or units of measure."))
    if speed > light_speed:
        print("You are stupid.  I don't think you can read.  This program will now exit.")
        time.sleep(5)
        exit()
    else:
        print("You have entered an acceptable speed.  You will travel at",speed,"Km / s.")
else:
        print("You have entered an acceptable speed.  You will travel at",speed,"Km / s.")        

trip_time = distance / speed
print("This trip will take",trip_time,"seconds to complete.")
time.sleep(5)

seconds_per_year = 3.154e7
max_trip = seconds_per_year * 3

if trip_time > max_trip:
    print("The trip will take too long.  It is not safe to embark on that journey.")
else:
    print("The trip will take no more than three years.  Be safe in space!  Great success!")

print("Thank you for using the Space Travel Calculator.  Live long and prosper!")
time.sleep(5)
exit() 
    
