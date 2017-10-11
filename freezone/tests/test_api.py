from freezone import api
from pprint import pprint
import os

def test_get_stuff():
    fz = api.Freezone()
    print
    print 'get_root_channels:', fz.get_root_channels()
    # root_radio seems to return same channel list as root list above?
    print 'get_root_radio_channels', fz.get_root_radio_channels()
    print 'get_freezone_partners', fz.get_freezone_partners()
    print 'get_abc_iview', fz.get_abc_iview()
    print 'get_currently_watched', fz.get_currently_watched()
    print 'get_whats_live', fz.get_whats_live()
    print 'get_live', fz.get_live()
    print 'get_most_recent', fz.get_most_recent()

def test_play_a_video():
    fz = api.Freezone()
    a_video_id = 22681
    video = fz.get_video(a_video_id)
    print video
    media = video.media[0]
    #os.popen('vlc %s' % media.hls)
    os.popen('vlc %s' % media.raw)

def test_walk_navigation():
    """Walk the entire heirarcy of categories and print every item"""
    fz = api.Freezone()
    nav = fz.get_navigation()

    def walk_nav(ch, level):
        print ' '*level, ch
        for c in ch.subcats:
            walk_nav(c, level+1)
        if not ch.subcats:
            for i in fz.get_channel(ch.link).items:
                print ' '*level, i

    for c in nav:
        walk_nav(c, 0)


