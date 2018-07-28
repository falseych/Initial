
#This python scrip is to test the precision of numpy


import numpy as np
pi=3.14              #The rough value of PI
#r=6378               #The radius of the Earth
r=float(raw_input("Please input the radius.\n"))
c1=2*pi*r            #The rough value of circumference using the tough PI
c2=2*np.pi*r        #The precise value of circumference using numpy
unit="km"            #The unit of radius and circumference

#print the result
print "The circumference calculated with %f is \t%f(%s)\nThe circumference calculated with numpy is \t%f(%s)"%(pi,c1,unit,c2,unit)
