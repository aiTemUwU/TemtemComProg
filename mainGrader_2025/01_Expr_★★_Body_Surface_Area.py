import math

weight = float(input())
height = float(input())

Mosterller = ((weight*height)**(1/2))/60
Haycock = 0.024265*(weight**0.5378)*(height**0.3964)
Boyd = 0.0333*(weight**(0.6157-0.0188*(math.log(weight, 10))))*(height**0.3)
               
print(Mosterller)
print(Haycock)
print(Boyd)