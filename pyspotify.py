#!/usr/bin/env python

####################################
# SETTINGS
####################################



DEFAULT_SPOTIFY_ICON      = '/usr/share/pixmaps/spotify.png'
#CACHE_DIR                 = os.path.join(os.environ['HOME'], '.cache/spotify/Covers/')



import json
import requests
import dbus

# Append album.json?= for json
API_URL =  'http://ws.spotify.com/search/1/'


# Search:
# Album
# Artist
# Track

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

class SpotifyController(object):
    """SpotifyController
    """

    def __init__(self,bus = dbus.SessionBus()):
        self.spotify_dbus = bus.get_object('com.spotify.qt','/')
        self.player = dbus.Interface(self.spotify_dbus,'org.freedesktop.MediaPlayer2')
        self.properties = dbus.Interface(self.spotify_dbus, 'org.freedesktop.DBus.Properties')

    def next(self):
        self.player.Next()

    def prev(self):
        self.player.Previous()

    def pause(self):
        self.player.Pause()

    def play_pause(self):
        self.player.PlayPause()

    def stop(self):
        self.player.Stop()

    def seek(self, offset):
        self.player.Seek(offset)

    def set_position(self, trackid, position):
        self.player.SetPosition(track,position)

    def open_uri(self, uri):
        self.player.OpenUri(uri)

if __name__=='__main__':
    Spotify = SpotifyController()
    Spotify.play_pause()
