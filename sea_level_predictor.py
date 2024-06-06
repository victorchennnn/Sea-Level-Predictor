import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit that goes through the year 2050
    regression1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope1 = regression1.slope
    intercept1 = regression1.intercept

    #create df from first year in original df to 2051 to plot the line
    max_year = df['Year'].max()
    extra_years = pd.DataFrame({'Year': range(max_year + 1, 2051)})
    extended_years = pd.concat([df['Year'], extra_years['Year']], ignore_index=True)

    plt.plot(extended_years, intercept1 + slope1*extended_years, color='r')


    # Create second line of best fit
    regression2 = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    slope2 = regression2.slope
    intercept2 = regression2.intercept

    #create df from 2000 to 2051 to plot the line
    years_since_2000 = pd.DataFrame({'Year': range(2000, 2051)})

    plt.plot(years_since_2000, intercept2 + slope2*years_since_2000, color='g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()