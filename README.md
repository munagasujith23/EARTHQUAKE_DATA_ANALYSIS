# Earthquake Data Analysis

A data analysis and visualization project in Python that explores 50 years of significant earthquakes (1965-2016) from a USGS dataset.

## Dataset
- Source: USGS earthquake dataset, downloaded from Kaggle
- Size: 23,412 records, magnitude 5.5 and above
- Period: 1965 to 2016
- File: `earth_quake.csv`

## What this project does
- Loads the data and fills missing values (numeric columns with the mean, "Magnitude Type" with "Unknown")
- Combines `Date` and `Time` into a datetime column and extracts the year and month
- Drops rows with invalid dates and removes duplicate rows
- Calculates mean, median, standard deviation, correlation, Z-scores, and the 95th percentile of magnitude
- Counts earthquakes per year and per reporting source (`Location Source`)
- Plots the Gutenberg-Richter relationship (magnitude vs. frequency)

## Visualizations
- Line chart: earthquakes per year
- Histogram: magnitude distribution
- Heatmap: correlation between magnitude and depth
- Bar chart: top 10 reporting sources
- Box plot: magnitude by source
- Scatter plots: depth vs. magnitude

## Key findings
- The most earthquakes in one year was in 2011 (712). The fewest was in 1966 (234).
- The average magnitude is about 5.9.
- Depth and magnitude are almost uncorrelated (correlation about 0.02).

## Tools used
Python, Pandas, NumPy, Matplotlib, Seaborn (written in Spyder)

## How to run
1. Install the libraries:
```
   pip install pandas numpy matplotlib seaborn
```
2. Keep `EarthQuake_Analysis.py` and `earth_quake.csv` in the same folder.
3. Run:
```
   python EarthQuake_Analysis.py
```

## Limitations and future work
- `Location Source` is the network that reported the earthquake, not a geographic region. A future version can group earthquakes by latitude and longitude.
- Some columns are mostly empty, so filling them with the mean adds little value. They could be dropped instead.
- The dataset includes non-earthquake events (nuclear explosions), which could be filtered out using the `Type` column.
- Next step: add a machine learning model with scikit-learn.

## Author
Kotra Venkata Nagendra Krishna Sai Kousik
BTech CSE (AI/ML), Sree Venkateswara College of Engineering
