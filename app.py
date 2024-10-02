# Module import
import streamlit as st
import pandas as pd
import plotly.express as px

# Read CSV
data = pd.read_csv('vehicles_us.csv')

# Data cleanup
# There are 51525 rows of information, and some columns have missing values: model_year, cylinders, odometer, paint_color, and is_4wd
# We should also consider converting model_year and cylinders to integer type, and is_4wd to bool type
data['model_year'] = data['model_year'].fillna('Unknown')
#data['model_year'] = data['model_year'].astype(int)

# Electric cars have 0 cylinders, we can make that substitution prior to replacing missing values
data.loc[data['fuel'] == 'electric', 'cylinders'] = 0.0
data['cylinders'] = data['cylinders'].fillna('Unknown')
#data['model_year'] = data['model_year'].astype(int) 

data['odometer'] = data['odometer'].fillna('Unknown')

data['paint_color'] = data['paint_color'].fillna('Unknown')

data['is_4wd'] = data['is_4wd'].fillna('Unknown')
data['is_4wd'] = data['is_4wd'].astype(bool) 

# Header
st.header('Car Sales Analysis')

# Histogram of Model Years of the cars
hist = px.histogram(data, x='model_year', title='Model Year Frequency', nbins=100, labels={'x':'Model Year', 'y':'Count'})
hist.update_layout(bargap=0.1)
st.plotly_chart(hist)

# Scatter plot of price vs. odometer reading
color_map = {'gas': 'red', 'hybrid': 'blue', 'electric': 'green', 'diesel': 'orange', 'other': 'black'}
scatter_price_odo = px.scatter(data, title='Sale Price vs. Odometer Reading (by Fuel Type)', x='odometer', y='price', hover_data=['odometer', 'price'], color='fuel', color_discrete_map=color_map)
st.plotly_chart(scatter_price_odo)

# Making checkbox to alter behavior of scatter plot between sorting by fuel type to sorting by vehicle condition
checked = st.checkbox('If checked: Change scatterplot to sort by Vehicle Condition')
if checked:
    st.write('Scatterplot will sort by Vehicle Condition')
    color_map_cond = {'salvage': 'red', 'like new': 'blue', 'good': 'green', 'fair': 'orange', 'excellent': 'black'}
    scatter_price_odo = px.scatter(data, title='Sale Price vs. Odometer Reading (by Vehicle Condition)', x='odometer', y='price', hover_data=['odometer', 'price'], color='condition', color_discrete_map=color_map_cond)
else:
    st.write('Scatterplot will sort by Fuel Type')