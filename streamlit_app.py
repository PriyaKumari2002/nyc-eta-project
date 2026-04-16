import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle

# page config
st.set_page_config(
    page_title="NYC Ride Demand Predictor",
    page_icon="🚕",
    layout="wide"
)

# load model
@st.cache_resource
def load_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/train.csv')
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['hour']    = df['Date/Time'].dt.hour
    df['day']     = df['Date/Time'].dt.day
    df['month']   = df['Date/Time'].dt.month
    df['weekday'] = df['Date/Time'].dt.weekday
    return df

model = load_model()
df    = load_data()

# title
st.title("🚕 NYC Ride Demand Predictor")
st.markdown("Predict how many Uber rides will happen in NYC at any given time!")

# sidebar inputs
st.sidebar.header("🔧 Input Parameters")

month = st.sidebar.selectbox(
    "Month",
    options=list(range(1, 13)),
    format_func=lambda x: ['Jan','Feb','Mar','Apr','May','Jun',
                           'Jul','Aug','Sep','Oct','Nov','Dec'][x-1]
)

day = st.sidebar.slider("Day of Month", 1, 31, 15)

weekday = st.sidebar.selectbox(
    "Day of Week",
    options=list(range(7)),
    format_func=lambda x: ['Monday','Tuesday','Wednesday',
                           'Thursday','Friday','Saturday','Sunday'][x]
)

hour = st.sidebar.slider("Hour of Day", 0, 23, 8)

# make prediction
input_data = pd.DataFrame({
    'month':   [month],
    'day':     [day],
    'weekday': [weekday],
    'hour':    [hour]
})
prediction = round(model.predict(input_data)[0])

# show prediction
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🚕 Predicted Rides", f"{prediction:,}")

with col2:
    hour_label = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    st.metric("🕐 Selected Time", f"{display_hour}:00 {hour_label}")

with col3:
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    st.metric("📅 Selected Day", days[weekday])

st.markdown("---")

# charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Rides Per Hour (All Data)")
    hourly = df.groupby('hour').size().reset_index()
    hourly.columns = ['hour', 'rides']
    fig = px.line(hourly, x='hour', y='rides',
                  markers=True, color_discrete_sequence=['#f39c12'])
    fig.add_vline(x=hour, line_dash="dash", line_color="red",
                  annotation_text="Selected Hour")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Rides Per Weekday")
    weekly = df.groupby('weekday').size().reset_index()
    weekly.columns = ['weekday', 'rides']
    weekly['day_name'] = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    fig2 = px.bar(weekly, x='day_name', y='rides',
                  color_discrete_sequence=['#3498db'])
    fig2.add_vline(x=weekday, line_dash="dash", line_color="red")
    st.plotly_chart(fig2, use_container_width=True)

# map
st.subheader("🗺️ NYC Pickup Locations")
sample = df.sample(10000)
fig3 = px.scatter_mapbox(
    sample, lat='Lat', lon='Lon',
    opacity=0.3, zoom=10,
    mapbox_style='open-street-map',
    title='NYC Uber Pickup Locations'
)
st.plotly_chart(fig3, use_container_width=True)