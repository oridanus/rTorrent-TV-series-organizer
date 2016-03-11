# rTorrent-TV-series-organizer
Automatically organize your TV series downloads from rTorrent, to Kodi's directory structure.

## Installation

* Install [OSMC](https://osmc.tv/), or any other kodi enviroment as you wish.

* Install rTorrent + ruTorrent, use this [wondeful script](https://github.com/Kerwood/Rtorrent-Auto-Install)

  * Install the base rtorrent 
  * Install RSS plugin, with the plugin installation of the script.

* Use [showRSS](http://new.showrss.info/) - to generate a feed with your favorite shows

* Configure the feed in your rTorrent - to download everything, with this regular expression - /()/i

![alt tag](https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/Screen%20Shot%202016-03-11%20at%2012.40.54%20PM.png)

* Use the [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) to specify where the tv shows is downloaded to:

```python
# Default directory to save the downloaded torrents.
directory = /mnt/500g/TV-Series/unsorted
```

* Confugre the last line of [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) for your directory sturcture. it tells rtorrent to call [copy-episode.py](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/copy-episode.py) script on compeltion of each download. 

 ```python
system.method.set_key = event.download.finished,mycommand, "execute = /usr/bin/python, /home/osmc/organizer/copy-episode.py, $d.get_base_path=, /mnt/500g/TV-Series"
```
  * 1st argument = the directory that just finished downloading.
  * 2nd argument = the destination TV series root directory.
  * The script parses the file name and copies it to the apropriate series directory. it scans for mkv files.


