# Brian Bock
# ENPM809T

# Import required packages
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dtime
import statistics

q2_path="Encoder_data_2.txt"
# FLpath="Encoder_data_3.txt"

# Import the data
q2_dataFile = open(q2_path,"r")
# FLdataFile = open(FLpath, "r")

q2_data=q2_dataFile.read().splitlines()

BRdata=[]
FLdata=[]
for data in q2_data:
	# print(data[0],data[1])
	BRdata.append(data[0])
	FLdata.append(data[1])


# Convert data from string to int to prevent funky plotting
BRint_list = list(map(int, BRdata))
FLint_list = list(map(int, FLdata)) 


# print(len(BRdata))
# print(int_list)
BRx=np.linspace(0,len(BRdata),len(BRdata))
FLx=np.linspace(0,len(FLdata),len(FLdata))


fig,axs=plt.subplots(2,1)

# Create a new figure
plt.sca(axs[0])
plt.plot(BRx,BRint_list,'.-')
plt.xlabel('Ticks')
plt.ylabel('Back Right Encoder')
plt.title("Encoder Ticks")

# Create a new figure
plt.sca(axs[1])
plt.plot(FLx,FLint_list,'r.-')
plt.xlabel('Ticks')
plt.ylabel('Front Left Encoder')


# plt.legend()
plt.show()






