#Impulse turbine calculator
Programmer: Paul Roche - PRELIM DESIGN. 
Originally in Ruby
Date: 15 May 2016
Ported to Python3 and cleaned up
Programmer: Johnathon Weare
Now in Python3 26 Sept 2016

#Version: v.01 alpha-protoplasm - design 10.03 hours to 23.27 hours, 15 May 2016
Programming Language: Ruby version 1.9.3p484 (2013-11-22 revision 43786)

##Working Title: Program to calculate impulse turbine power output

##Design Notes for deletion when programme works: math direction...create relevant equations

##First Principles - Pressure = Force/Area
1 Pascal (pressure) = 1 newton of force per square meter
1 Bar = 100,000 Pascals
1 metric horsepower = 75kg of force per square meter = 735.5 Watts
Power (mechanical power in Watts) = torque (n.m) * angular speed (in radians per second); equivalently use RPM which is simpler...
for end users - divide by 60 for RPM
P = T*2π*(N/60)
where P = mechanical power in watts; T = torque in Newton Meters (n.m), and N = RPM (revolutions per minute)

Readme [installation instructions for GUI and implementation of variables]

##List Constants

Gravity (g) = 9.8125 m/s/s at latitude 52°17′59″ N longitude 1°31′59″ W
Gravity coordinates in decimal form: 52.299722 latitude; 1.533056 longitude
See http://www.ptb.de/cartoweb3/SISproject.php for more information vis fluctuating gravitational conditions
See also http://www.calpoly.edu/~gthorncr/ME302/documents/AccuracyofGravity.pdf

rho = circa 1000 kg/m3 for fresh water (rho = density of working fluid in kg per cubic meter) and 1200kg/m3 for seawater
Pi (π) = 3.14159265358979323846264338327950288419716939937510 (implement pi to 50 digits)
g = gravity in Leamington Spa UK = 9.7803267714 * (1 + 0.00193185138639sin2λ/√1-0.00669437999013sin2λ)...
...where sin2 = sine squared; and where lambda (λ) = latitude. Note vis decimal latitude e.g., 52.3 for latitude 52° 18' 0")
Allow users an automated (url) so they can calculate gravity for their actual locus using a latitude lambda value...
accurate to as many dec places as possible

 
#Issues
problem with v.01? Lots of issues. x wa used for delta v calcs but is also being used to represent pmech! wtf
and worse, x was also assigned to fucking flowrate which was probably not even needed as you had already had a Newton figure - meh

The floating point problem sucks...leads to answers of 'infinity watts' when running it...second law violations always a bad sign
meh
...if flowrate or indeed any other variable is less than 1...infinite kW error appears 
Mathematically still a mess but not too far away from being useful speciality code.
