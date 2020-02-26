# Space Travel Calculator, Ryan Kelley, 02/26/20 1:37pm, Version 0.8999999999
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
            February 26, 2020
            Version 0.899999999999999
""")
print("This Space Travel Calculator determines if an outerspace mission will take more or less than three years.")
user_name = input("What is your name? [Please type your name and press ENTER.]  ")
print("Hello, how are you?  It is nice to meet you", user_name,"!")

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

menu_choice = int(input("Please make your choice."))
print(menu_choice)

distance = 0

if menu_choice == 0:
    print("You have chosen the Sun.")
    distance = dist_sun
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 1:
    print("You have chosen Mars.")
    distance = dist_mars
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 2:
    print("You have chosen Pluto.")
    distance = dist_mars
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 3:
    print("You have chosen Alpha Centauri.")
    distance = dist_alpha_centauri
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 4:
    print("You have chosen the exoplanet Eps Eridani B.")
    distance = dist_eps_eridani_b
    print("It is",distance,"kilometers from the Earth.")
elif menu_choice == 5:
    print("You have chosen the blackhole V616 Mon.")
    distance = dist_v616_mon
    print("It is",distance,"kilometers from the Earth.")
else:
    print("You did NOT choose an option from the menu.  This program will now exit.  Please restart.")
    exit() 
    
speed = int(input("Please enter your speed in Km / s.  DO NOT type commas or units, just the number."))

light_speed = 299792

if speed > light_speed:
    print("You cannot go faster than light speed: 299,792 Km /  s.")
    speed = int(input("Please enter your speed in Km / s.  DO NOT type commas or units, just the number."))
    if speed > light_speed:
        print("You are stupid.  Please learn to read and follow directions.  Good bye!")
        exit()
    else:
        print("The speed you entered was",speed," Km / s.  Good luck!")
else:
        print("The speed you entered was",speed," Km / s.  Good luck!")        
        
trip_time = distance / speed
print("The trip will take",trip_time,"seconds to complete.")


