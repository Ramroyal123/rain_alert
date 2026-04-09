import os
import requests
from twilio.rest import Client
OWM_ENDPOINT="http://api.openweathermap.org/data/2.5/forecast"
YOUR_LATITUDE=16.596148
YOUR_LONGITUDE=81.592646
api_key=os.environ.get("API_KEY")

account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")

weather_parameters={
    "lat": YOUR_LATITUDE,
    "lon":YOUR_LONGITUDE,
    "appid":api_key,
    "cnt":4
}
response=requests.get(OWM_ENDPOINT,params=weather_parameters)
#response.raise_for_status()
weather_data=response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain, Remember to bring an ☂️",
        from_="+16625733588",
        to="+919666491898")
    print(message.status)



#recovery_code_twilio=SG6A732CVECCH9XEBJP7DTX7
