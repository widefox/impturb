#!/usr/bin/env python2
# coding: utf-8
# Programmer: Johnathon Weare
# Date: 15 May 2016
# Based on the original:
# Programmer: Paul Roche - PRELIM DESIGN. 
# Date: 15 May 2016

# Version: v.01 alpha-protoplasm - design 10.03 hours to 23.27 hours, 15 May 2016

first_num = input("Enter a value for njet (number of jets - normally 1 but could be 4 or even 6 for a major installation): ")

print ("A value for nforce (unitless fraction for turbine efficiency) has been assigned at 0.85 though may be varied: ")
print ("see the readme file for more information about varying the nforce value")
print ("A value 'd' for turbine pitch circle diameter in meters has been entered at 0.5m but can be varied: ")
# we are going to have to sort out the floating point issue asap because non-integers are obviously essential
print ("A value for fjet is calculated automatically based on rpm and other factors: ")
second_num = input("Please enter a value for maximum rpm of the turbine under load: ")

third_num = input("Enter a value for flowrate of water in cubic meters per second: ")

print (first_num, " njet ", second_num, " rpm ", third_num, " x ")
#(first_num + second_num).to_s
# x = flowrate in cubic meters per second
nforce = 0.85
pi = 3.14159265358979323846264338327950288419716939937510
njet = first_num
d = 0.5
rpm = second_num
flowrate = 0.5
x = third_num

fjet = nforce * pi * d * njet * rpm / x * 60

# Pmech = fjet * njet * pi * flowrate * rpm * 0.85 / 60
pmech = nforce * pi * njet * d * rpm * fjet / 60
print ("Mechanical power output is ", pmech, "W")
#if pmech > 1000:
print ("The power output is therefore ", pmech/1000, "kW")
