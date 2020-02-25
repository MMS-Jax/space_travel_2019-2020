# Space Travel Calculator, Ryan Kelley, 02/25/20 1:36PM, Version 1.0
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
            February 25, 2020
            Version 1.0
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

save_option = int(input("Please make your choice."))
# print(save_option)

distance = 0

if save_option == 0:
    distance = dist_sun
    print("You have selected The Sun.  It is ",distance,"kilometers from the Earth.")
elif save_option == 1:
    distance = dist_mars
    print("You have selected Mars.  It is ",distance,"kilometers from the Earth.")
elif save_option == 2:
    distance = dist_pluto
    print("You have selected Pluto.  It is ",distance,"kilometers from the Earth.")
elif save_option == 3:
    distance = dist_alpha_centauri
    print("You have selected Alpha Centauri.  It is ",distance,"kilometers from the Earth.")
elif save_option == 4:
    distance = dist_eps_eridani_b
    print("You have selected the exoplanet Eps Eridani B.  It is ",distance,"kilometers from the Earth.")
elif save_option == 5:
    distance = dist_v616_mon
    print("You have selected the blackhole V616 Mon.  It is ",distance,"kilometers from the Earth.")
else:
    print("Please choose an option from the menu.  The program will now stop and restart.")
    exit() 

speed = int(input("Please enter your speed in Km / s.  Type ONLY numbers, no symbols."))
print(speed)

light_speed = 299792

if speed > light_speed:
    print("You have entered a speed faster than light: 299,792 Km / s.  Please re-enter speed.")
    speed = int(input("Please enter your speed in Km / s.  Type ONLY numbers, no symbols."))
    if speed > light_speed:
        print("You are dumb and cannot read.  Please restart the program, loser.")
        exit()
    else:
        print("The speed you entered was",speed,"Km / s.")
else:
    print("The speed you entered was",speed,"Km / s.")

trip_time = distance / speed 
    
seconds_per_year = 3.154e7
max_time = seconds_per_year * 3

if trip_time > max_time:
    print("The trip will be longer than three years.  It is not safe and you might die in space.")
else:
    print("The trip is less than or equal to three years in length.  It is safe and should succeed.")

print("Thank you for using the Space Travel Calculator.  Have fun exploring outer space!")
exit()

    
