# -*- coding: utf-8 -*-
"""Actividad_Integradora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ae6Qjxp9LrdofymdySS3ySJ4NDc6-GxK
"""

# pip install streamlit

import pandas as pd
import streamlit as st

df = pd.read_csv('https://drive.google.com/file/d/1WQ5QFkP9S1FfpAxCTxQpzWKEP5lD67uL/view?usp=drive_link')
st.title('The Police Incident Reports from 2028 to 2022 in San Francisco.')
st.markdown('The data shon below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case sucha as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution')

mapa = pd.DataFrame()
mapa = mapa.dropna()
st.map(mapa.astype(int))

'''
mapa['Date']= df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District']=df['Police District']
mapa['Neighborhood']=df['Analysis Neighborhood']
mapa['Incident Category']=df['Incident Category']
mapa['Incident Subcategory']=df['Incident Subcategory']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
'''
