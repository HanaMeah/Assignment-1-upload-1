# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# display(df.head(100))


def lineplot1(df):
    """

    write a docstring PLOT 1 LINE PLOT

    """

    plt.figure(1)
    plt.plot(df["Year Entered"], df["Applications"], label="Applications")
    plt.plot(df["Year Entered"], df["Admits"], label="Admissions")

    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    plt.xlabel("Year of Applications")
    plt.ylabel("Number of Applicants")
    plt.title("Yale Applications vs Admissions")
    return



def lineplot2(df):
    """

    write a docstring PLOT 2 LINE PLOT

    """

    plt.figure(2)
    plt.plot(df["Year Entered"], df["NewHaven"], label="New Haven")
    plt.plot(df["Year Entered"], df["NewEngland"], label="New England")
    plt.plot(df["Year Entered"], df["NewYorkState"], label="New York State")
    plt.plot(df["Year Entered"], df["EastofMississippi"],
             label="East Mississippi")
    plt.plot(df["Year Entered"], df["WestofMississippi"],
             label="West Mississippi")

    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    plt.xlabel("Year of Applications")
    plt.ylabel("Number of Applicants")
    plt.title("Yale Applications from key local states")
    return



def bargraph(df_new):
    """

    write a docstring PLOT 3 bar graph

    """

    plt.figure(3)
    plt.bar(df_new["Year Entered"],
            df_new["NewYorkState"], label="New York State")
    plt.bar(df_new["Year Entered"], df_new["NewEngland"], label="New England")
    plt.bar(df_new["Year Entered"], df_new["NewHaven"], label="New Haven")

    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    plt.xlabel("Year of Applications")
    plt.ylabel("Number of Applicants")
    plt.title("Yale Applications from 3 key local states 2015 to 2022")
    return



def piechart(df, states):
    """

    write a docstring PLOT 4 bar tree map

    """
    
    plt.figure(4)

    plt.pie(df, labels=states)
    plt.title("Admissions in 2022 Amongst 3 key states")
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    return




def piechart2(df, states):
    """

    write a docstring PLOT 4 bar tree map

    """
    
    plt.figure(5)

    plt.pie(df, labels=states)
    plt.title("Admissions in 2021 Amongst 3 key states")
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    return



# reading Yale Admissions data
df_admits = pd.read_csv("YaleAdmits.csv")

lineplot1(df_admits)
lineplot2(df_admits)


# subset less years to make the insight more useful
df_new = df_admits.iloc[29:37]

bargraph(df_new)


df_select = df_admits.iloc[-1, 24: 27]
states = ["New Haven", " New England", "New York State"]



piechart(df_select, states)


df_select_2 = df_admits.iloc[-2, 24: 27]
states = ["New Haven", " New England", "New York State"]

piechart2(df_select_2, states)