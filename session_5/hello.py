from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)


# -----------------------------------------------------------------------------
# WELCOME
# -----------------------------------------------------------------------------


@app.route("/")
def hello():
    return render_template("hello.html", name="User")


@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())


@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    print form_data['email']
    return "ALL OK"


# -----------------------------------------------------------------------------
# WEATHER API
# the code is mostly based on this post on stackoverflow:
# http://stackoverflow.com/questions/23521652/flask-and-python-how-to-make-search-engine-for-data-from-mysql-database
# -----------------------------------------------------------------------------


def get_the_weather(place):
    '''
    Get the weather for a specified place using the openweathermap api.
    '''
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",  # the endpoint
        params={
            "q": place,  # the 'q'uery
            "units": "metric",
            "appid": "44db6a862fba0b067b1930da0d769e98"
        }
    )
    weather_data = response.json()
    return weather_data


def format_weather_output(weather_data):
    '''
    Function to format the weather data into a neater output for display
    '''
    weather_display = "It's {}C in {}, and the the weather is {}".format(
        weather_data['main']['temp'],
        weather_data["name"],
        weather_data['weather'][0]['main']
    )
    return weather_display


@app.route('/weather', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        # first we collect the weather data with our custom function
        # called get_the_weather() defined above which is in JSON format
        weather_data = get_the_weather(place=request.form['weather'])
        # then we format the json output into a nicer string with the other
        # custom function format_weather_output(). You could also have the
        # displaying of the weather data in the weather.html file.
        weather_display = format_weather_output(weather_data=weather_data)
        # when we have a single string that contains all the weather data
        # we render the weather.html template, assigning the weather string
        # to a paramter weather_record that will be available in the html.
        return render_template("weather.html", weather_record=weather_display)
    # this is the default state, when we have not performed a search yet,
    # we still want the /weather page to render.
    return render_template('weather.html')


# -----------------------------------------------------------------------------
# RUN APP
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
