# -*- coding: utf-8 -*-
"""
Spyder Editor

MSc Data Science
Applied Data Science 1
Assignment 1 - 20 %
Hana Meah
16048117

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def lineplot1(df):
    """

    Line Plot 1 defining a time series for Applcitions received by Yale
    compared to Admissions Yale took each year

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

    Line Plot 2 defining a time series comparing Application numbers in 
    5 main local states

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

    Stacked Bar Graph defnining Growth of Applications to Yale from 2015-2022 
    visualising proportions of applicants from 3 states

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

    Pie Chart defnining proportion of Applications to Yale from 3 key states 
    in 2022

    """

    plt.figure(4)

    plt.pie(df, labels=states)
    plt.title("Admissions in 2022 Amongst 3 key states")
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    return


def piechart2(df, states):
    """

     Pie Chart 2 defnining proportion of Applications to Yale from 3 key states 
     in 2021

    """

    plt.figure(5)

    plt.pie(df, labels=states)
    plt.title("Admissions in 2021 Amongst 3 key states")
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    return


""" 

Main Program

"""

# reading Yale Admissions data
df_admits = pd.read_csv("YaleAdmits.csv")

# display(df.head(100))

lineplot1(df_admits)
lineplot2(df_admits)


# subset with less yearsonly 2015 to 2022 to make the insight more useful
df_new = df_admits.iloc[29:37]

bargraph(df_new)


# subset with values from 3 states in 2022
df_select = df_admits.iloc[-1, 24: 27]
states = ["New Haven", " New England", "New York State"]

piechart(df_select, states)


# subset with values from 3 states in 2021
df_select_2 = df_admits.iloc[-2, 24: 27]
states = ["New Haven", " New England", "New York State"]

piechart2(df_select_2, states)
