# Space Travel Calculator, Ryan Kelley, 01/27/20 9:10AM, Version 0.5
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
            January 27, 2020
            Version 0.5
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




# print("The distance to Alpha Centauri is",dist_alpha_centauri," kilometers.")
# print("The distance to the exoplanet Eps Eridani B is",dist_eps_eridani_b," kilometers.")
# print("The distance to the nearest blackhole is",dist_v616_mon," kilometers.")
