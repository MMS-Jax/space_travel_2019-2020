# Space Travel Calculator, Ryan Kelley, 02/13/20 10:13AM, Version 0.65
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
            Version 0.65
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
print("# press the ENTER key.  There will be a pause before you make the choice.#")
print("#------------------------------------------------------------------------#")
time.sleep(3) 
distance = 0
menu_choice = int(input("Please make your selection."))

if menu_choice == 0:
    distance = dist_sun
    print("You have chosen the Sun.  It is ",distance,"kilometers from the Earth.")
elif menu_choice == 1:
    distance = dist_mars
    print("You have chosen Mars.  It is ",distance,"kilometers from the Earth.")
elif menu_choice == 2:
    distance = dist_pluto
    print("You have chosen Pluto.  It is ",distance,"kilometers from the Earth.")
elif menu_choice == 3:
    distance = dist_alpha_centauri
    print("You have chosen Alpha Centauri.  It is ",distance,"kilometers from the Earth.")
elif menu_choice == 4:
    distance = dist_eps_eridani_b
    print("You have chosen the exoplanet Eps Eridani B.  It is ",distance,"kilometers from the Earth.")
elif menu_choice == 5:
    distance = dist_v616_mon
    print("You have chosen the blackhole V616 Mon.  It is ",distance,"kilometers from the Earth.")
else:
    print("You did not make a choice from the menu.  Please select an option from the list next time.  The program will now restart.")
    exit()    
time.sleep(3)

speed = 0
speed = int(input("Please enter a speed.  Your speed is measured in Km / s.  DO NOT ENTER COMMAS.  Press [Enter] when finished."))
            
light_speed = 299792

if speed > light_speed: # 1st check for speed of light. 
    print("You have entered a value greater than the speed of light: 299792 Km / s.  That is not possible.")
    speed = int(input("Please enter a speed LESS THAN OR EQUAL TO the speed of light."))
    if speed > light_speed: # 2nd check for speed of light.  
        print("It is obvious you cannot read.  Please restart the program and try again.")
        exit()
    else:
        print("Ok, your speed is acceptable.  You will be traveling at ",speed,"Km /s.")
else:
        print("Ok, your speed is acceptable.  You will be traveling at ",speed,"Km /s.")       
    





