import os
import requests
from twilio.rest import Client
OWM_ENDPOINT="http://api.openweathermap.org/data/2.5/forecast"
api_key="478ad1488354962c4d0bf85d9016c360"

account_sid="ACfecaf224268176892dfe2e52b046a642"
auth_token="8fd5ee7dc746591b85469089e9eb4738"

weather_parameters={
    "lat": 16.596148,
    "lon":81.592646,
    "appid":api_key,
    "cnt":4
}
response=requests.get(OWM_ENDPOINT,params=weather_parameters)
response.raise_for_status()
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
