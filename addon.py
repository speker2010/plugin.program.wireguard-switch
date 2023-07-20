import sys
import urllib
from urllib.parse import parse_qs
from urllib.parse import urlencode
import xbmcgui
import xbmcplugin

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'program')

def build_url(query):
    return base_url + '?' + urlencode(query)

mode = args.get('mode', None)

if mode is None:
    print('Hi')
elif mode[0] == 'on':
    xbmcgui.Dialog().ok('Vpn on', 'message')
elif mode[0] == 'off':
    xbmcgui.Dialog().ok('Vpn off', 'message')

url = build_url({'mode': 'on'})
li = xbmcgui.ListItem('Vpn on')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)


url = build_url({'mode': 'off'})
li = xbmcgui.ListItem('Vpn off')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

xbmcplugin.endOfDirectory(addon_handle)
