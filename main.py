#!/usr/bin/env python

import web_api
from pyspotify import SpotifyController

if __name__== '__main__':
   Spotify = SpotifyController()
   print(Spotify.get_metadata('artist'))
