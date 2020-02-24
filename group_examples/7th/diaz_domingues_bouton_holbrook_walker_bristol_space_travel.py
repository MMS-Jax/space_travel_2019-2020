# Space Travel Calculator, Ryan Kelley, 02/24/20 3:44PM, Version 1.0
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
            February 24, 2020
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

menu_choice = int(input("What is your choice?"))
# print(menu_choice)

distance = 0

if menu_choice == 0:
    distance = dist_sun
    print("You have selected the Sun.  It is ",distance," kilometers from the Earth.")
elif menu_choice == 1:
    distance = dist_mars
    print("You have selected Mars.  It is ",distance," kilometers from the Earth.")
elif menu_choice == 2:
    distance = dist_pluto
    print("You have selected Pluto.  It is ",distance," kilometers from the Earth.")
elif menu_choice == 3:
    distance = dist_alpha_centauri
    print("You have selected Alpha Centauri.  It is ",distance," kilometers from the Earth.")
elif menu_choice == 4:
    distance = dist_eps_eridani_b
    print("You have selected the exoplanet Eps Eridani B.  It is ",distance," kilometers from the Earth.")
elif menu_choice == 5:
    distance = dist_v616_mon
    print("You have selected the blackhole V616 Mon.  It is ",distance," kilometers from the Earth.")
else:
    print("You did not select an option from the menu.  Please restart the program.")
    exit()
time.sleep(5)  
  
speed = int(input("Please enter your speed in Km / s.  DO NOT enter Km / s or commas, just a number.")) 
            
light_speed = 299792 

if speed > light_speed:
    print("You cannot go faster than light speed: 299,792 Km / s.")
    speed = int(input("Please enter your speed in Km / s.  DO NOT enter Km / s or commas, just a number."))
    if speed > light_speed:
        print("You are stupid and cannot read.  Please restart the program after fixing your eyes.")
        exit()
    else:
        print("The speed is acceptable.  You are traveling at ",speed,"Km / s.")
else:
    print("The speed is acceptable.  You are traveling at ",speed,"Km / s.")


trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")
time.sleep(5)
seconds_per_year = 3.154e7
max_time = seconds_per_year * 3

if trip_time > max_time:
    print("Your trip will exceed three years.  You will die alone in space.  Have a nice day!")
else:
    print("The trip will take three years or less.  It should succeed.  Good luck!")

print("I hope you have enjoyed using the Space Travel Calculator.  Enjoy exploring the universe!")
time.sleep(5)
exit()


