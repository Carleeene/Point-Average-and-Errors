#2 Point Moving Average for Forecasting

#Import ceil from the math library
from math import ceil

#Indicate the total period of the Operations
#Per variable as the Period
Per = int(input('Total Period of the Operations: '))

#Input the Actual value during a period
#Av variable as Actual value
def Actual():
    actual_values = []
    for i in range(Per):
        actual_values.append(int(input(f'Type your Actual Value here each period {1+i}: ')))
    return actual_values

Av = Actual()

#Calculating the 2 Point Moving Average for Forecasting 
#Fv variable as Forecasting Value
Fv = {}

for i in range(2,Per+1):
    Fv[i+1] = ceil((Av[i-2] + Av[i-1])/2)
print(Fv)
