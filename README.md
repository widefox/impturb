#Impulse turbine calculator
(C) Johnathon Weare 2016
Licence: GPL 3
Now in Python3 28 Sept 2016
Based on the original by Paul Roche, in Ruby 15 May 2016
Ported to Python, fixed

##Version
* 0.01 Ruby alpha-protoplasm, 15 May 16
* 0.1 Python, fixed result, 28 Sep 16

##Impulse turbine power output calculator

##Requirements
Python 2 or 3

##References
Based on the equation from (enter source here)
See http://www.ptb.de/cartoweb3/SISproject.php for more information vis fluctuating gravitational conditions
See also http://www.calpoly.edu/~gthorncr/ME302/documents/AccuracyofGravity.pdf

##Misc notes
First Principles - Pressure = Force/Area
* 1 Pascal (pressure) = 1 Newton of force per square meter
* 1 Bar = 100,000 Pascals
* 1 metric horsepower = 75kg of force per square meter = 735.5 Watts
* Power (/W) = torque (Nm) * angular velocity (/rad/s)
* P = T*2π*(N/60)
* where P = mechanical power /W; T = torque /Nm, and N = revolutions per minute
* rho = circa 1000 kg/m3 for fresh water (rho = density of working fluid kg/m3) and 1200kg/m3 for seawater
* Pi (π) = 3.1415926
* Gravity (g) = 9.8125 m/s2

#Issues
Based on inputting the jet force. More options such as water head should be given
