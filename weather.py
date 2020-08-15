#! /usr/bin/env python3.8

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current information for your zip code')
parser.add_argument('zip', help='zip/postal codeto get weather for')
parser.add_argument('--country', '-c', default='us')

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Error: no 'OWM_API_KEY' provoded")
    sys.exit(1)
url = f"https://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)
# print(res)

if res.status_code != 200:
    print(f"Error connecting to weather provider: (res.status_code)")
    sys.exit(2)

print(res.json())
