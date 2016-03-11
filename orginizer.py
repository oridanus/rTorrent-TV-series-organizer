import os
import string
import shutil
import datetime
import sys


#----------------------------------------------------------------------------------#
# start logging
log_file="E:\\\\auto-extractor-log.txt"
logfile = open(log_file, \'a\')

now = datetime.datetime.now()
now_string = now.strftime("%Y-%m-%d %H:%M:%S")
logfile.write("-----------------------------------------------------------------------------------------------------------------\
")

logfile.write(now_string + " new file found in unsorted directory\
")
#----------------------------------------------------------------------------------#


#--------------------------------------------------------------#
# building the string for the path of source file to move
source_dir = "E:\\TEMP\\Unsorted"
try:
    episode = os.listdir(source_dir)[0]
except IndexError:
    logfile.write(now_string + " there is no file in the unsorted dir, maybe unrar was unsuccessful - exiting\
")
    logfile.write("=================================================================================================================\
")
    logfile.close()
    sys.exit()

source_file = source_dir + "\\\\" + episode

#--------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------#
# building the string for the path of the dest folder to move the source file into

series_base_dir = "E:\\TV Series"

dest_series_with_dots = episode[:episode.rfind(\'.S\')]
dest_series_without_dots = dest_series_with_dots.replace("."," ")
dest_series_dir = series_base_dir + \'\\\\\' + dest_series_without_dots

# check if the dir really exist ( parsing succedded )
try:
    os.chdir(dest_series_dir)
except:
    # ok , so we will try to parse with lower case \'s\'
    dest_series_with_dots = episode[:episode.rfind(\'.s\')]
    dest_series_without_dots = dest_series_with_dots.replace("."," ")
    dest_series_dir = series_base_dir + \'\\\\\' + dest_series_without_dots
    try:
        os.chdir(dest_series_dir)
    except:
        no_match_dir="E:\\\\TEMP\\\
o_match"
        logfile.write("parse error - there is no dir named " + dest_series_dir +"\
")
        logfile.write("moving the file to " + no_match_dir + " directory in order to stay with clean unsorted dir\
")
        shutil.move(source_file,no_match_dir)
        logfile.write("=================================================================================================================\
")
        logfile.close()
        sys.exit()



# returns the last in the array sorted alphbeticly, i.e : season 5 is after season 2 alphbeticlly.
# pop gives the last value in the array .

latest_season_dir=os.listdir(dest_series_dir).pop()
dest_dir=dest_series_dir + "\\\\" + latest_season_dir
#------------------------------------------------------------------------------------------------------#


#----------------------------------#
# moving the file
try:
    shutil.move(source_file,dest_dir)
except:
    logfile.write("the file:\
   " + source_file + "\
could not be moved to the directory:\
   "+ dest_dir + "\
")
    logfile.write("maybe already exists there?\
")
    os.remove(source_file)
    logfile.write("the file has been removed ( rar files still there in completed dir... )\
")
    logfile.write("=================================================================================================================\
")
    logfile.close()
    sys.exit()

#----------------------------------#
# end logging
now = datetime.datetime.now()
now_string = now.strftime("%Y-%m-%d %H:%M:%S")
logfile.write(now_string + " the file:\
   " + source_file + "\
was moved to directory:\
   " + dest_dir + "\
")
logfile.write("=================================================================================================================\
")
logfile.close()')
