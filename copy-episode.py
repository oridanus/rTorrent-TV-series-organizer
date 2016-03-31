import PTN
import os
import sys
import shutil
from time import gmtime, strftime
import time
import commands
from distutils.dir_util import mkpath

log_file = open('/var/log/copy-episode.log', 'a')
log_file.write('====== STARTING ========= ' + strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ========================================================================\n')
episode_dir = sys.argv[1]
log_file.write('|  Source episode directory     = ' + episode_dir + "\n")

episode_full_path = os.path.join(episode_dir, [f for f in os.listdir(episode_dir) if f.endswith('.mkv')][0])
base_series_dest_dir = sys.argv[2]
log_file.write('|  Detention TV Shows directory = ' + base_series_dest_dir + "\n")

episode_file = os.path.basename(episode_full_path)
parse_results = PTN.parse(episode_file)
dest_dir  = os.path.join(base_series_dest_dir, parse_results['title'], 'Season ' + str(parse_results['season']))
dest_path = os.path.join(dest_dir, episode_file)

log_file.write('|       Copying\n|  ' + episode_full_path + '\n|       To\n|  ' + dest_path + '\n') 
mkpath(dest_dir)
shutil.copyfile(episode_full_path , dest_path)

log_file.write("|  Refreshing Kodi...\n")

commands.getstatusoutput("/usr/bin/kodi-send --host=127.0.0.1 --port=9777 --action=\"UpdateLibrary(video)\"")

log_file.write('======= DONE ============ ' + strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ========================================================================\n')

log_file.close()
