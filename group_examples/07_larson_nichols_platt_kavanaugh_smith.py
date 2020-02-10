# Space Travel Calculator, Ryan Kelley, 02/10/20 3:42PM, Version 1.0
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
object = int(input("What object do you want?"))
time.sleep(3)
#print(object)

distance = 0

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
    print("The distance to the blackhole V616 Mon is",distance," kilometers.")
else:
    print("Error!  You did not choose an option from the menu.")
    exit()
time.sleep(3)
speed = int(input("Please enter the speed in Km/s.  You do not need to enter commas or Km/s, just the number."))
print(speed)

light_speed = 299792
light_speed = int(light_speed)

if speed > light_speed:
    speed = int(input("Do not enter a speed greater than 299792 Km/s.  Please re-enter your speed."))
    if speed > light_speed:
        print("You obviously cannot read and follow directions.  Please restart the program.")
        exit()
    else:
        print("Ok, you entered",speed,"Km / s.")  
else:
        print("Ok, you entered",speed,"Km / s.")
time.sleep(3)
speed = int(speed)
trip_time = distance / speed
print("The time in seconds for the trip is:",trip_time,".")
# Extra Credit -- Figure out and print the trip time in days.  
seconds_per_year = 3.154e7
max_trip = seconds_per_year * 3

if trip_time > max_trip:
    print("Your trip time will exceed three years.  The mission will most likely be unsucessful.")
else:
    print("Your trip time is less than or equal to three years.  The mission will most likely be successful.")

    




