import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'program')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
elif mode[0] == 'on':
    xbmcgui.Dialog().ok('Vpn on', 'message')
elif mode[0] == 'off':
    xbmcgui.Dialog().ok('Vpn off', 'message')

url = build_url({'mode': 'on'})
li = xbmcgui.ListItem('Vpn on', iconImage='DefaultFolder.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
xbmcplugin.endOfDirectory(addon_handle)
