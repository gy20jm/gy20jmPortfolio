# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:51:59 2021

@author: Minty
"""

#import all required modules:
import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation

#set up variables:
num_of_agents=5
num_of_iterations=5
neighbourhood=20

#create empty lists for agents, rowlist and environment:
agents=[]
rowlist=[]
environment=[]

#size of animation pop-up window:
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

#import environment csv file:
f=open ('in.txt') 
reader=csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
        environment.append(rowlist)
        for value in row:
            rowlist.append(value)
f.close()
            
#plot the environment data:
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.axis([0,99,0,99])
matplotlib.pyplot.show()

#make the agents:
for i in range(num_of_agents):
   agents.append(agentframework.Agent(environment, random.randint(0,99), random.randint(0,99),agents))
       
carry_on=True

#animation loop:
def update(frame_number):
    fig.clear()
    global carry_on
   
#call the agents:
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
#create stopping condition. If random number is less than 0.1, then animation stops.        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition met")
    
#plot the agents:
    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    
'''       
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a			
        a = a + 1
'''
#distance between agents:
def distance_between(agents_row_a, agents_row_b):
   return (((agents_row_a.x- agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5
             
for agents_row_a in agents:
    for agents_row_b in agents:
       distance = distance_between(agents_row_a, agents_row_b)
       #show that this is working:
       #print(distance)
 
animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.5, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()




