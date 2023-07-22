import requests

API = '#Use your own API from the website'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter the city name: ')
request_url = f'{BASE_URL}?appid={API}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data ['weather'][0]['description']
    print(weather)
    temp = round(data['main']['temp'] - 273.15,2)
    
    print('Weather: ',weather)
    print('Temperature: ', temp, 'celcius')
    


else:
    print('an error occured')

