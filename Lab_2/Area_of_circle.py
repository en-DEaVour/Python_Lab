# Name:- MOHD MUSTAJAB KHAN
# Roll no:- 33
# En. no:- A180570

import math
print(" For Area of circle")
while 1 :
    try:
        Radius_of_circle = input("Enter the value of Radius-:")
        Radius_of_circle = float(Radius_of_circle)
        Area_of_circle = math.pi *( Radius_of_circle * Radius_of_circle )
        print (" Area of circle is-:", Area_of_circle)
        break;
    except ValueError:
        print(" Enter the value of Radius in Numeric ")
        continue
