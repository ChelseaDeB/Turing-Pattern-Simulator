#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:44:25 2021

@author: chelsea
"""

import TuringPatternSim as TurPat


'''Creating a Simulator object '''
SpecifyDimensions = TurPat.Simulator( 1, 0.5, 0.03, 0.055, 50,250)

'''
1 is the diffusion coefficient of the activor  Da
0.5 is the diffusion coefficient of the inhibitor Di

Da is always bigger than the Di, by Turing's model

0.03 is the feed rate, amount of activor being put into the system by an 
outside source. Note, activator could create more activator, but feed refers to 
an outside (other means) of supplying activator 

0.055 is the kill rate, therefore how fast the activator is being broken down

50 is the width of the image.

250 is the height of the image.

'''

NoDimensions = TurPat.Simulator( 1, 0.5, 0.03, 0.055) 
#by default will produce an image 250 by 250 
                                                    
'''Creating an image and passing it a seed'''
PassingInSeed = TurPat.Simulator( 1, 0.5, 0.014, 0.053, seed="fig.png")
#Will create an image with the seeding pattern of fig.png

'''Display the plot to the screen'''
PassingInSeed.DisplayPattern()
 


'''How to create a simulator then seed it will a random pattern'''
RandomSeed = TurPat.Simulator( 1, 0.5, 0.03, 0.055)
RandomSeed.seedRand(60, 10)
#filling the graph with 60 squares randomly placed, and each square is 20 by 20

'''How to seed the middle of the simulator'''
MidSeed = TurPat.Simulator( 1, 0.5, 0.03, 0.055)
MidSeed.seedMid(30) #seeds the middle with a square that 60 by 60


'''Produce a single image'''
RandomSeed.Simulate(350) #will update the graph 350 using the Gray Scott equation

RandomSeed.DisplayPattern(filename= "Tutorial_Simulate500Iterations.png") 
#will save the output in the file  Simulate500Iterations.png

#Could have passed Tutorial/Simulate500Iterations.png then the file 
#Simulate500Iterations.png would be saved in the folder Tutorial


'''Produce a time lapse '''
PassingInSeed.SimulateOvertime(500, 50) 
#Will simulate for a total of 500 iterations, and produce an image every 50 iterations
#Graph will display at 0,50,100,150, 200, 250, 300, 350, 400, 450 and 500 iterations

PassingInSeed.SimulateOvertime(500, 50, PathFile = "Tutorial_SimuateOvertime") 
#will save the images as files name  
#Tutorial_SimuateOvertime__Iteration_0.png   Tutorial_SimuateOvertime__Iteration_50.png ...

#You could have passed Tutorial/SimuateOvertime and it would have
#saveed the results in a folder name Tutorial with each imaged named
#SimuateOvertime__Iteration_0.png   SimuateOvertime__Iteration_50.png 



