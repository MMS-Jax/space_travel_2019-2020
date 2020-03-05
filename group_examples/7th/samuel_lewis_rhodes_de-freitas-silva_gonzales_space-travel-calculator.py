# Space Travel Calculator, Ryan Kelley, 03/05/20 3:51PM, Version 1.0
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

menu_choice = int(input("What number do you want?"))
# print(menu_choice)
time.sleep(5)
if menu_choice == 0:
    distance = dist_sun
    print("You have selected the Sun.")
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 1:
    distance = dist_mars
    print("You have selected Mars.")
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 2:
    distance = dist_pluto
    print("You have selected Pluto.")
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 3:
    distance = dist_alpha_centauri
    print("You have selected Alpha Centauri.")
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 4:
    distance = dist_eps_eridani_b
    print("You have selected the exoplanet Eps Eridani B.")
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 5:
    distance = dist_v616_mon
    print("You have selected the blackhole V616 Mon.")
    print("It is",distance,"kilometers from the Earth.")
else:
    print("You did not make a choice from the menu.  The program will now exit.  Please restart it.")

speed = int(input("Please enter a speed in Km / s.  Do not enter commas or units of measure."))  

light_speed = 299792

if speed > light_speed:
    print("You cannot exceed light speed: 299,792 Km / s.")
    speed = int(input("Please enter a speed in Km / s.  Do not enter commas or units of measure."))
    if speed > light_speed:
        print("I think you are stupid.  You cannot follow directions.  The program will now exit.")
        exit()
    else:
        print("Your speed is",speed,"Km / s.")
else:
        print("Your speed is",speed,"Km / s.")       
time.sleep(5)
trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")

num_secs_per_year = 3.1543e7
max_trip = num_secs_per_year * 3

if trip_time > max_trip:
    print("The trip will take too long.  It is not safe to start the trip.")
else:
    print("The trip will take no more than three years.  Great success!")

print("Thank you for using the Space Travel Calculator.")
time.sleep(5)
exit() 
    
