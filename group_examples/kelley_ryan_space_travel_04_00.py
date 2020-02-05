# Space Travel Calculator, Ryan Kelley, 01/21/20 1:29PM, Version 0.45
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
                Version 0.45
              January 23, 2020

""")
print("Greetings, I am the NASA Space Travel Calculator. I will help you calculate travel times to different places in space.") 
name = input("How are you!  What is your name? [Type your name and press ENTER.]")
print("Good afternoon," + name)

# Millions and Billions 
million = 1000000 # Six 0's
billion = 1000000000 # Nine 0's 
trillion = 1000000000000 # Twelve 0's 


# Distances for Objects in our Solar System [Measured in kilometers.] 
distance_mars = 225 * million  
distance_pluto = 5.9 * billion 
distance_saturn = 1.4 * billion 

print("The distance to Mars is",distance_mars,"kilometers.")
print("The distance to Saturn is",distance_saturn,"kilometers.")
print("The distance to Pluto is",distance_pluto,"kilometers.")

# Distances for Objects Outside of the Solar System [Measured in kilometers.] 
light_year = 9.4607e+12 # Kilometers 
distance_alpha_centauri = 4.22 * light_year 
print("The distance to Alpha Centauri is",distance_alpha_centauri,"kilometers.")
distance_cygnusX3 = 11000 * light_year 
print("The distance to the blackhole at Cygnus X-3 is",distance_cygnusX3,"kilometers.")
distance_neutron_star = 625 * light_year 
print("The distance to the closest neutron star is",distance_neutron_star,"kilometers.")