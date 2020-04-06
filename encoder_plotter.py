# Brian Bock
# ENPM809T
# In Class 4/6 - Encoder Plotter

# Import required packages
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dtime
import statistics

filepath="4-6data.txt"

# Import the data
dataFile = open(filepath,"r")

data=dataFile.read().splitlines()

int_list = list(map(int, data)) 


print(len(data))
print(int_list)
x=np.linspace(0,len(data),len(data))


# Create a new figure
plt.figure()
# Create a list of frames (1-len(data))
plt.plot(x,int_list,'.-')
plt.xlabel('Ticks')
plt.ylabel('Voltage High/Low')
plt.title("Encoder Ticks")

#plt.legend()
plt.show()






