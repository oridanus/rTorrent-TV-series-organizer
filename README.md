# rTorrent-TV-series-organizer
Automatically organize your TV series downloads from rTorrent, to Kodi's directory structure.

## Installation

* install [OSMC](https://osmc.tv/) 

* install rTorrent + ruTorrent, use this [wondeful script](https://github.com/Kerwood/Rtorrent-Auto-Install)

  * isntall the base rtorrent 
  * install RSS plugin, with the plugin installation of the script.

* use [showRSS](http://new.showrss.info/) - to generate a feed with your favorite shows

* configure the feed in your rTorrent - to download everything, with this regular expression - /()/i

![alt tag](https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/Screen%20Shot%202016-03-11%20at%2012.40.54%20PM.png)

* use the [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) to specify where the tv shows is downloaded to:

```python
# Default directory to save the downloaded torrents.
directory = /mnt/500g/TV-Series/unsorted
```

* confugre the last line of [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) for your directory sturcture. it tells rtorrent to call [copy-episode.py](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/copy-episode.py) script on compeltion of each download. 

```python
system.method.set_key = event.download.finished,mycommand, "execute = /usr/bin/python, /home/osmc/organizer/copy-episode.py, $d.get_base_path=, /mnt/500g/TV-Series"
```
1st argument = the directory that just finished downloading.
2nd argument = the destination TV series root directory.

The script parses the file name and copies it to the apropriate series directory. it scans for mkv files.


