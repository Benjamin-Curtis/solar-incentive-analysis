#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:36:31 2025

@author: benjamincurtis
"""

#import pandas as pd
import pandas as pd

#set maximum number of rows to print to none
pd.set_option('display.max_rows', None)

#create df called solar
solar=pd.read_csv('res_solar_by_county.csv')

#set index to County
solar=solar.set_index('County')

#print coloumns of df
print('\nColumns:', list(solar.columns))

#find count of projects
count=solar['projects']

#print count
print('\nNumber of projects:', count)

#create list for Onondaga, Oswego, and Wayne
some_cny_counties= ['Onondaga','Oswego','Wayne']

#print the count in each county
print('Number of projects in Central New York')
print(count[some_cny_counties])

#print the projects in Albany
print('Number of projects in Albany')
print(count['Albany'])

#sort the values in count from high to low
high_to_low=count.sort_values(ascending=False)
print(high_to_low)

#Locate the top five counties
top_five=high_to_low.iloc[0:5]
print('The Top Five Solar Panel Counties')
print(top_five)

#Dive the columns of solar by the number of projects in corresponding county
means=solar.div(count, axis='index')
print ('Means by County')
print(means)

#compare the means for all counties to Onodaga
onodaga_row=means.loc['Onondaga']
relative=means/onodaga_row
relative=round(relative, 2)
rel_incentive=relative['total_incentive']
print('Onondga Incentive Relative to New York Counties')
print(rel_incentive.sort_values())



