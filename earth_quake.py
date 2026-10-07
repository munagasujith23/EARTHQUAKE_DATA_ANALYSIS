# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:22:39 2026

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("earth_quake.csv")

# Fill missing values with mean or default values
df = df.fillna({
    "Depth Error":df["Depth Error"].mean(),
    "Depth Seismic Stations":df["Depth Seismic Stations"].mean(),
    "Magnitude Type":("Unknown"),
    "Magnitude Error":df["Magnitude Error"].mean(),
    "Magnitude Seismic Stations":df["Magnitude Seismic Stations"].mean(),
    "Azimuthal Gap":df["Azimuthal Gap"].mean(),
    "Horizontal Distance":df["Horizontal Distance"].mean(),
    "Horizontal Error":df["Horizontal Error"].mean(),
    "Root Mean Square":df["Root Mean Square"].mean()
})

# Combine Date and Time into a single datetime column
df["DateTime"]=pd.to_datetime(df["Date"]+" "+df["Time"],format = "mixed",errors = "coerce")

# Extract Year and Month from datetime
df["Year"] = df["DateTime"].dt.year
df["Month"] = df["DateTime"].dt.month

# Drop rows with invalid datetime values
df = df.dropna(subset = ["DateTime","Year","Month"])

# Remove duplicate rows
df.drop_duplicates()

# Clean Location Source column
df["Location Source"].unique()
df["Location Source"].str.strip().str.lower()

# Convert dataframe to numpy array
data = df.to_numpy()

# Basic statistics
np.mean(df["Magnitude"])
np.mean(df["Depth"])
np.median(df["Magnitude"])
np.median(df["Depth"])
np.std(df["Magnitude"])
np.std(df["Depth"])

# Correlation coefficient between Depth and Magnitude
correlation = np.corrcoef(df["Depth"],df["Magnitude"])[0,1]

# Z-score for Magnitude
df["Z_score"] = ((df["Magnitude"]-np.mean(df["Magnitude"]))/np.std(df["Magnitude"]))
df[df["Z_score"]>3]  # Outliers

# Top 5% magnitudes
percentage = np.percentile(df["Magnitude"],95)
top_5 = df[df["Magnitude"]>=percentage]

# Gutenberg-Richter law plot
magnitude = data[:,8]
bins = np.arange(3,9,0.1)
frequency,edges = np.histogram(magnitude,bins = bins)
cummulative_frequency = np.cumsum(frequency[::-1])[::-1]
magnitude_values = (edges[:-1]+edges[1:])/2
mask = cummulative_frequency>0
plt.plot(magnitude_values[mask],np.log10(cummulative_frequency[mask]),marker = "o")
plt.title("Magnitude-frequency Distribution(Gutenberg-Richter relationship)")
plt.xlabel("Magnitude Values")
plt.ylabel("log10(Cummulative Frequency)")
plt.show()

# Frequency of earthquakes per year
year_freq = df["Year"].value_counts().sort_index()

# Location Source counts
df["Location Source"].value_counts().sort_index()

# Pivot table for mean Magnitude and Magnitude Error by Location Source
pd.pivot_table(
    df,
    index = "Location Source",
    values = ["Magnitude","Magnitude Error"],
    aggfunc = "mean")

# Count of Magnitude Types
df["Magnitude Type"].value_counts()
#Visulations

# Line plot:Earthquake frequency per year
plt.plot(year_freq.index,year_freq.values,color = "red",label = "years",
         marker = "o",markeredgecolor = "black",markerfacecolor = "green")
plt.title("Earthquake Frequency Trend Over Years")
plt.xlabel("Years")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Histogram:Magnitude distribution
sns.histplot(df["Magnitude"],bins = 10,edgecolor ="black")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.title("Magnitude Distribution")
plt.show()

# Heatmap:Correlation  between Magnitude and Depth
correlation = df[["Magnitude","Depth"]].corr()
sns.heatmap(correlation,annot = True,cmap="coolwarm")
plt.title("Correlation Matrix(Magnitude,Depth)")
plt.show()

# Bar Chart:Top 10 most affected regions
data = df["Location Source"].value_counts().head(10)
plt.bar(data.index,data.values)
plt.title("Top10 Most Affected Regions")
plt.xlabel("Location Source")
plt.ylabel("Number of Earthquakes")
plt.show()

#box plot: Magnitude Distribution by region
plt.figure(figsize=(25,10))
sns.boxplot(x = df["Location Source"],y=df["Magnitude"],hue=df["Location Source"],data = df,)
plt.title("Magnitude Distribution by Region")
plt.show()

# Scatter plot:Depth vs Magnitude relationship
plt.figure(figsize = (20,10))
plt.scatter("Depth","Magnitude",data = df)
plt.xlabel("Depth")
plt.ylabel("Magnitude")
plt.title("Depth vs Magnitude relationship")
plt.show()

# Log- Scaled scatter plot:Magnitude vs Depth
plt.figure(figsize = (15,15))
sns.scatterplot(x = "Magnitude",y ="Depth",data=df,hue = "Location Source")
plt.xscale("log")
plt.yscale("log")
plt.title("Magnitude-frequency(Gutenberg Richter law)")
plt.show()
