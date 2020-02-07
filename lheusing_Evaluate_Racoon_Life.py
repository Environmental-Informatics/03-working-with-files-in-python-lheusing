#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:43:47 2020

@author : Logan Heusinger
Assignment 3- import txt file and create a seperate txt file and meta data file

Objectives
- read/write/open text files
- manipulate lists, dictionaries, and tuples
- create text and accompaning metadata file

"""
listdist = [] 
fin = open( "2008Male00006.txt", 'r' ) # open input file
lines = fin.readlines() # read all lines in file
fin.close() # close the file
Data = [0]*len(lines) # create a list of 0s of equal size to the file that was read

for lidx in range(len(lines)):
    Data[lidx] = lines[lidx].split(",") #strip the lines 
    
headers = Data[0] #collect headers data
Data.remove(headers)
lifestate = Data[14] #store weather dead or alive
lifestate = str(lifestate[0])
Data.remove(Data[14]) #remove as it messes with row counting
headers.remove('Year') #Remove headers titles that are not needed
headers.remove('Risk')
headers.remove('MVL')
headers.remove('PercptionDist')
headers.remove('MSL')
headers.pop(9) #remove steps and last as .remove wasnt working
headers.pop(8)

Day = [str(row[1]) for row in Data] #create lists from the data and name them
Time = [str(row[2]) for row in Data] # in addition change their type to approp 
George = [int(row[3]) for row in Data]
X = [float(row[4]) for row in Data]
Y = [float(row[5]) for row in Data]
Asleep = [str(row[6]) for row in Data]
Behave = [str(row[7]) for row in Data]
Energy = [float(row[8]) for row in Data]

tdata = list(zip(*Data)) #change row and colum - not used later but kept
lifedic = dict(zip(headers,[Day,Time,George,X,Y,Asleep,Behave,Energy])) #create dictionary with header

def meanval(lists): #calculate average of any above list
    mean = sum(lists)/len(lists)
    return mean
def cumsum(lists): #calculate cumulative sum of any above list
    csum = sum(lists)
    return csum
def dist(X,Y): #calculate the idstance between two points and set the first distance point to 0  as no movement can be made
    for i in range(len(X)):
        if i == 0 :
            Distance = 0
            listdist.append(Distance) #add to the list
        else :
            Distance =  ((((X[i]-X[i-1])** 2)  + ((Y[i]-Y[i-1])**2)) ** 0.5)
            listdist.append(Distance) #add to the list

dist(X,Y) #compute distance
distancedic = ( {'Distance':listdist}) #change list to dict and add title
lifedic.update(distancedic) #add distance to the final dictionary

averageenergy = meanval(Energy) #calculate various means and sums
averageX = meanval(X)
averageY = meanval(Y)
totaldistance = cumsum(listdist)


ffile = open("lheusing_Georges_life.txt",'w') #creates new txt file and writes it
ffile.write(("Racoon name:{}{}\n").format(headers[2],George[0])) #header block
ffile.write(("Average location: {},{}\n").format(averageX,averageY))
ffile.write(("Distance traveled: {}\n").format(totaldistance))
ffile.write(("Average energy level: {}\n").format(averageenergy))
ffile.write(("Racoon end state: {}\n\n").format(lifestate))
ffile.write(("Date               Time                 X                        Y               Asleep     Behavior mode       Distance traveled  \n"   ))
for i in range(len(lifedic)): #adds dictionary data and places in colums sepearted by tabs
    ffile.write('%s \t %s \t %s \t %f \t %s \t %s \t %f\n' % (lifedic['Day'][i], lifedic['Time'][i], lifedic[' X'][i], lifedic[' Y'][i], lifedic[' Asleep'][i], lifedic['Behavior Mode'][i], lifedic['Distance'][i] )) 
ffile.close()