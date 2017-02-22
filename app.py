import logging
from flask import Flask
from flask_ask import Ask, statement,  session, question
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
import requests
import json
from geopy import Nominatim
from random import choice

class Location():

    def __init__(self, location):
        geoloc = Nominatim()
        loc = geoloc.geocode(location)
        self.lat = loc.latitude
        self.lon = loc.longitude

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

loc = None
base_url = "https://api.foursquare.com/v2/venues/search?v=20131016"
bar_code = "categoryId=4bf58dd8d48988d116941735"
rest_code = "categoryId=4bf58dd8d48988d1c4941735"
client_id = "Your id"
client_secret = "your secret"

@ask.launch
def launched():
    return question("Hello, welcome to whats around me. Where are you located?")

@ask.intent("LocationIntent")
def get_location(location):
    location = str(location)
    global loc
    try:
        loc = Location(location)
    except Exception:
        return statement("There was an error getting the location you requested. Please try again.")
    return question("Are you looking for a Bar or a Restaurant? For example, you can say, I'm looking for a bar, or just bar.")

@ask.intent("BarIntent")
def find_bars():
    if loc == None:
        return statement("There was an error in getting the location")
    url = "{}&{}&{}&{}&ll={}%2C{}".format(base_url, bar_code, client_id, client_secret, loc.get_lat(), loc.get_lon())
    bar = get_result(url)
    if bar == None:
        return statement("There was an error getting the establisments you requested")
    return statement("You should try {}".format(bar))

@ask.intent("RestaurantIntent")
def find_restaurant():
    if loc == None:
        return statement("There was an error in getting the location")
    url = "{}&{}&{}&{}&ll={}%2C{}".format(base_url, rest_code, client_id, client_secret, loc.get_lat(), loc.get_lon())
    rest = get_result(url)
    if rest == None:
        return statement("There was an error getting the establisments you requested")
    return statement("You should try {}".format(rest))

def get_result(url):
    r = requests.get(url)
    if r.json()["meta"]["code"] >= 400:
        return None
    j = json.loads(r.text)
    result_list = [u"{} in {}".format(obj["name"], obj["location"]["city"]) for obj in j["response"]["venues"]]
    to_return = str(choice(result_list))
    return to_return

@ask.intent("WhatsAroundMeIntent")
def whats_around_me(location):
    return get_location(location)

@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Stopping")

if __name__ == '__main__':
    app.run(debug=True)
