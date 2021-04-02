#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:39:12 2021

@author: chelsea
"""

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''


input: 


    Da: diffusion coefficient of the activator 
    Db: diffusion coefficient of the inhibitor 
    
    feed: the amount of activator being put into the system
    
    kill: kill rate
   
    X: is the hieght of our matrices, default 400
        must be an integer 
    Y: is the height, Da diffusion coefficient of the activator, default 400
        must be an integer
    lap_constants: the values for the convolution, 
        default: np.array([[0.05, 0.2, 0.05], [0.2, -1, 0.2], [0.05, 0.2, 0.05]])
        must be a 2D array 
restrictions:
    
    - Da,Db,feed,kill are between 0 and 1 i.e. over the interval [0,1]  
    - kill > feed
    
    e.g Da : 05. 
    
    
'''
    
class Simulator:
    def __init__(self, Da, Db, feed, kill, width = 250, height = 250,
                 
                 lap_constants = np.array([[0.05, 0.2, 0.05]
                                           , [0.2, -1, 0.2], 
                                           [0.05, 0.2, 0.05]]), seed = ''):
        
        #gray scot they filled with A everywhere and B no where. i.e. only activator
        self.Da = Da
        self.Db = Db
        self.feed = feed
        self.kill = kill
        self.lp_kernel = lap_constants
        
        if seed:
            
            seedPat = mpimg.imread(seed)
            self.height = seedPat.shape[0]
            self.width = seedPat.shape[1]
            self.grid_A = np.zeros((self.height, self.width)) #activtor
            self.grid_B = np.zeros((self.height, self.width)) #inhibitor, follows seeding 
            for x in range(self.height):
                for y in range(self.width):
                    self.grid_A[x,y] = 1 - (sum(seedPat[x,y]) / len(seedPat[x,y]))
                    self.grid_B[x,y] = 1 - (sum(seedPat[x,y]) / (2*len(seedPat[x,y])))
        else:
        
            self.grid_A = np.zeros((height, width)) #activtor
            self.grid_B = np.zeros((height, width)) #inhibitor, follows seeding 
            self.height = height
            self.width = width
        
        return

    def laplace(self):
        
        La = ndimage.convolve(self.grid_A, self.lp_kernel, mode="reflect", cval=0)
        Lb = ndimage.convolve(self.grid_B, self.lp_kernel, mode="reflect", cval=0)
        return La,Lb
    
    
    ''' 
    This function will feed the middle of a graph with activator.
    
    Input:
        r:  fills in a 2r by 2r square with activator in the middle of the graph
            
    '''
    
    def seedMid(self, r):
        self.grid_A[self.height//2-r:self.height//2+r,self.width//2-r:self.width//2+r] = 0.50
        self.grid_B[self.height//2-r:self.height//2+r,self.width//2-r:self.width//2+r] = 0.25
        return 
    
   
    
    '''
   This function will fill the grid with random bunches of activator.
   
   Input:
       num_seeds: pass it the nmber of bunches you want
       r: the size of each square, squares dimensions are 2r by 2r
   
   '''
    
    def seedRand(self, num_seeds, r ):
        
        '''generate an array with num_seed random integers between 0 and X'''
        x_cords= np.random.randint(self.height, size = (num_seeds))
        '''generate an array with num_seed random integers between 0 and X'''
        y_cords= np.random.randint(self.width, size = (num_seeds))
        #print( x_cords, y_cords)
        
        for i in range(num_seeds):
            self.grid_A[x_cords[i]-r:x_cords[i]+r,y_cords[i]-r:y_cords[i]+r] = 0.50
            self.grid_B[x_cords[i]-r:x_cords[i]+r,y_cords[i]-r:y_cords[i]+r] = 0.25
        return
        
        
    '''Updates the graph to what it would look like in the next time step'''
    def updateGrayScott(self):
        a = self.grid_A 
        b = self.grid_B
        La, Lb = self.laplace()
        #self.grid_A =
        self.grid_A =  a + (self.Da * La - a *b *b + self.feed *(1-a))
        self.grid_B = b + (self.Db * Lb + a *b *b - (self.kill + self.feed) * b)
        #print(self.grid_B)
        return 
    
    def DisplayPattern(self, CMAP = "Greys", filename = ''):
        plt.figure() # creating figure
        plt.axis('off')
        plt.rcParams["savefig.bbox"] = "tight"
        plt.imshow(self.grid_B, cmap = CMAP) 
        
        
        if filename:
            plt.savefig(filename)
            
        
        return 
        
    '''  
    Simulates the graph for a certain number of times that you specify
    
    Input:
            iterations: amount of updates you want for the system
            
    '''
    def Simulate(self, iterations):
        for _ in range(iterations):
            self.updateGrayScott()
        return
    
    def SimulateOvertime(self, maxIT, Step, PathFile=""):
        IterationsDone=0
        if PathFile =="":
            self.DisplayPattern()
            for Iteration in range(Step,maxIT +Step, Step):
                IterationsDone = Iteration
                self.Simulate(Step)
                self.DisplayPattern()
            
        
        
        else:
            self.DisplayPattern(filename =PathFile + "_Iteration_"+str(IterationsDone)+".png")
            for Iteration in range(Step,maxIT +Step, Step):
                IterationsDone = Iteration
                self.Simulate(Step)
                self.DisplayPattern(filename = PathFile + "_Iteration_"+str(IterationsDone)+".png")
                plt.close("all")
        return
