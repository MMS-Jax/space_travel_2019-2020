# Space Travel Calculator, Ryan Kelley, 02/19/20 3:12PM, Version 0.8
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
            February 19, 2020
            Version 0.8
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

choice = 0
choice = int(input("What is your choice?"))
time.sleep(3)
# print(choice)

distance = 0 

if choice == 0:
    distance = dist_sun
    print("You selected 0.  You are traveling to the Sun.  It is ",distance,"kilometers from Earth.")
elif choice == 1:
    distance = dist_mars
    print("You selected 0.  You are traveling to Mars.  It is ",distance,"kilometers from Earth.")
elif choice == 2:
    distance = dist_pluto
    print("You selected 0.  You are traveling to Pluto.  It is ",distance,"kilometers from Earth.")
elif choice == 3:
    distance = dist_alpha_centauri
    print("You selected 0.  You are traveling to Alpha Centauri.  It is ",distance,"kilometers from Earth.")
elif choice == 4:
    distance = dist_eps_eridani_b
    print("You selected 0.  You are traveling to the exoplanet Eps Eridani B.  It is ",distance,"kilometers from Earth.")
elif choice == 5:
    distance = dist_v616_mon
    print("You selected 0.  You are traveling to the blackhole V616 Mon.  It is ",distance,"kilometers from Earth.")
else:
    print("You must choose a number from the menu!  Please restart the program.")
    exit() 

speed = int(input("Please enter your speed in Km / s.  Do not enter COMMAS or UNITS, just a number."))        

light_speed = 299792

if speed > light_speed:
    print("You cannot go faster than light speed which is 299,792 Km / s.  Please enter a new speed.")
    speed = int(input("Please enter your speed in Km / s.  Do not enter COMMAS or UNITS, just a number."))
    if speed > light_speed:
        print("You are too stupid to read instructions.  Please restart the program.")
        exit()
    else:
        print("Your speed is OK.  You will travel at ",speed,"Km / s.") 
else:
    print("Your speed is OK.  You will travel at ",speed,"Km / s.")

trip_time = distance / speed
print("The trip will take", trip_time,"seconds to complete.")
time.sleep(3)
seconds_per_year = 3.154e7
max_time = seconds_per_year * 3

if trip_time > max_time:
    print("The trip will take more than three years.  You will probably die a horrible death in space, alone.")
else:
    print("The will take no more than three years.  The trip will be successful.")
time.sleep(3)

print("I hope you have enjoyed using the Space Travel Calculator.  Good luck exploring the Universe!")
time.sleep(3)
exit() 


