#!/usr/bin/env python3
# (C) 2016 Johnathon Weare
# Licence: GPL3
# Date: 28 September 2016
# Based on the original by Paul Roche 15 May 2016
"""Impulse turbine calculator"""
import math
def imppower():
    """calc power"""
    njet = float(input("Number of jets (normally 1, sometimes 4-6): "))
    fjet = float(input("Force of jet /N: "))
    # print ("see the readme file for more information about varying the etaforce value")
    # diameter is the pitch circle diameter /m
    diameter = float(input("Pitch circle diameter /m "))
    # density of working liquid /kg/m3
    # liqdensity=1000
    # print ("Liquid density: ", liqdensity)
    # a made up example pressure from one's head (for example 4x atmospheric)
    # pressureinonesshead=401536
    # print ("Pressure (to be clarified) /Pa: ", pressureinonesshead)
    rpm = float(input("rpm of the turbine under load: "))
    #flowrate = input("Enter a value for flowrate of water /m3/s: ")
    # unitless fraction for turbine efficiency
    etaforce = float(input("Efficiency (typically 0.85): "))

    pmech = fjet * njet * math.pi * rpm / 60.0 * etaforce * diameter
    print("Power output= " + str(pmech) + " W")
    print("Power output= " + str(pmech/1000.0) + " kW ")
    print("Power output= " + str(pmech/1000000.0) + " MW")

imppower()
