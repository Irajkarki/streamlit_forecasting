import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
import base64

st.title('Automated Time series Forescasting')

"This data app uses Facebook's open=souce prophet library."

#step-1:Import Data

df = st.file_uploader('Import the time series csv file here.column name should be ds and y')

if df is not None:
    data = pd.read_scv(df)
    data['ds'] = pd.to_datetime(data['ds'],errors='coerce')

    st.write(data)

    max_date= data['ds'].max()
    #st.write(max_data) yo hataudai herni


#step 2: Select Forecasr Horizon

"Keep in mind that forecasts become less accurate"

periods_input =st.number_input('h(ow many periods would you like to forecast into the future?',
min_value=1, max_value=365)

if df is not None:
    m= Prophet()
    m.fit(data)


