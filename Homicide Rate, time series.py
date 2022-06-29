# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:26:54 2021

@author: Roelo
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

data={"Countries":["Chile","Argentina","Colombia","Venezuela","Uruguay","Peru",
                   "Bolivia","Brazil","Paraguay","Ecuador","Suriname","Guyana"],
      "Population":[18729160,44361150,49661048,28887118,3449285,31989260,11353142,
                    209469323,6956066,17084358,575990,779006],
      "2000":[3.20,8.56,66.97,33.16,6.45,3.2,5.80,23.80,18.96,14.45,14.44,10.18],
      "2001":[3.15,8.39,69.16,32.30,6.56,3.0,6.70,24.82,24.21,12.82,16.58,10.74],
      "2002":[3.20,9.47,69.45,38.31,6.95,2.7,5.80,25.39,24.80,14.50,11.82,19.20],
      "2003":[3.24,7.79,56.70,44.39,5.93,2.9,5.15,25.76,22.81,14.49,12.30,28.05],
      "2004":[3.30,6.07,48.03,37.39,6.02,3.12,5.20,24.12,21.10,17.58,9.32,17.57],
      "2005":[3.56,5.65,42.47,37.70,5.72,2.88,5.18,23.45,15.23,15.34,13.81,19.03],
      "2006":[3.61,5.37,40.46,45.65,6.07,2.76,5.13,23.96,12.55,16.96,12.27,20.50],
      "2007":[3.37,5.39,39.32,48.28,5.82,3.11,8.06,23.47,13.05,15.90,8.80,15.41],
      "2008":[3.52,5.92,36.47,52.79,6.62,4.32,8.52,23.89,13.70,17.94,8.32,21.16],
      "2009":[3.73,6.53,35.35,49.89,6.75,5.24,8.29,22.96,13.32,17.77,7.5,15.65],
      "2010":[3.17,5.83,34.18,45.99,6.10,5.52,12.67,22.11,11.86,17.47,7.48,18.68],
      "2011":[3.69,6.08,35.32,48.40,5.91,5.53,12.10,24.34,10.37,15.38,6.50,17.29],
      "2012":[2.49,6.34,35.68,54.74,7.90,6.67,11.77,26.62,10.11,12.43,6.30,18.40],
      "2013":[3.16,7.28,33.16,62.82,7.67,6.76,8.84,26.94,9.28,10.98,5.30,20.41],
      "2014":[2.47,7.57,28.41,63.34,7.88,6.90,8.80,28.85,8.76,8.22,5.78,19.52],
      "2015":[3.39,6.59,26.90,52.04,8.59,7.37,6.17,28.59,9.22,6.49,6.08,19.42],
      "2016":[3.36,6.03,25.74,59.56,7.83,7.87,6.22,29.88,9.87,5.84,7.26,18.41],
      "2017":[4.22,5.21,25.02,89.1,8.26,7.91,6.18,30.83,7.88,5.79,5.43,14.83],
      "2018":[2.7,5.32,25.34,81.4,12.06,9.16,6.42,27.38,7.14,5.80,5.22,14.25],
      "2019":[2.6,5.08,25.4,60.3,9.8,8.54,6.32,26.70,7.02,5.48,5.01,14.11]}

df=pd.DataFrame.from_dict(data)

                                    # Edit the DataFrame

#Remove unnecessary columns
df.drop(["Population"],axis=1,inplace=True)
#Calculate the mean of each row from 2000-2019
average=df.mean(axis=1)
print(average)
#Add a new column
Year_2020=[3.25,6.52,39.97,51.87,7.24,5.27,7.46,25.69,13.56,12.58,8.77,17.64]
df["Year_2020"]=Year_2020
#Rename a column
df.rename(columns={"Year_2020":"2020"},inplace=True)

#Drop Column Countries to perform annual percentage change 2000-2020
df.drop(["Countries"],axis=1,inplace=True)
#Find annual Percentage change/New dataframe of percentage change
percent=df.pct_change(periods=1,axis=1)
#Find Average percentage change
Average_percent=percent.mean(axis=1)

#Add new column representing Average percent change from 2000-2020
Average_Percent_Change=[0.018678,-0.006370,-0.016647,0.035707, 0.017385, 0.037088,
                        0.030764,0.005149, 0.004883,0.024599,0.001334,0.057675]
df["Average_Percent_Change"]=Average_Percent_Change
#Rename Average_Percent_Change column
df.rename(columns={"Average_Percent_Change":"Average Percent Change"},inplace=True)

#Add Countries to the dataframe as Column again
Countries=["Chile","Argentina","Colombia","Venezuela","Uruguay","Peru",
           "Bolivia","Brazil","Paraguay","Ecuador","Suriname","Guyana"]
df["Countries"]=Countries



                                # Create the Area Plot

#Put the Countries column as the index
df.set_index("Countries",inplace=True)
#Iterate through the years in a list range, transpose the dataframe
years=list(map(str,range(2000,2020)))
df_transpose=df[years].transpose()

#Style Sheets for the plot
print(plt.style.available)
mpl.style.use(["Solarize_Light2"])

#Plot the Area Plot
df_transpose.plot(kind="area",stacked="False",figsize=(12,7))
plt.title("Homicide rate from 2000-2020, per 100,000 ppl")
plt.xlabel("Years",fontsize=10)
plt.ylabel("Homicide Rate",fontsize=10)
plt.legend(fontsize=8)
plt.show()

            # GeoPandas - Create Choropleth map- Average homicide rate of last..

import geopandas as gpd
#Load the built-in world dataset
world_data=gpd.datasets.get_path("naturalearth_lowres")
world=gpd.read_file(world_data)

#Want to merge our two datasets/df + world from geopandas library
Table=world.merge(df,how="left",left_on=["name"],right_on=["Countries"])
Table2=Table.dropna(subset=["2000","2001"])

import folium
my_map=folium.Map()
folium.Choropleth(geo_data=Table2,name="choropleth",columns=["name","2010"],
                  key_on="feature.properties.name", fill_color="BuGn",
                  fill_opacity=0.7, line_opacity=0.2,
                  legend_name="Homocide Rate % 2010"
).add_to(my_map)
my_map.save("Rate of Homocide in South America.html")


    















