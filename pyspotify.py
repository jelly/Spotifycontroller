import dbus
from dbus.exceptions import DBusException

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

    def get_property(self,property_name):
        """Get the properties from Spotify

        """
        valid_properties = ['PlaybackStatus','LoopStatus','Shuffle','Rate','Metadata','Volume','Position','MinimumRate',
                'MaximimRate','CanGoNext','CanGoPrevious','CanPlay','CanPause','CanSeek','CanControl',
                'CanQuit','Identity','HasTrackList','DesktopEntry','HasTrackList','CanRaise','SupportedUriSchemes',
                'SupportedMimeTypes','Metadata']

        if property_name in valid_properties:
            if property_name == 'Volume':
                return self.player.Volume()
            else:
                return self.properties.Get('org.freedesktop.MediaPlayer2',property_name)
        else:
            return None

    def set_property(self,property_name,value):
        """Set property

        TODO: check if any of these actually work
        """
        
        valid_properties = {
                'Volume':   self.player.SetVolume,
                'Rate':     self.player.SetRate,
                'Shuffle':  self.player.SetShuffle,
                'Position': self.player.SetPosition, }

        if property_name in valid_properties:
            valid_properties[property_name](value)
            return True
        else:
            return False

    def get_metadata(self, value):
        """
        """

        metadata = {
                'title':    'xesam:title',
                'artist':   'xesam:artist',
                'album':    'xseam:album',
                'track':    'xesam:trackNumber',
                'uri':      'xesam:url',
                'created':  'xesam:contentCreated',
                'disc':     'xesam:discNumber',
                'length':   'mpris:length',
                'trackid':  'mpris:trackid', 
                'artUrl':   'mpris:artUrl', }
        
        if value in metadata:
            try:
                return self.player.GetMetadata().get(metadata[value])
            except DBusException:
                print("value not found %s " % e.get_dbus_message())


        elif meta == 'formatlength':
            secs = int(self.get_meta('length')) / 1000000
            return  "%d:%02d" % ( secs/60, secs%60)

        elif meta == 'url':
            try:
                return 'http://open.spotify.com/track/' + self.get_meta('trackid').split(':')[2]
            except:
                print ("Track url not found:",e)
        else:
            return False

