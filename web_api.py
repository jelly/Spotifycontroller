#!/usr/bin/env python

import requests
import json

# Search:
# Album
# Artist
# Track

# Append album.json?= for json
API_URL =  'http://ws.spotify.com/search/1/'

def search_track(track):
    """search for a track in the spotify web API

    Keyword arguments:
    track -- UTF8 string
    """
    r = requests.get(API_URL + 'track.json' ,params={'q': track})
    data = json.loads(r.text)

    # {'page': 1, 'num_results': 405, 'query': 'learn to fly', 'type': 'track', 'limit': 100, 'offset': 0}

    # artists , name, href -> spotify uri
    for entry in data['tracks']:
        print(entry)


def search_artist(artist):
    """search for an artist in the spotify web API

    Keyword arguments:
    artist -- UTF8 string
    """
    r = requests.get(API_URL + 'artist.json' ,params={'q': artist})
    data = json.loads(r.text)

    # name, href -> spotify uri
    for entry in data['artists']:
        print(entry)


def search_album(album):
    """search for an album in the spotify web API

    Keyword arguments:
    album -- UTF8 string
    """
    r = requests.get(API_URL + 'album.json' ,params={'q': album})
    data = json.loads(r.text)

    # 

    # artists , name, href -> spotify uri
    for entry in data['albums']:
        print(entry)
