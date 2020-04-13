
import numpy as np
import matplotlib.pyplot as plt
import math




def ticks2dist(ticks):
	motor_rotations_per_meter=587.649
	ticks_per_wh_rev=20
	wheel_radius=.0325 #m
	ticks_per_meter=ticks_per_wh_rev/(2*math.pi*wheel_radius)# ticks/meter
	dist=ticks/ticks_per_meter
	print(dist)
	return dist # meters

def deadReckonPlot(start_pos, ticks, ax):

	startx=start_pos[0]
	starty=start_pos[1]
	theta=np.deg2rad(start_pos[2])

	# Assume ticks were counted while moving

	# convert ticks to distance
	dist=ticks2dist(ticks)


	new_pos=[0,0,0]

	new_pos[0]=startx+dist*math.cos(theta)
	new_pos[1]=starty+dist*math.sin(theta)
	new_pos[2]=np.rad2deg(theta)

	# plot line from start_pos to end_pos
	x=np.linspace(startx,new_pos[0],500)
	y=np.linspace(starty,new_pos[1],500)
	# line=(start_pos[:2],new_pos)

	# print(start_pos[:2],new_pos[:2])
	# print(new_pos)

	ax.plot(x,y,'-')
	return new_pos




if __name__ == "__main__":
	x=0
	y=0
	theta=45
	start_pos=(x,y,theta)

	ticks=100
	

	fig,ax=plt.subplots()

	new_pos=deadReckonPlot(start_pos,ticks,ax)
	new_pos[2]=90
	new_pos=deadReckonPlot(new_pos,ticks,ax)
	new_pos[2]=180
	new_pos=deadReckonPlot(new_pos,ticks,ax)

	plt.xlabel('X Position (m)')
	plt.ylabel('Y Position (m)')
	plt.title("Where we've been")
	plt.show()
