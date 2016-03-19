# rTorrent TV Series Organizer
Automatically organize your TV series downloads from rTorrent, to [Kodi](https://kodi.tv/)'s directory structure.

![alt tag](http://i.imgur.com/wrpYku8.jpg)


## Installation

* Install [OSMC](https://osmc.tv/), or any other kodi enviroment as you wish.

* Install rTorrent + ruTorrent, use this [wondeful script](https://github.com/Kerwood/Rtorrent-Auto-Install)

  * Install the base rtorrent 
  * Install RSS plugin, with the plugin installation of the script.

* Use [showRSS](http://new.showrss.info/) - to generate a feed with your favorite shows

* Configure the feed in your rTorrent - to download everything, with this regular expression - /()/i

![alt tag](https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/Screen%20Shot%202016-03-11%20at%2012.40.54%20PM.png)

* Use the [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) to specify where the tv shows are downloaded to:

```ruby
# Default directory to save the downloaded torrents.
directory = /mnt/500g/TV-Series/unsorted
```

* create a dir for the organizer
```bash
mkdir /home/osmc/organizer
```

* download the 
```bash
cd /home/osmc/organizer
wget https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/copy-episode.py
```

* install [parse-torrent-name](https://pypi.python.org/pypi/parse-torrent-name/0.1.0) python package
```bash
pip install parse-torrent-name
```

* Confugre the last line of [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) for your directory sturcture. it tells rtorrent to call [copy-episode.py](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/copy-episode.py) script on completion of each download. 

 ```python
system.method.set_key = event.download.finished,mycommand, "execute = /usr/bin/python, /home/osmc/organizer/copy-episode.py, $d.get_base_path=, /mnt/500g/TV-Series"
```
  * 1st argument = the directory that just finished downloading.
  * 2nd argument = the destination TV series root directory, that Kodi knows.
  * The script parses the file name and copies it to the appropriate series directory. it scans for mkv files in the downloaded directory.


