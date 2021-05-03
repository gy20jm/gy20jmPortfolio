# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 07:45:38 2021

@author: Minty
"""
#import random module:
import random

#build Agent class:
class Agent:
       #create objects:
       def __init__(self, environment, y, x, agents):
           self.environment=environment
           self.store=0
           self.y=y
           self.x=x
           self.agents=agents
           #check this is working correctly:
           #print(x,y,agents)
           
      #create move function:
       def move(self):
           if random.random() < 0.5:
               self.y = (self.y + 1) % 100
           else:
               self.y = (self.y - 1) % 100
               
           if random.random() < 0.5:
               self.x = (self.x + 1) % 100
           else:
               self.x = (self.x - 1) % 100
        
       #create eat function:    
       def eat(self): 
          if self.environment[self.y][self.x] > 10:
                 self.environment[self.y][self.x] -= 10
                 self.store += 10
        
       #create share_with_neighbours function:
       def share_with_neighbours(self, neighbourhood):
           for agent in self.agents:
               distance=self.distance_between(agent)
               if distance <= neighbourhood:
                   sum=self.store+agent.store
                   average=sum/2
                   self.store=average
                   agent.store=average
                   #check that this is working correctly:
                   #print("sharing " + str(distance) + " " + str(average))
           
       #create distance_between function:           
       def distance_between (self, agent):
           return (((self.x-agent.x)**2)+((self.y-agent.y)**2))**0.5
       
           