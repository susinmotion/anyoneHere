# from CONTAINING FOLDER OF RUN.PY import MODULE NAMED BELOW
from app import app
from flask import render_template, url_for, request
import pygeocoder, foursquare
from pygeocoder import Geocoder
import requests



def import_foursq():
	with open("foursq_api_key", "r") as f:
		my_client_ID,my_client_secret=f.readlines()
		fsq_client=foursquare.Foursquare(client_id=my_client_ID, client_secret=my_client_secret)
		return fsq_client

global fsq_client
fsq_client=import_foursq();

@app.route('/', methods=['GET','POST'])
#@app.route('/start', methods=['GET','POST'])
#@app.route('/start/<location>', methods=['GET','POST'])
#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown

def index():
	print fsq_client
	if request.method=="GET":
		return render_template ("start.html")
	else:
		location=request.form.get('location')
		destination=request.form.get('destination')
		return ((map(location,destination)))

@app.route('/map')

def map(location,destination):
	api_key=open('api_key').read()
	url="https://maps.googleapis.com/maps/api/js?key=%s"%api_key
	geoOrig=Geocoder.geocode(location)
	geoDest=Geocoder.geocode(destination)
	lat1,lng1=geoOrig[0].coordinates
	lat2,lng2=geoDest[0].coordinates
	directionsurl=("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&key=%s")%(location, destination, api_key)
	directions=requests.get(directionsurl)
	print directions.content
	return render_template("base.html", url=url, lat1=lat1, lng1=lng1, lat2=lat2,lng2=lng2)

#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown
#def THE NAME OF THE THING AFTER THE SLASH--different page views
