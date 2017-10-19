import requests
from flask import Flask, render_template, request
from geocode import getGeocodeLocation

app = Flask(__name__)

darkapi = '24d67c234f99b3d0913838bdedb6148a'

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    try:
        ucity = request.form['userCity']
        latitude, longitude = getGeocodeLocation(ucity)
        r = requests.get('https://api.darksky.net/forecast/%s/%s,%s' % (darkapi, latitude, longitude))
        json_object = r.json()
        temp_k = json_object['currently']['temperature']
        temp_f = int(temp_k)
        city = str(ucity)
        sky = str(json_object['currently']['summary'])
        hourly = str(json_object['hourly']['summary'])
        rainchance = int(json_object['currently']['precipProbability'])
        return render_template('weather.html', temp=temp_f, city=city, sky=sky, hourly=hourly, rainchance=rainchance)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
