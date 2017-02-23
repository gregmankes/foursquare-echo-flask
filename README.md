# Foursquare Echo Flask
Simple Restaurant and Bar suggestions by Alexa in a specific location.

### Usage
[![Using the skill](http://img.youtube.com/vi/gnda2KVUN-o/0.jpg)](https://youtu.be/gnda2KVUN-o "Alexa Bar and Restaurant Suggestions using Foursquare")

### Instructions

Clone repo

```
git clone https://github.com/gregmankes/foursquare-echo-flask.git
```

Install Flask-ask

```
pip install flask-ask --user
```

Install requests

```
pip install requests --user
```

Install geopy

```
pip install geopy --user
```

Add client_id and client_secret from Foursquare developer credentials

Install [ngrok](http://ngrok.com)

Follow instructions [here](https://github.com/johnwheeler/flask-ask) and [here](https://youtu.be/cXL8FDUag-s?t=1m26s) to create the skill

Copy the following into the intent schema

```json
{
    "intents": [{
        "intent": "LocationIntent",
        "slots": [{
            "name": "location",
            "type": "AMAZON.US_CITY"
        }]
    }, {
        "intent": "WhatsAroundMeIntent",
      	"slots":[{
          	"name":"location",
          	"type": "AMAZON.US_CITY"
        }]
    }, {
      	"intent": "RestaurantIntent"
    }, {
      	"intent": "BarIntent"
    }, {
      	"intent": "AMAZON.StopIntent"
    }]
}
```

Copy the following into the sample utterances

```
AMAZON.StopIntent stop
WhatsAroundMeIntent in {location}
BarIntent bar
BarIntent I am looking for a bar
RestaurantIntent I am looking for a restaurant
RestaurantIntent restaurant
LocationIntent {location}
```

Run the flask app
```
python app.py
```

Run ngrok
```
ngrok http 5000
```

Copy the ngrok https url to global endpoint

PROFIT!!!

SIDE NOTES:
To interface with alexa, you would say:
```
Alexa, open whatsaroundme
```
OR
```
Alexa, ask whatsaroundme in New York, New York
```
