print("Medieval focus daytrajectory calculator \nMD '23")

def grading_stem_comp ():
  Distance = []

  for i in range (3):
    Distance.append (float(input("Enter how far projectile landed from target for each of the three test you will conduct (you will be promted three times)")))
  return tuple(Distance)
  
import math

# Declaring the value of gravity 
gravity = 9.81

# Declaring the values of angle, velocity, height and the distances to zero
angle = 0
velocity = 0
height = 0
Distance1 =0
Distance2 =0
Distance3 =0
# The formula i used requires that the height, angle and velocity values are greater than zero
# The program will continue asking for the required value if the one provided is equal zero

while angle <= 0:
  angle = int(input("Enter a release angle (greater than zero) : "))

while velocity <= 0:
  velocity = int(input("Enter the release velocity (greater than zero) : "))

while height <= 0:
  height = int(input("Enter the release height (greater than zero) : "))


# Calculating the Range or projectile distance value using formula shown in https://youtu.be/UkLZKxxTFaA 
# I needed to include the function of math.radians to convert degrees to radians, because thats what is accepted in Python.
distance = ( velocity*math.cos(math.radians(angle)) * ( velocity*math.sin(math.radians(angle)) + math.sqrt(velocity*math.sin(math.radians(angle)))**2 ) + 2*gravity*height ) / gravity

# Converting the distance from meters to feet and rounding the final number.
print ( " To ensure a direct hit move your catapult:", round(distance*3.281), "ft away from your target") 

# students now test their catapult- against a target using the trajectory calculator to hone in on there targets after each test input the distance the projectile landed from there target to get a pass fail grade

results=grading_stem_comp()
g=results[0]
h=results[1]
f=results[2]

sum= g+h+f/3
print (sum," ft")

if sum < 4:
 print ("You passed")

else:
  print ("You failed")


# reference important sites that I used 

# https://docs.python.org/3/library/ https://youtu.be/UkLZKxxTFaA 
#https://www.omnicalculator.com/physics/projectile-motion#:~:targetText=Write%20down%20the%20equations%20of%20motion.&targetText=Horizontal%20distance%20traveled%20can%20be,g%20is%20the%20gravity%20acceleration.
#https://www.tutorialspoint.com/python3/python_lists.htm
#https://youtu.be/UkLZKxxTFaA

