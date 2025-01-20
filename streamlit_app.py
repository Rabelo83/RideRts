import streamlit as st
import requests

# API Configuration
API_KEY = "KfRiwhzgjPeFG9rviJvkpCjnr"
BASE_URL = "https://riderts.app/bustime/api/v3/getpredictions"
RTPIDATAFEED = "bustime"

# Streamlit App
st.title("Bus Prediction App")
st.write("Enter a bus stop number to get predictions.")

# User Input
bus_stop = st.text_input("Bus Stop Number:")

if st.button("Get Prediction"):
    if bus_stop.strip():
        # API Request
        params = {
            "key": API_KEY,
            "rtpidatafeed": RTPIDATAFEED,
            "stpid": bus_stop,
            "format": "json"
        }
        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()

                # Handle API response
                if "bustime-response" in data and "prd" in data["bustime-response"]:
                    predictions = data["bustime-response"]["prd"]

                    st.subheader(f"Predictions for Bus Stop {bus_stop}")
                    for prediction in predictions:
                        route = prediction.get("rt", "N/A")
                        destination = prediction.get("des", "N/A")
                        time = prediction.get("prdctdn", "N/A")

                        st.write(f"Route: {route}, Destination: {destination}, Arrival in: {time} minutes")
                else:
                    st.warning(f"No predictions available for Bus Stop {bus_stop}.")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid bus stop number.")
