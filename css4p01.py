# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:57:48 2024

@author: thabi
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")

file.dropna(inplace=True)

highest_rating_movie = file.loc[file["Rating"].idxmax()]

print(highest_rating_movie)

#Q1: The Dark Knight



print(file.describe())

# Q2:average avenue = 84.564558 (range= 70 and 100 mil)

data_2015_2017 = file[(file["Year"]>=2015) & (file["Year"] <=2017)]

print(data_2015_2017.describe())

#Q3:average for 2015-2017 = 64.498958 (range= 50 and 80 mil)

parent_file = pd.read_csv("movie_dataset.csv")

movies_2016 = (parent_file["Year"]==2016).sum()

print(movies_2016)

#Q4: movies released in 2026= 297

movies_by_C_Nola = (parent_file["Director"]=="Christopher Nolan").sum()

print(movies_by_C_Nola)

#Q5= 5 movies

movie_rating = (parent_file["Rating"] >=8.0).sum()

print(movie_rating)

#Q6: 78 MOVIES

movies_directed_by_Chris = parent_file[parent_file["Director"]=="Christopher Nolan"]["Rating"].median()

print(movies_directed_by_Chris)

#Q7: median rating = 8.6

Year_with_highest_rating = parent_file.groupby("Year")["Rating"].mean()

Year_with_highest_rating_mean = Year_with_highest_rating.idxmax()
print(Year_with_highest_rating_mean)

#Q8: highest average year is 2007

movies_2006 = (parent_file["Year"]==2006).sum()

Diff_2006_2016 = movies_2016 - movies_2006

Percentage_Diff = Diff_2006_2016*100/movies_2006

print(Percentage_Diff)

#Q9: percentage increase is 575

Common_actor = parent_file["Actors"].str.split(',', expand=True).stack().reset_index(level=1,drop=True).to_frame('Actor')

Most_Common_Actor = Common_actor["Actor"].mode()

print(Most_Common_Actor)

#Q10: common actor Mark Wahlberg

Uniq_Genre = parent_file["Genre"].str.split(",").explode().str.strip()

Unique_Genre = Uniq_Genre.nunique()

print(Unique_Genre)

#Q11: 20 genres

"""
Finding numeric columns and use use them to find correlation

"""
Numeric_Col = parent_file.select_dtypes(include=["number"]).columns

#Correlation

Correlation = parent_file[Numeric_Col].corr()