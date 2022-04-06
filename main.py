
import requests
import os

from twilio.rest import Client

API_KEY = os.environ.get("API_KEY")


account_sid = os.environ.get("A_SSID")
auth_token = os.environ.get("AUTH_TOKEN")

MY_LAT = "20.593683"
MY_LNG = "78.962883"

rain_check = 0
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

with requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters) as response:
    response.raise_for_status()
    weather_data = response.json()
    hourly_weather_data = weather_data["hourly"]
    # print(hourly_weather_data)

    for i in hourly_weather_data[:13]:
        weather_id = i["weather"][0]["id"]
        if int(weather_id) < 700:
            rain_check += 1
    if rain_check == 0:
        client = Client(account_sid,auth_token)
        message = client.messages \
            .create(
            body="It looks like it might rain today, bring an ☂️",
            from_='+15074195734',
            to=os.environ.get("NO")
        )
    else:
        print("It does not look like it will rain today")
    # print(message.status)




