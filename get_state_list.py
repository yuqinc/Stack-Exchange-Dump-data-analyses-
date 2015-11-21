#!/Users/yuqincai/Library/Enthought/Canopy_64bit/User/bin/python
# Author:Yuqin Cai
#get the USA locations of users, plot according to states

import re
import os
import sys, getopt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

#STEP1 get the location
text_file=open("../data/location.out","a")
with open("../data/Users.xml") as f:
    for line in f:
        result =re.search('Location=(.+?)AboutMe=',line) # grep all contents between strings
        if result:
            found =result.group(1)
            text_file.write("%s\n" %found.replace('\"','')) #get rid of double quotes
text_file.close()
#this location output file will be used for both USA and world programmer geographic distribution analyses

#STEP2 check if it is a USA state 
states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
#text_file=open("../data/usa_location.out","a")
states_count=list()
with open("../data/location.out") as f:
    for line in f:
        #if any(s in line for s in states):
        for state in states:
            if state in line: 
                print state
                print line
                #text_file.write('{0}'.format(line)) 
                states_count.append(state)

#STEP3 sort the list 
states_count.sort()
##sorted(states)
##count frequency of each elements in a list 
freq=[len(list(group)) for key, group in groupby(states_count)]
len(freq)

#STEP4 dataframe for analysis
data=zip(states,freq)
#dataframe a tuple
df = pd.DataFrame(data, columns=['state','user_numbers'])

#output dataframes to a file for Choropleths 
df.to_csv('usa_programmer_counts.out', sep='\t')

#STEP5, plot results
fig=plt.figure()
ax =fig.add_subplot(111)
fig.subplots_adjust(bottom=0.15)
x=df.state
y=df.user_numbers
index =np.arange(51)
bar_width= 0.35
plt.bar(index,y,bar_width,color='orange')
plt.xlim(0,52)
plt.xticks(index + bar_width, x.tolist(),rotation=0,fontsize= 8, weight='bold')
plt.ylabel('States',fontsize= 14, weight='bold')
plt.ylabel('Programmer numbers',fontsize= 14, weight='bold')
plt.title("geographic distribution of stackoverflow programmers",fontsize= 14, weight='bold')
plt.show()