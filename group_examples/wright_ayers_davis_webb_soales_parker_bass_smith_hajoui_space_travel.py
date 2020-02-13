# Space Travel Calculator, Ryan Kelley, 02/13/20 1:22PM, Version 0.7
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
            Version 0.7
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

choice = int(input("Please make a choice."))
time.sleep(3)
distance = 0

if choice == 0:
    print("You have chosen the Sun.")
    distance = dist_sun 
    print("The distance to the Sun is",distance,"kilometers.")
elif choice == 1:
    print("You have chosen Mars.")
    distance = dist_mars 
    print("The distance to Mars is",distance,"kilometers.")
elif choice == 2:
    print("You have chosen Pluto.")
    distance = dist_pluto
    print("The distance to Pluto is",distance,"kilometers.")
elif choice == 3:
    print("You have chosen the Alpha Centauri.")
    distance = dist_alpha_centauri 
    print("The distance to Alpha Centauri",distance,"kilometers.")
elif choice == 4:
    print("You have chosen the exoplanet Eps Eridani B.")
    distance = dist_eps_eridani_b 
    print("The distance to the exoplanet Eps Eridani B is",distance,"kilometers.")
elif choice == 5:
    print("You have chosen the blackhole V616 Mon.")
    distance = dist_v616_mon 
    print("The distance to the blackhole V616 Mon",distance,"kilometers.")
else:
    print("Error!  You did not choose a valid number from the menu!  This program will now explode.  Please restart.")
    exit() 
time.sleep(3)
speed = 0
speed = int(input("Please enter your speed in Km / s.  Please DO NOT enter commas or Km / s, just the number then press [ENTER]."))

light_speed = 299792

if speed > light_speed:
    speed = int(input("You CANNOT exceed the speed of light: 299,792 Km / s.  Please re-type your speed and press [ENTER]."))
    if speed > light_speed:
        print("You are stupid and cannot read.  I will now exit.  Please restart the program.")
        exit()
    else:
        print("Ok, your speed is",speed,"Km / s.")
else:
    print("Ok, your speed is",speed,"Km / s.")
time.sleep(3)

trip_time = distance / speed
print("The trip will take ",trip_time,"seconds to complete.")

seconds_per_year = 31536000
max_travel = seconds_per_year * 3

if trip_time > max_travel:
    print("The trip will take more than three years.  It will not succeed.  Please choose a different location.")
else:
    print("The trip will take three years or less.  It will succeed!  Good luck on the trip!")


print("I will now exit in five seconds.")
time.sleep(5)
exit() 









        

