# rTorrent TV Series Organizer
Automatically organize your TV series downloads from rTorrent, to [Kodi](https://kodi.tv/)'s directory structure.

![alt tag](http://i.imgur.com/wrpYku8.jpg)


## Installation

* Install [OSMC](https://osmc.tv/), or any other kodi enviroment you wish. 
  rtorrent is not maintanted anymore so the versions that works for me are [OSMC 2017-06](http://download.osmc.tv/installers/diskimages/OSMC_TGT_rbp2_20170705.img.gz) with rtorrent Rtorrent-Auto-Install-4.0.0-Debian-Wheezy

* Install rTorrent + ruTorrent, use this [wondeful script](https://github.com/Kerwood/Rtorrent-Auto-Install)

  * Install the base rtorrent 
  * Install RSS plugin, from the plugin installation menu.

* Use [showRSS](http://new.showrss.info/) - to generate a feed with your favorite shows
* Browse to rTorrent from your browser ([your-ip]/rutorrent) and add the showRSS feed you created

* Configure the feed in your rTorrent - to download everything, with this regular expression -
 ```ruby
 /()/i
 ```

![alt tag](https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/Screen%20Shot%202016-03-11%20at%2012.40.54%20PM.png)

* Create a dir for the organizer
 ```bash
 mkdir /home/osmc/organizer
 ```

* Download the [copy-episode.py](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/copy-episode.py) script
 ```bash
 cd /home/osmc/organizer
 wget https://raw.githubusercontent.com/oridanus/rTorrent-TV-series-organizer/master/copy-episode.py
 chmod 777 copy-episode.py
 ```

* Install [parse-torrent-name](https://pypi.python.org/pypi/parse-torrent-name/0.1.0) python package (if you don't have pip yet installed, [here](https://pip.pypa.io/en/stable/installing) is the how-to)
 ```
 pip install parse-torrent-name
 ```

* Configure in [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc) where the tv shows are downloaded to:

 ```
 # Default directory to save the downloaded torrents.
 directory = /mnt/500g/TV-Series/unsorted
 ```

* Configure the event to trigger when a download finishes in [.rtorrent.rc](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/.rtorrent.rc). It tells rtorrent to call [copy-episode.py](https://github.com/oridanus/rTorrent-TV-series-organizer/blob/master/copy-episode.py) script on completion of each download.

```
system.method.set_key = event.download.finished,mycommand, "execute = /usr/bin/python, /home/osmc/organizer/copy-episode.py, $d.get_base_path=, /mnt/500g/TV-Series"
```
  * 1st argument = the directory that just finished downloading.
  * 2nd argument = the destination TV series root directory, this one is configured in Kodi as the TV shows dir.
  * The script scans for mkv files in the downloaded directory, parses the file name and copies it to the appropriate TV show directory:
  
  
```
    TV Shows                  <<Source folder, Content: TV shows>>
   |----TV Show 1
   |       |----Season #
   |            |--Files
```

  * After copying - the script updates the Kodi's library, so your fresh episode is ready to watch in one click!

* Log file can be found in /var/log/copy-episode.log


```
  osmc@pi:~$ tail -9 /var/log/copy-episode.log
====== STARTING ========= 2016-03-31 18:07:07 ========================================================================
|  Source episode directory     = /mnt/500g/TV-Series/unsorted/The.Americans.2013.S04E03.720p.HDTV.x264-KILLERS[rarbg]
|  Destination TV Shows directory = /mnt/500g/TV-Series
|       Copying
|  /mnt/500g/TV-Series/unsorted/The.Americans.2013.S04E03.720p.HDTV.x264-KILLERS[rarbg]/The.Americans.2013.S04E03.720p.HDTV.x264-KILLERS.mkv
|       To
|  /mnt/500g/TV-Series/The Americans/Season 4/The.Americans.2013.S04E03.720p.HDTV.x264-KILLERS.mkv
|  Refreshing Kodi...
======= DONE ============ 2016-03-31 18:14:35 ========================================================================

```

## Tips and Tricks

* Mounting an SMB drive (for example connected to a router and shared), edit /etc/fstab
  ```bash
 //192.168.1.1/volume(sda1)/ /mnt/500g cifs noauto,x-systemd.automount,username=name,password=name,uid=1000,gid=1000,iocharset=utf8 0 0
 ```

* Adding an alias called "log" to show the last episode downloaded from the log, edit ~/.bashrc
  ```
  alias log='tail -9 /var/log/copy-episode.log'
  ```
* Show the last episode downloaded automaticly when you open the terminal, add this in the end of your ~/.bashrc  
  ```
  log
  ```

