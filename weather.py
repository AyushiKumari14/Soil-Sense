import requests

API_KEY = "088c5880f8fcc418e2fa1b39c3f30221"


def get_weather(city):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["name"],
                "main": {
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"]
                },
                "weather": [
                    {
                        "description": data["weather"][0]["description"]
                    }
                ]
            }

            forecast = None
            weather_error = None

            return weather, forecast, weather_error

        else:
            try:
                error_message = response.json().get(
                    "message",
                    "Unable to get weather data"
                )
            except Exception:
                error_message = "Unable to get weather data"

            return None, None, f"Weather API Error: {error_message}"

    except requests.exceptions.RequestException as e:
        return None, None, f"Connection Error: {e}"

    except Exception as e:
        return None, None, f"Weather Error: {e}"