# -*- coding: utf-8 -*-
import urllib, xbmc, xbmcgui, xbmcplugin, sys

def Youtubechannel(channelname):
	xbmc.executebuiltin('XBMC.Container.Update(plugin://plugin.video.youtube/channel/{0}/)'.format(channelname))

def get_params():
    param_string = sys.argv[2]
    
    commands = {}

    if param_string:
        split_commands = param_string[param_string.find('?') + 1:].split('&')
    
        for command in split_commands:
            if len(command) > 0:
                if "=" in command:
                    split_command = command.split('=')
                    key = split_command[0]
                    value = urllib.unquote_plus(split_command[1])
                    commands[key] = value
                else:
                    commands[command] = ""
    return commands

def addDir(name,url,mode,iconimage,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
	if mode==1:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
	elif mode==3 or mode==5 or mode==9 or mode==14:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	
params = get_params()
mode = params.get("mode")
if mode==None:
	addDir('Le Télévidéographe','plugin://plugin.video.youtube/channel/UCHPPL2dju56vT8dHtnFbbiA ',1,'https://i.imgur.com/FJbULPm.png','')

else:
	Youtubechannel('UCHPPL2dju56vT8dHtnFbbiA')

xbmcplugin.endOfDirectory(int(sys.argv[1]))