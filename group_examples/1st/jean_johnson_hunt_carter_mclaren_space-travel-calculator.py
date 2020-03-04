# Space Travel Calculator, Ryan Kelley, 02/28/20 4:02PM, Version 0.6
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
            February 28, 2020
            Version 0.6
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

distance = 0
time.sleep(5) 

if menu_choice == 0:
    distance = dist_sun
    print("You have selected the Sun.  It is",distance,"kilometers from Earth.")
elif menu_choice == 1:
    distance = dist_mars
    print("You have selected Mars.  It is",distance,"kilometers from Earth.")
elif menu_choice == 2:
    distance = dist_pluto
    print("You have selected Pluto.  It is",distance,"kilometers from Earth.")
elif menu_choice == 3:
    distance = dist_alpha_centauri
    print("You have selected Alpha Centauri.  It is",distance,"kilometers from Earth.")
elif menu_choice == 4:
    distance = dist_eps_eridani_b
    print("You have selected the exoplanet Eps Eridani B.  It is",distance,"kilometers from Earth.")
elif menu_choice == 5:
    distance = dist_v616_mon
    print("You have selected the blackhole V616 Mon.  It is",distance,"kilometers from Earth.")
else:
    print("Please choose an option from the menu above.  The program will now exit.")
    exit() 
time.sleep(5)     
speed = int(input("Please enter a speed in Km / s.   DO NOT use commas or units of measure."))

light_speed = 299792

if speed > light_speed:
    print("You cannot go faster than light speed: 299,792 Km / s.")
    speed = int(input("Please enter a speed in Km / s.   DO NOT use commas or units of measure."))
    if speed > light_speed:
        print("You are too stupid to use this program.  Please follow directions.  I will now exit.")
        exit()
    else:
        print("Your speed is ",speed,"Km / s.")
else:
        print("Your speed is ",speed,"Km / s.")
time.sleep(5) 
trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")

num_secs_year = 3.154e7
max_travel = 3 * num_secs_year

if trip_time > max_travel:
    print("The trip will take more than three years to complete.  It is not safe to go!")
else:
    print("The mission should be safe to complete.  It will take no more than three years.")

print("I hope you have enjoyed using the Space Travel Calculator.  Please be safe in space!")
time.sleep(5) 
exit() 

