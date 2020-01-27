# Space Travel Calculator, Ryan Kelley, 01/24/20 2:26PM, Version 0.45
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
            January 24, 2020
            Version 0.45
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

print("The distance to the Sun is",dist_sun," kilometers.")
print("The distance to Mars is",dist_mars," kilometers.")
print("The distance to Pluto is",dist_pluto," kilometers.")

# Distances Outside of Solar System [Measured in kilometers.]
light_year = 9460730000000 # Kilometers in a light year.  

dist_alpha_centauri = 4.3 * light_year
dist_eps_eridani_b = 10.44 * light_year
dist_v616_mon = 2800 * light_year

print("The distance to Alpha Centauri is",dist_alpha_centauri," kilometers.")
print("The distance to the exoplanet Eps Eridani B is",dist_eps_eridani_b," kilometers.")
print("The distance to the nearest blackholeis",dist_v616_mon," kilometers.")
