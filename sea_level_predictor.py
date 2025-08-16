import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (full data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = pd.Series(range(1880, 2051))
    plt.plot(years1, res1.intercept + res1.slope * years1, 'r', label='Best fit line 1880-2050')

    # Create second line of best fit (year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000, 2051))
    plt.plot(years2, res2.intercept + res2.slope * years2, 'g', label='Best fit line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
