import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(1, figsize=(16,9))
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    first_regression = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    previous_year = df["Year"].max()
    d = {"Year": range(previous_year + 1, 2051)}
    df2 = pd.DataFrame(data=d)
    df = pd.concat(objs=(df, df2), ignore_index=True)
    
    plt.plot(df["Year"], first_regression.intercept + first_regression.slope * df["Year"], c="g", label="fit all") 
    # Create second line of best fit
    df_recent_year = df.loc[(df["Year"] >= 2000) & (df["Year"] <= previous_year)]
    best_fit = linregress(df_recent_year["Year"], df_recent_year["CSIRO Adjusted Sea Level"])

    df_recent_year = pd.concat(objs=(df_recent_year, df2), ignore_index=True)
    plt.plot(df_recent_year["Year"], best_fit.intercept + best_fit.slope * df_recent_year["Year"], c="r")
    # Add labels and title
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()