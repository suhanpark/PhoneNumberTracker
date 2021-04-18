import phonenumbers as pn
from phonenumbers import geocoder as gc
from phonenumbers import carrier as car
from phonenumbers import timezone as tz
import requests
import json


def find_loc(number):
	ch_number = pn.parse(number, "CH")
	location = gc.description_for_number(ch_number, "en")
	return location


def isolate_nums(number):
	num = ""
	for i in number.strip():
		if i.isnumeric():
			num += i
	return num[1:]


def getCarrier_US(number):
	url = 'https://api.telnyx.com/v1/phone_number/1' + number
	html = requests.get(url).text
	data = json.loads(html)
	data = data["carrier"]
	carrier = data["name"]
	return carrier


def find_carrier(number):
	carrier = ""
	country_check = str(pn.parse(number))
	if "Country Code: 1 " in country_check:
		num = isolate_nums(number)
		carrier = getCarrier_US(num)
	else:
		service_number = pn.parse(number, "RO")
		carrier = car.name_for_number(service_number, "en")
	return carrier


def phone_number_info(number):
	pnum = pn.parse(number)
	location = find_loc(number)
	carrier = find_carrier(number)
	time_zone = tz.time_zones_for_number(pnum)
	validity = pn.is_valid_number(pnum)
	possiblity = pn.is_possible_number(pnum)
	L = [pnum, location, carrier, time_zone, validity, possiblity]
	return L

