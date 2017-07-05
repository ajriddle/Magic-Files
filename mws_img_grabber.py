import os
from urllib import urlretrieve
from numpy import *

#Change to appropriate pics directory
os.chdir('../HOU/') 
#Read in file containing card names
cards = genfromtxt('HOU_names.txt',dtype=str,delimiter=';') 
for name in cards:
    name = name.replace("/","") #remove slashes
    loc = name.replace("'","") #remove apostraphes
    loc = loc.replace("-","") #remove hyphens
    loc = loc.replace(",","") #remove commas
    loc = loc.replace(" ","") #remove spaces
    loc = loc.lower() #Make lower case
    #Assign set abreviation for url, e.g. change 'hou' to 'akh' for Amonkhet
    set_abrev = 'hou'
    url = 'http://mythicspoiler.com/'+set_abrev+'/cards/'+loc+'.jpg'
    #Save image jpegs using MWS '.full' convemtion
    urlretrieve(url,name+'.full.jpg')
    