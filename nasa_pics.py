import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from twilio.rest import Client

# NASA APOD API endpoint
url = "https://api.nasa.gov/planetary/apod"

# API key (you need to sign up for a free API key at https://api.nasa.gov/)
api_key = ""

# Twilio configuration
account_sid = ""
auth_token = ""
twilio_phone_number = ""
receiver_phone_number = ""

# Parameters for the request (date is optional)
params = {
    'api_key': api_key,
    # 'date': 'YYYY-MM-DD'  # You can specify a date if you want a picture from a specific day
}

# Making the GET request
response = requests.get(url, params=params)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Converting the response to JSON format
    data = response.json()
    
    # Extracting relevant information
    title = data['title']
    image_url = data['url']
    explanation = data['explanation']
    
    # Printing the information
    # print(f"Title: {title}")
    # print(f"Image URL: {image_url}")
    # print(f"Explanation: {explanation}")

    # Download the image
    # image_response = requests.get(image_url)
    # img_data = BytesIO(image_response.content)

    # Twilio setup
    client = Client(account_sid, auth_token)

    # Send the image via MMS
    message = client.messages.create(
    	to=receiver_phone_number,
    	from_=twilio_phone_number,
    	body=title,
    	#media_url=[img_data.getvalue()]
    	)
else:
	print(f"Error: {responses.status_code}")


