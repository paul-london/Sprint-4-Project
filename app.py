import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header(Car Sales Analysis)

st.plotly_chart(hist)

st.plotly_chart(scatter_price_odo)

st.checkbox('Toggle color of scatter plot')