import requests
import datetime

OPEN_WEATHER_MAP_KEY = "15fe5de8d743843fdadd3ad7b5a458a7"


class WeatherData:
    """ Stores information about a weather at a range of dates """

    def __init__(self, data):
        self.data = data

    def at_time(self, d_time):
        """
		Get the current temperature at a given time
		:param d_time: datetime object to get weather for
		:return: A number represent temperature in celsius
		"""
        # Check for the range if fits between
        for i in range(len(self.data) - 1):
            day_data = self.data[i]
            next_day_data = self.data[i + 1]
            if day_data[0] < d_time < next_day_data[0]:
                return day_data[1]
        # Check if date is beyond last entry
        if len(self.data) > 0 and self.data[-1][0] < d_time:
            return self.data[-1][1]
        # Otherwise return bad value
        return -1


def from_openweathermap(town='hamilton'):
    """
	Fetch 5 day 3 hourly weather forecast from open weather map
	:param town: The location to get weather data for
	:return: Weather data object to query temperature
	"""
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={town},nz&mode=json&appid={OPEN_WEATHER_MAP_KEY}&units=metric'
    response = requests.get(url)

    segments = []
    if response.status_code == 200:
        data = response.json()
        for segment in data['list']:
            date = datetime.datetime.fromtimestamp(segment['dt'])
            temp = float(segment['main']['temp'])
            segments.append((date, temp))
    return WeatherData(segments)


def from_metservice(town='hamilton'):
    """
	Get the 10 day weather forcast for the specified town if it exists
	Default town is hamilton, list of towns is on metservice website
	# Where forecasts are taken from: https://www.metservice.com/towns-cities/hamilton#!/ten-day
	:param town: Town to get
	:return: A list of the next days weather
	"""

    # Full url for the 10 day forecase from metservice
    url = 'https://www.metservice.com/publicData/localForecast' + str(town).lower()

    response = requests.get(url)

    days = []

    if response.status_code == 200:
        data = response.json()
        for day in data['days']:
            date = datetime.datetime.strptime(day['dateISO'].replace(':', ''), "%Y-%m-%dT%H%M%S%z")
            t_min = int(day['min'])
            t_max = int(day['max'])
            # Add morning, day and evening temps
            morning = date.replace(hour=0, minute=0, second=0, microsecond=0)
            midday = morning.replace(hour=8)
            evening = morning.replace(hour=18)
            days.append(WeatherData([(morning, t_min), (midday, t_max), (evening, t_min)]))

    return days


defaultProvider = from_openweathermap
