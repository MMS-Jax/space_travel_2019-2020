# Space Travel Calculator, Ryan Kelley, 02/13/20 4:03PM, Version 1.0
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
            February 13, 2020
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

choice = int(input("Please make your choice."))
time.sleep(5)
distance = 0 

if choice == 0:
    distance = dist_sun
    print("You have selected the Sun.  It is ",distance,"kilometers from Earth.")
elif choice == 1:
    distance = dist_mars
    print("You have selected Mars.  It is ",distance,"kilometers from Earth.")
elif choice == 2:
    distance = dist_pluto
    print("You have selected Pluto.  It is ",distance,"kilometers from Earth.")
elif choice == 3:
    distance = dist_alpha_centauri 
    print("You have selected Alpha Centauri.  It is ",distance,"kilometers from Earth.")
elif choice == 4:
    distance = dist_eps_eridani_b
    print("You have selected the exoplanet Eps Eridani B.  It is ",distance,"kilometers from Earth.")
elif choice == 5:
    distance = dist_v616_mon
    print("You have selected the blackhole V616 Mon.  It is ",distance,"kilometers from Earth.")
else:
    print("Please choose a value from the menu!  This program will now explode.  Please restart.")
    exit()
    
speed = 0
time.sleep(5)
speed = int(input("Please enter a speed in Km / s.  You do not need to enter commas or the unit of measurement, just a number."))

light_speed = 299792

if speed > light_speed: 
    speed = int(input("Please enter a speed less than 299,792 Km / s. You cannot exceed the speed of light."))
    if speed > light_speed:
        print("You are stupid and cannot read.  Please restart the program.  I will now exit..loser.")
        exit()
    else:
        print("Ok, your speed is ",speed,"Km / s.  Let's move on!")
else: 
    print("Ok, your speed is ",speed,"Km / s.  Let's move on!")

trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")
time.sleep(5)
seconds_per_year = 3.154e7
max_time = seconds_per_year * 3

if trip_time > max_time:
    print("The trip will take more than three years.  The mission will not succeed.  Please choose a different location.")
else:
    print("The trip will not exceed three years, it will succeed.  Safe travels and good luck!")

print("I hope you have enjoyed using this program. I will now exit.  Have a nice day!")
time.sleep(5)
exit() 
    

    
    
