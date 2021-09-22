import matplotlib.pyplot as plt
from graphics import *
import  collections
import numpy as np
from numpy import linalg as LA
from math import sqrt
import numpy as np

file = open("Coordinates.txt","w")
f = open ('Matrix.txt', 'r')
D = []
D = [ line.split() for line in f]
for i in range (0,32):
    for j in range (0,32):
        D[i][j]=float(D[i][j])

plt.title("Square Numbers", fontsize=19)
plt.xlabel("Number", fontsize=10)
plt.ylabel("Square of Number", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=9)



P1=Point(0,0)


plt.scatter(P1.x, P1.y, s=500)
plt.text(P1.x, P1.y,1,fontsize=9)
file.write("P1")
file.write(":%s" %P1)
file.write("\n")

P2=Point(P1.x+D[0][1],0)

plt.scatter(P2.x, P2.y, s=500)
plt.text(P2.x, P2.y,2,fontsize=9)
file.write("P2")
file.write(":%s" %P2)
file.write("\n")
P3=Point((D[0][1]*D[0][1]-D[1][2]*D[1][2]+D[0][2]*D[0][2])/(2*D[0][1]),sqrt(D[1][2]*D[1][2]-(P2.x-(D[0][1]*D[0][1]-D[1][2]*D[1][2]+D[0][2]*D[0][2])/(2*D[0][1]))*(P2.x-(D[0][1]*D[0][1]-D[1][2]*D[1][2]+D[0][2]*D[0][2])/(2*D[0][1])))-P2.y)

plt.scatter(P3.x, P3.y, s=500)
plt.text(P3.x, P3.y,3,fontsize=9)
file.write("P3")
file.write(":%s" %P3)
file.write("\n")

k=4
for i in range(3,32):
    P4=Point((D[1][i]*D[1][i]-D[0][i]*D[0][i]-P2.x*P2.x)/((-2)*P2.x),sqrt((D[0][i]*D[0][i]-((D[1][i]*D[1][i]-D[0][i]*D[0][i]-P2.x*P2.x)/((-2)*P2.x))*((D[1][i]*D[1][i]-D[0][i]*D[0][i]-P2.x*P2.x)/((-2)*P2.x)))))
    DistanceP1=sqrt(P4.x * P4.x + P4.y * P4.y)
    DistanceP2=sqrt((P4.x - P2.x) * (P4.x - P2.x) + (P4.y - P2.y) * (P4.y - P2.y))
    DistanceP3=sqrt((P4.x - P3.x) * (P4.x - P3.x) + (P4.y - P3.y) * (P4.y - P3.y))
    if(DistanceP1 + 0, 1 >= D[0][i] and DistanceP1 - 0, 1 >= D[0][i] and DistanceP2 + 0, 1 >= D[1][i] and DistanceP2 - 0, 1 >= D[1][i] and DistanceP3 + 0, 1 >= D[2][i] and DistanceP3 - 0, 1 >= D[2][i]):
        plt.scatter(P4.x, P4.y, s=500)
        plt.text(P4.x, P4.y,k,fontsize=9)
        file.write("P%s" %str(k))
        file.write(":%s" %P4)
        file.write("\n")
        k+=1
    else:
        file.write("The point was miscalculated")


plt.show()
