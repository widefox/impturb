# impturb
Impulse turbine calculator
#!/usr/bin/env ruby
# Programmer: Paul Roche - PRELIM DESIGN. 
# Date: 15 May 2016

# Version: v.01 alpha-protoplasm - design 10.03 hours to 23.27 hours, 15 May 2016
# Programming Language: Ruby version 1.9.3p484 (2013-11-22 revision 43786)

# Working Title: Program to calculate impulse turbine power output
# 
# Design Notes for deletion when programme works: math direction...create relevant equations

# First Principles - Pressure = Force/Area
# 1 Pascal (pressure) = 1 newton of force per square meter
# 1 Bar = 100,000 Pascals
# 1 metric horsepower = 75kg of force per square meter = 735.5 Watts
# Power (mechanical power in Watts) = torque (n.m) * angular speed (in radians per second); equivalently use RPM which is simpler...
# for end users - divide by 60 for RPM
# P = T*2π*(N/60)
# where P = mechanical power in watts; T = torque in Newton Meters (n.m), and N = RPM (revolutions per minute)

# Readme [installation instructions for GUI and implementation of variables]

# List Constants
# 
# Gravity (g) = 9.8125 m/s/s at latitude 52°17′59″ N longitude 1°31′59″ W
# Gravity coordinates in decimal form: 52.299722 latitude; 1.533056 longitude
# See http://www.ptb.de/cartoweb3/SISproject.php for more information vis fluctuating gravitational conditions
# See also http://www.calpoly.edu/~gthorncr/ME302/documents/AccuracyofGravity.pdf

# rho = circa 1000 kg/m3 for fresh water (rho = density of working fluid in kg per cubic meter) and 1200kg/m3 for seawater
# Pi (π) = 3.14159265358979323846264338327950288419716939937510 (implement pi to 50 digits)
# g = gravity in Leamington Spa UK = 9.7803267714 * (1 + 0.00193185138639sin2λ/√1-0.00669437999013sin2λ)...
# ...where sin2 = sine squared; and where lambda (λ) = latitude. Note vis decimal latitude e.g., 52.3 for latitude 52° 18' 0")
# Allow users an automated (url) so they can calculate gravity for their actual locus using a latitude lambda value...
# accurate to as many dec places as possible
# 
#  
# List of Variables
# [[h = head in meters (i.e. distance travelled by working fluid before striking pitch circle diameter of impulse turbine) not needed here]]
# njet = number of jets
# fjet = jet force in Newtons
# nforce = proportion of force producing output torque (0.95 is normally a reasonable estimate)
# D = Pitch Circle Diameter of impulse turbine (meters)
# rpm = runner speed in revolutions per minute
# x = mechanical power in watts???
#
#
# 
#
# Pmech (watts) = Fjet x Njet x pi x h x w x d / 60


#Fjet = Force in Newtons

#Njet = number of jets eg 1 jet nozzle

#pi = 3.141592654 etc

#h = efficiency coefficient (unit-less fraction between 0 and 1) = eg 0.85 (always going to be a figure between 0.69 and 0.94...
# Larger they are, the more efficient

#d = diameter of turbine in metres (circle representing the pitch circle diameter of the turbine, that is, a circle the diameter of which represents the point where the working fluid noozle strikes the circular turbine which will not normally be the outermost edge of the turbine)

#w = rpm (i.e note the method of conversion from radians per second to rpm by dividing by 60) = eg for example 1200 rpm

#Accordingly, applying a Pmech equation example:

#170,000 (watts) = Fjet (10,006 Newtons) x Njet (1) x pi (3.141592654 etc) x h (0.85) x w (mystery value being rpm) x d (0.87m) / 60

#= 10,006 X 1 X Pi x 0.85 x RPM x 0.87 / 60
#= 23246 x w / 60
#170,000 = 23246w / 60
#170,000 = 387.4333w
#w = 438.78 RPM

# Have to subtract vb from vj per Mb = Ajet . (vj - vb) . pwater
# Why? Becuse runner speed may not exceed 50% of noozle jet velocity
# Why? See derivation infra
# x = optimal speed ratio as between runner (i.e. cup velocity) and vjet:
#x = vb / vj
#x = ratio
#vb = Cup velocity at pitch circle diameter of turbine
#vj = Jet velocity
#F = mb. vj . (1-x) (1+ z.cos g)
#h = mb . (vj . vj) . x . (1-x) . (1+z.cosg) / Â½ . mb (vj . vj)
#P = F . vb = mb . vj . (1-x) . (1+z.cos g) . vb  = mb . vj . x . (1-x) . (1+z.cos g)
#dh / dx = 2(1-2x). (1+z.cos g) = 0
#x = 0.5
 
 
#h = system efficiency as a unit-less fraction between zero and one
#F = force of water on cups (N)
#mb = mass flow rate into cup (kg/s)
#vj = Jet velocity (m/s)
#vb = runner tangential velocity at pitch circle diameter (m/s)
#z = efficiency factor for flow in buckets (unit-less fraction between zero and 1)
#g = angle of sides of cups
#x = speed ratio of vj to vb


#Maths - keep it as simple as a dimple wearing a wimple

#Water Jet Velocity (Vjet)

#Bernoulli equation gives velocity of water jet (v = vjet) applied to a turbine.

#P = Â½ r . V2

#P = Pressure (401,536 Pa)
#rho = density (1020kg/m3)
#V = velocity (m/s) mystery value

#401536 = Â½ 1020 . V2
#401536 = 510 . V2
#V2 = 401,536 / 510
#V = 28 m/s

#Force of water Jet (Fjet)

# 1 m3/s of seawater (1020kg/m3) represents a flow rate of 1020kg/s.
# 1000kg/m3 for freshwater is better but wtf.
# F = 1020kg/s x 28 m/s/s
# = 28560 Newtons...actually right though an enormous figure in that example

#Fjet Momentum Change Calculation

#Turbine speed may not exceed 50% of water jet speed. Hence...

#Vjet = 28 m/s
#Vrunner = 14 m/s

#Delta Mom = mass flow rate x Delta V
#Delta Mom = mass flow rate x (Vjet - Vrunner)
#Delta Mom = 1020kg/s x (28 m/s - 14 m/s)
#Delta Mom = 14280 N (for this example)

#Fjet = 14280N.

#Turbine RPM

# Can now calc the RPM figure for a turbine based on runner velocity
# of 14 m/s.

# First need circumference of turbine. For example:

# Diameter = 0.9m
# radius = 0.45m
# 2.pi.r = 2.827433388m (circumference)

# Vrunner = 14 m/s
# RPS = 4.951487 (revolutions per second) x 60
# = 297 RPM
# wtf

# Power Output
# Applying 297 RPM and Fjet = 14280 Newtons to Pmech equation:

# Pmech = Fjet x Njet x pi x flowrate x RPM x 0.9 x 0.87m / 60
# need to check all of this - why would you have flowrate and Fjet in the same equation...meh
# = 14280N x 1(jet) x pi x 1m3/s x 297RPM x 0.9(eff) x 0.87m / 60
# = 173Kw
# wtf
# Cross referencing this output figure with the conventional equation for electrical power output in watts:

# Pwatts = h(25m) x g(9.81 m/s/s) x rho (1020kg/m3) x 0.9 (eff) x 1m3/s (flow)
# = 225kW
# explanation for the different results? Flowrate of less than 1 m3/s is not needed and brings the figure down as lower value than 1.
#
#
#
#
#
#
#

# [need code to calc fjet before applying value to pmech equation and maths to calc fjet via bernoulli/pressure calcs]
# lots of work here and not mathematically accurate atm and would be nice to geolocate the gravity locus concept for accuracy
# linking to a url and grabbing gravity data for their locus (optional for users who want that sort of accuracy
# Inane fuckery required atm with existing web resources. Really needs to be simplified.
# And programming a discrete grav locus calculaton programme should be relatively trivial if already done for this programme


# Amother example continuing looking at the maths
# Bernoulli equation gives jet velocity.

# P = Â½ r . V2

# P = Pressure (Pa)
#rho = density (kg/m3)
#rho = density (kg/m3)
#V = velocity (m/s)
#V = velocity (m/s)
#P = 160 bar = 16,000,000 Pa = 16,000,000 N/m2
#rho fresh water = 1000 kg/m3
#The mystery value is velocity (m/s)
#16,000,000 = Â½ 1000 . V2
#V = 178.8854382 m/s

#Newton gives us Force (per mass x acceleration)
#F = m.a
#F = 0.16kg/s x 179 m/s
#F = 28.64 Newtons

#Note again (see supra) that Turbine at its most efficient when the runner travels at half jet speed ie here at 89.5 m/s
# very high rpm possible but not under load. Torque and rpm have essentiallty inverse relationship.  

#The Change in momentum of the jet (assuming water leaves cups with zero absolute tangential velocity) balances force applied to cup.

#Accordingly:
#Delta Mom = mass flow rate x Delta V
#Delta Mom = mass flow rate x (Vjet/Vrunner equation)
#Delta Mom = 0.16 x (179 - 89.5)
#Delta Mom = 14.3 N

# The x= 0.5 delta v speed limit again here


#Bernoulli's equation gives jet velocity.

#P = ½rho *v2

#Example of vjet calculation where pressure and density known
#P = Pressure (352,000 Pa)
#rho = density (1020kg/m3)
#V = velocity (m/s) mystery value
#352,000 = ½ 1020 . V2
#352,000 = 510 . V2
#V2 = 352,000 / 510
#V = 26.2 m/s
#Note that higher system pressure eg 450,000 Pa would give vjet (jet velocity) of 29.7 m/s.

#A mass flow rate of 1 m3/s (1020kg/s) provides the following Force figures in Newtons depending on velocity:

#F = 1020kg/s x 26.2 m/s/s
#= 26,724 Newtons - ludicrously high force figure but looks accurate due to huge mass flow rate (1 cubic meter per second of seawater)

#F = 1020kg/s x 29.7 m/s/s
#= 30,294 Newtons
# wtf
#Applying figures supra to Pmech equation for mechanical power output in watts (based on estimated RPM of say 100 RPM at Fjet values of 26724N and 30294N respectively

#Pmech = Fjet x Njet x pi x flowrate x RPM x 0.85 / 60
#= 26724N x 1 x pi x 1m3/s x 100 x 0.85  / 60
#= 118Kw

#= 30294N x 1 x pi x 1m3/s x 100 x 0.85  / 60
#= 134.8Kw
# why 'flowrate' here in the first of the two equations as you already have Fjet (force in newtons) and if...
# mass flow rate is already a fucking component of the force figure (having already been taken into account)...check
# ...homegrown equations against texts

#continuing...accordingly
#Delta Mom = mass flow rate x Delta V
#Delta Mom = mass flow rate x (Vjet - Vrunner)
#Delta Mom = 0.16 x (179 - 89.5)
#Delta Mom = 14.3 N


# ***************************
#Bernoulli's equation gives jet velocity vjet.

#P = ½rho *v2
# where P = pressure in Pascals, rho = density in kg/m3 and v = velocity in m/s

#If the pressure of working fluid is known, velocity when it strikes turbine may be calculated

#For example, if pressure, P = 352,000 Pa
#and rho or fluid density = 1020 kg/m3 (as is approx the case for seawater)
#velocity or v (m/s) is the only remaining mystery value, and may be calculated as follows:

#352,000 (P) = ½ 1020 * v2
#352,000 = 510 * v2
#v2 = 352,000 / 510
#v = 26.2 m/s

# velocity of the working fluid is now known (26.2m/s) from which Fjet may be provided once the flowrate in m3/s is known

# How calculate Flowrate?

# Force = mass x acceleration
# F = m.a
# F = 0.16kg/s x 26.2 m/s
# F = [] Newtons

#Note that impulse turbines are most efficient when the runner travels at half the jet speed
# so if jet speed (vjet) is 179m/s then optimal runner velocity (turbine pitch circle diameter speed) will be 89.5 m/s

#The Change in momentum of the jet (assuming the water jet leaves the cups with zero absolute tangential velocity) will balance the force applied to the cup.

#Accordingly:
#Delta Mom = mass flow rate x Delta v (where delta v is the difference)
#Delta Mom = mass flow rate x (Vjet - Vrunner)
#Delta Mom = 0.16 x (179 - 89.5)
#Delta Mom = 14.3 N
# enough theory and repetition
# Code conceptual framwork

print "Enter a value for njet (number of jets - normally 1 but could be 4 or even 6 for a major installation): "

first_num = gets.to_i

print "A value for nforce (unitless fraction for turbine efficiency) has been assigned at 0.85 though may be varied: "
print "see the readme file for more information about varying the nforce value"
print "A value 'd' for turbine pitch circle diameter in meters has been entered at 0.5m but can be varied: "
# we are going to have to sort out the floating point issue asap because non-integers are obviously essential
print "A value for fjet is calculated automatically based on rpm and other factors: "
print "Please enter a value for maximum rpm of the turbine under load: "

second_num = gets.to_i

print "Enter a value for flowrate of water in cubic meters per second: "

third_num = gets.to_i

puts first_num.to_s + " njet " + second_num.to_s + " rpm " + third_num.to_s + " x "
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
	print "Mechanical power output is "
	print pmech
	print " watts.  "
if pmech > 1000
 	print "The power output is therefore "
 	print pmech/1000
 	print " kilowatts "
 end

# problem with v.01? Lots of issues. x wa used for delta v calcs but is also being used to represent pmech! wtf
# and worse, x was also assigned to fucking flowrate which was probably not even needed as you had already had a Newton figure - meh
#
# The floating point problem sucks...leads to answers of 'infinity watts' when running it...second law violations always a bad sign
# meh
# ...if flowrate or indeed any other variable is less than 1...infinite kW error appears 
# Mathematically still a mess but not too far away from being useful speciality code.
# Ruby and sublime text IDE are nice
