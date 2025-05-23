import streamlit as st
import requests
import pandas as pd
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''


date = st.date_input("Pickup date", value= "2014-07-06")
time = st.time_input('Pickup time', value=datetime.time(19, 18, 0))
pickup_datetime = f"{date} {time}"
pickup_longitude = st.number_input("Pickup longitude", format="%.6f", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", format="%.6f", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", format="%.6f", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", format="%.6f", value=40.769802)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=2)

st.write(f'Pickup date and time: {pickup_datetime}')
st.write(f'date: {date}')
st.write(f'time: {time}')

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

response = requests.get(url, params=params)

st.write(f'The predicted taxi fare is ', response.json())
