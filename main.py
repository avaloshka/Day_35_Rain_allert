import requests
from twilio.rest import Client
import os

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("api_key")

account_sid = "ACb6660dee953c939f597514e4a767c01c"
auth_token = os.environ.get("auth_token")

lon = -0.1257
lat = 51.5085

weather_params = {
                            "lat": lat,
                            "lon": lon,
                            "appid": api_key,
                            "exclude": "current,minutely,daily"
                        }


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in weather_data["hourly"][:48]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    # And now send sms
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today, bring an umbrella",
        from_="+12027967893",
        to="+447852234889"
    )

    print(message.status)
