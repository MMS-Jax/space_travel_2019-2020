# Space Travel Calculator, Ryan Kelley, 02/13/20 12:19PM, Version 0.7
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

choice = int(input("What choice do you want?"))
time.sleep(3)
distance = 0

if choice == 0:
    distance = dist_sun
    print("You have chosen the Sun.  It is is",distance,"kilometers from the Earth.")
elif choice == 1:
    distance = dist_mars
    print("You have chosen Mars.  It is is",distance,"kilometers from the Earth.")
elif choice == 2:
    distance = dist_pluto
    print("You have chosen Pluto.  It is is",distance,"kilometers from the Earth.")
elif choice == 3:
    distance = dist_alpha_centauri
    print("You have chosen Alpha Centauri.  It is is",distance,"kilometers from the Earth.")
elif choice == 4:
    distance = dist_eps_eridani_b
    print("You have chosen the exoplanet Eps Eridani B.  It is is",distance,"kilometers from the Earth.")
elif choice == 5:
    distance = dist_v616_mon
    print("You have chosen the blackhole V616 Mon.  It is is",distance,"kilometers from the Earth.")
else:
    print("You did not choose a number from the menu.  This program will now exlpode.  Please restart.")
    exit() 
time.sleep(3)
speed = 0
light_speed = 299792

speed = int(input("Please enter your speed in Km / s.  Do not enter commas, just the number.  Do not exceed the speed of light: 299,792 Km / s."))

if speed > light_speed:
    print("You entered a speed greater than the speed of light!  That is impossible!")
    speed = int(input("Please enter your speed in Km / s.  Do not enter commas, just the number.  Do not exceed the speed of light: 299,792 Km / s."))
    if speed > light_speed:
        print("It is obvious you cannot read and follow directions.  This program will now exit.")
        exit()
    else:
        print("Ok, that speed is fine.  You entered",speed," Km / s for your speed.") 
else:
        print("Ok, that speed is fine.  You entered",speed," Km / s for your speed.") 
time.sleep(3)

trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")
print("I need to calculate how many years that will take...")
time.sleep(3) 

seconds_per_year = 31556952
max_time = seconds_per_year * 3

if trip_time > max_time:
    print("The trip will take more than three years.  The mission will fail.")
else:
    print("The trip will take three years or less.  The mission will succeed.")
time.sleep(3)

print("I hope you have enjoyed using this program.  Good luck exploring outer space!")
print("I will exit in 5 seconds.")
time.sleep(5)
exit() 





