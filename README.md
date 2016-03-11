# rTorrent-TV-series-organizer
automatically organize your TV series downloads from rTorrent, to Kodi's directory structure

## Installation

install [OSMC](https://osmc.tv/) 

install rTorrent + ruTorrent, use this [wondeful script](https://github.com/Kerwood/Rtorrent-Auto-Install)

also install RSS plugin, with the plugin installation of the script.

use [showRSS](http://new.showrss.info/) - to generate a feed with your favorite shows

configure the feed in your rTorrent - to download everything, with this regular expression - /()/i

![alt tag](https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/Screen%20Shot%202016-03-11%20at%2012.40.54%20PM.png)

use the [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) to specify where the tv shows is downloaded to.

the last line of [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) calls a python script on compeltion of download. it parses the file name and copies it to the apropriate series directory. currently scans for mkv files.


