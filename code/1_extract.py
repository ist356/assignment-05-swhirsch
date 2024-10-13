import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  

survey = pd.read_csv('https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv')
survey['year'] = survey['Timestamp'].apply(pl.extract_year_mdy)
survey.to_csv('cache/survey.csv', index=False)
years = survey['year'].unique()

for year in years:
    col_year = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&displayColumn=0")
    col_year = col_year[1]
    col_year['year'] = year
    col_year.to_csv(f'cache/col_{year}.csv', index=False)

url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"
state_table = pd.read_csv(url)
state_table.to_csv('cache/states.csv', index=False)

