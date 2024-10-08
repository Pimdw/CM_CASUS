##   Functies worden hier gedefinieerd   ##

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Verwijderen van alle uitschieters in de kolom van de dataset
def remove_outliers(dataframe, columnName):
    q1 = np.quantile(dataframe[columnName], 0.25)
 
    q3 = np.quantile(dataframe[columnName], 0.75)
    
    iqr = q3-q1
    
    upperBound = q3+(1.5*iqr)
    lowerBound = q1-(1.5*iqr)

    return dataframe[(dataframe[columnName] >= lowerBound) & (dataframe[columnName] <= upperBound)]


# Maakt een boxplot voor de kolom : gross
def boxplot_gross_and_budget(dataframe, columnName):
    fig1, ax1 = plt.subplots()
    ax1.boxplot(dataframe[columnName])
    def euro_formatter(x, _):
        if x >= 1000000:
            return f"${x / 1000000:.0f}M"
    plt.gca().yaxis.set_major_formatter(FuncFormatter(euro_formatter))
    ax1.set_title(f"Boxplot from {columnName}")
    ax1.set_xlabel(columnName)
    ax1.set_ylabel('Gross')
    plt.show()

# Maakt een histogram van de kolom : gross
def histogram_gross(dataframe, columnName):
    plt.hist(dataframe[columnName], bins=100, color='skyblue', edgecolor='black')
    def euro_formatter(x, _):
        if x >= 1000000:
            return f"${x / 1000000:.0f}M"
    plt.gca().xaxis.set_major_formatter(FuncFormatter(euro_formatter))
    plt.title(f"The frequency of {columnName}")
    plt.xlabel('Gross')
    plt.ylabel('Frequency')
    plt.show()


# Maakt een boxplot voor de kolom : Facebook-likes
def boxplot_likes(dataframe, columnName):
    fig1, ax1 = plt.subplots()
    ax1.boxplot(dataframe[columnName])
    ax1.set_title(f"Boxplot from {columnName}")
    ax1.set_xlabel(columnName)
    ax1.set_ylabel('Amount of likes')
    plt.show()


# Maakt een histogram voor de kolom: de frequentie van Facebook-likes
def histogram_likes(dataframe, columnName):
    plt.hist(dataframe[columnName], bins=100, color='skyblue', edgecolor='black')
    plt.title(f"Frequency of {columnName}")
    plt.xlabel('Likes')
    plt.ylabel('Frequency')
    plt.show()

# Functie uit les CM10
# Dit passen we toe om de leesbaarheid te verbeteren in de visualisaties
def euro_formatter(x, _):
    if x >= 1000000:
        return f"${x / 1000000:.0f}M"

# Maakt een scatter plot van twee variabelen en toont de correlatiecoëfficiënt.
def correlation_plot(df, targetVariable, featureVariable):
    fig1, ax1 = plt.subplots()
    sns.regplot(x=targetVariable, y=featureVariable, data=df, scatter_kws={'s': 3}, line_kws={'color': 'red'}, ax=ax1)

    plt.gca().xaxis.set_major_formatter(FuncFormatter(euro_formatter))
    
    ax1.set_xlabel(targetVariable)
    ax1.set_ylabel(featureVariable)

    correlation = df[[targetVariable, featureVariable]].corr().iloc[0, 1]

    ax1.set_title(f"{targetVariable} vs {featureVariable} (r = {correlation:.2f})")



# Film in 5 Categorieën delen
def classify_movie(row):
    if row['budget'] > 100000000 and row['gross'] > 300000000:
        return 'Blockbuster'# Hoog budget, hoge opbrengst
    
    elif row['budget'] > 100000000 and row['gross'] < 50000000:
        return 'Flop' # Hoog budget, lage opbrengst
    
    elif row['budget'] < 20000000 and row['gross'] > 50000000:
        return 'Cultfilm' # Laag budget, hoge opbrengst
    
    elif 50000000 <= row['budget'] <= 100000000 and 50000000 <= row['gross'] <= 300000000:
        return 'Mid-Range Movie' # Middelgroot budget, middelgrote opbrengst
    
    else:
        return 'Average' # Overige gewone films