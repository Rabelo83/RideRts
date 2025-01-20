import requests

# API credentials
API_KEY = "KfRiwhzgjPeFG9rviJvkpCjnr"
BASE_URL = "https://riderts.app/bustime/api/v3/getpredictions"
RTPIDATAFEED = "bustime"

def get_predictions(stop_id):
    """
    Fetch predictions from the API for a given stop ID.

    Args:
        stop_id (str): The ID of the bus stop to retrieve predictions for.

    Returns:
        dict: The response data from the API as a dictionary, or None if there's an error.
    """
    # Parameters for the API request
    params = {
        "key": API_KEY,
        "rtpidatafeed": RTPIDATAFEED,
        "stpid": stop_id,
        "format": "json"
    }

    try:
        # Make the GET request to the API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print("Welcome to the Bus Prediction System!")
    stop_id = input("Please enter the stop ID: ").strip()  # Ask the user for the stop ID

    # Fetch predictions for the given stop ID
    predictions = get_predictions(stop_id)

    if predictions:
        # Check if the API response contains predictions
        if "bustime-response" in predictions and "prd" in predictions["bustime-response"]:
            print("\nPredictions for stop ID:", stop_id)
            for prd in predictions["bustime-response"]["prd"]:
                route = prd["rt"]
                destination = prd["des"]
                time = prd["prdctdn"]
                print(f"Route: {route}, Destination: {destination}, Arrival in: {time} minutes")
        else:
            print(f"No predictions available for stop ID {stop_id}.")
    else:
        print("Failed to retrieve predictions. Please try again later.")
