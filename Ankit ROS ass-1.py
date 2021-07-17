#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""Week I Assignment by Ankit Kumar
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50

Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n:int):
        for i in range(n):
            self.theta += w *(self.dt)
            self.x += v*np.cos(self.theta)
            self.y += v*np.sin(self.theta)
            self.x_points.append(self.x)
            self.y_points.append(self.y)

        return self.x, self.y, self.theta

    def plot(self, v: float, w: float,i:int):

        plt.title(f"Unicycle Model: {v}, {w}")
        plt.title(f" Ankit's ROS ass-1 graphs - {i}")
        plt.xlabel("x-Coordinates")
        plt.ylabel("y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()


if __name__ == "__main__":
    print("Unicycle Model Assignment")

    # ploting multiple trajectories
    trajec = [
        {'x':0,'y': 0,'theta': 0,'dt': 0.1, 'v':1,'w': 0.5,'step': 25},
        {'x':0,'y': 0,'theta': 1.57,'dt' :0.2,'v': 0.5, 'w':1,'step':  10},
        {'x':0,'y': 0,'theta': 0.77, 'dt':0.05, 'v': 5,'w': 4, 'step': 50}
                   ]
    for i in range(len(trajec)):
        x = trajec[i]['x']
        y = trajec[i]['y']
        theta = trajec[i]['theta']
        dt = trajec[i]['dt']
        v = trajec[i]['v']
        w = trajec[i]['w']
        n = trajec[i]['step']
        project=Unicycle(x, y, theta, dt)
        cordinates = project.step(v, w, n)
        x, y, theta = cordinates
        project.plot(v, w, i+1)
       
