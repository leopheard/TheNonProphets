from xbmcswift2 import Plugin, xbmcgui
from resources.lib import thenonprophets

plugin = Plugin()

URL = "https://www.spreaker.com/show/3254964/episodes/feed"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/icon.png"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/icon.png"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = thenonprophets.get_soup(URL)
    
    playable_podcast = thenonprophets.get_playable_podcast(soup)
    
    items = thenonprophets.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = thenonprophets.get_soup(URL)
    
    playable_podcast1 = thenonprophets.get_playable_podcast1(soup)
    
    items = thenonprophets.compile_playable_podcast1(playable_podcast1)

    return items



if __name__ == '__main__':
    plugin.run()
