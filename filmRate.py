#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:59:40 2019

"""

import requests
import json
import sys

apicall = "http://www.omdbapi.com/"

def ratings(film, KEY):

    payload = {'apikey': KEY, 'r': 'json', 't': film}
    resp = requests.get(apicall, params=payload)
    if resp.status_code == 200:
        respDict = json.loads(resp.text)
        if respDict['Response'] == 'True':
            rateLine = [el for el in respDict['Ratings'] if el['Source'] == 'Rotten Tomatoes']
            if rateLine:
                rating = rateLine.pop()['Value']
                print("Rotten Tomatoes rating for \"{0}\" => {1}".format(respDict['Title'], rating))
            else:
                print("Rotten Tomatoes rating not availble for \"{}\"".format(respDict['Title']))
        else:
            print("ERROR:  ", respDict['Error'])
    else:
        print("Error, please check key validity or server connection issues")


if __name__ == "__main__":
    APIKEY = ""
    try:
        with open ("key.txt") as f:
            APIKEY = f.read().strip("\n")
    except IOError: 
        print("Error: File key.txt does not exist")
        sys.exit()
    
    if not APIKEY:
        print("API key is missing, check key.txt file content")
        sys.exit()
    
    if len(sys.argv) == 1:

        while True:
            film_input = input("\nPlease insert the film title (Return to exit):  ")
            if film_input == "":
                break
            ratings(film_input, APIKEY)

    elif len(sys.argv) == 2:
        ratings(sys.argv[1], APIKEY)
    else:
        print("Please check syntax, program use: \n\nInteactive mode: filmRate.py\nCommand line mode: filmRate.py \"film name\"\n")

