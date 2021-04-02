#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:44:21 2021

@author: chelsea
"""

import argparse
import TuringPatternSim as TurPat

#simulate a turing pattern that was seeded with an image

parser = argparse.ArgumentParser(description='Simulate a Turing Pattern');
parser.add_argument('--Da', help='Diffusion coefficient of activator', type=float,required=True)
parser.add_argument('--Di', help='Diffussion coefficient of inhibitor', type=float, required=True)
parser.add_argument('--F', help='Feed value',required=True, type=float)
parser.add_argument('--K', help='Kill value',required=True, type=float)
parser.add_argument('--SeedPat', help='Name of the file that will be used to seed the pattern or "Random" or "Mid" to specify which function to seed it with', required=True)
parser.add_argument('--Ite', help='Iterations that the simulation will go through', required=True, type=int)
parser.add_argument('--Steps', help='Amount of iterations between images', required=True, type=int)
parser.add_argument('--FileName', help='File name for the outputted image', required=True)
parser.add_argument('--NumSeed', help='Number of seed if rand chosen ', required=False)
parser.add_argument('--Radius', help='Size of the seed if "Random" or "Mid" was choosen', required=False)


args = parser.parse_args()

if args.SeedPat == "Random":
    RandomSeed = TurPat.Simulator( float(args.Da), float(args.Di), 
                                 float(args.F), float(args.K))
    
    RandomSeed.seedRand(int(args.NumSeed), int(args.Radius))
    RandomSeed.SimulateOvertime(int(args.Ite), int(args.Steps), PathFile = str(args.FileName))   
elif args.SeedPat == "Mid":
    MidSeed = TurPat.Simulator( float(args.Da), float(args.Di), 
                                 float(args.F), float(args.K))
    MidSeed.seedMid(int(args.Radius))
    MidSeed.SimulateOvertime(int(args.Ite), int(args.Steps), PathFile = str(args.FileName))

    
else:
    
    PassingInSeed = TurPat.Simulator( float(args.Da), float(args.Di), 
                                     float(args.F), float(args.K), seed=str(args.SeedPat))
    PassingInSeed.SimulateOvertime(int(args.Ite), int(args.Steps), PathFile = str(args.FileName))
