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
        # r = requests.get(
        #    'http://api.openweathermap.org/data/2.5/weather?APPID=7fc77377fc287a3ca61556cf825e9730&lat=%s&lon=%s' % (latitude, longitude))
        r = requests.get('https://api.darksky.net/forecast/24d67c234f99b3d0913838bdedb6148a/%s,%s' % (latitude, longitude))
        json_object = r.json()
        temp_k = json_object['currently']['temperature']
        temp_f = int(temp_k)
        city = str(ucity)
        sky = str(json_object['currently']['summary'])
        return render_template('weather.html', temp=temp_f, city=city, sky=sky)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
