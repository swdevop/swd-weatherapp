import requests
from flask import Flask, render_template, request
from geocode import getGeocodeLocation

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    try:
        ucity = request.form['userCity']
        latitude, longitude = getGeocodeLocation(ucity)
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?APPID=7fc77377fc287a3ca61556cf825e9730&lat=%s&lon=%s' % (latitude, longitude))
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        temp_f = int((temp_k - 273.15) * 1.8 + 32)
        city = json_object['name']
        sky = str(json_object['weather'][0]['description'])
        return render_template('weather.html', temp=temp_f, city=city, sky=sky)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
