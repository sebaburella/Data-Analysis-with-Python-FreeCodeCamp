import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = True, index_col='date')

# Clean data
df = df[ 
    (df["value"] <= (df["value"].quantile(0.975))) &
    (df["value"] >= (df["value"].quantile(0.025)))
]


def draw_line_plot():
    fig = df.plot(xlabel="Date", ylabel="Page Views", title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019").figure





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = pd.DatetimeIndex(df.index).year
    df_bar["Months"] = pd.DatetimeIndex(df.index).month_name()
    
    df_bar = pd.pivot_table(df_bar, values="value", index="Years", columns="Months", dropna=False)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',         'December']
    df_bar = df_bar.reindex(columns=months)
    

    # Draw bar plot

    ax = df_bar.plot(kind='bar', xlabel = 'Years', ylabel = 'Average Page Views')
    fig = ax.get_figure()



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(1, 2)

    sns.boxplot(y="value", x= "year", data=df_box,  orient='v' , ax=axes[0]).set(title = "Year-wise Box Plot (Trend)",       xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(y="value", x= "month", data=df_box,  orient='v' , ax=axes[1], order=['Jan', 'Feb', 'Mar',
    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']).set(title = "Month-wise Box Plot (Seasonality)", xlabel =        'Month', ylabel = 'Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
