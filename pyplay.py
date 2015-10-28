# PyPlay radio playout script by Giles Booth @blogmwiki
# written in Python2 to run on MacOS X without installing Python3
# only works in OS X as uses afplay to play audio files
# requires an M3U playlist file called playlist.m3u and audio files in same directory

import os
import time
import subprocess
import re
import datetime

playlist = ""

# \033[7m is code for inverse video
# \033[0m is normal video
# \033[31m is red video

# function to display tracks, durations, playing status & out time
def showTracks():
    os.system('clear')
    t = str(datetime.datetime.now().time())
    t = t[0:8]
    print '\033[37;44mWelcome to PyPlay!\t\t\t',t,'\033[0m'
    print ""
    print '\033[0;30;47m# Track                 Length  Status  Out time \033[0m'
    for z in range(len(trackList)):
        highlightOn = ""
        highlightOff = ""
        if "PLAYING" in trackList[z][4]:
            highlightOn = "\033[31;103m"
            highlightOff = "\033[0m"
        print highlightOn, z+1, trackList[z][1], "\t", trackList[z][3], "\t", trackList[z][4], highlightOff
    print 'Press ctrl+c to stop playing, q to quit'

# returns a float with duration of track in seconds
def getTrackLength(thing):
    bumf = ""
    bumfList = []
    trackLength = ""
    snog = trackArray[thing]
    foo = "afinfo " + snog
    bumf = subprocess.check_output(foo, shell=True)
    bumfList = bumf.split('\n')
    for line in bumfList:
        if line.startswith('estimated duration'):
            duration = line
    trackLength = re.findall(r"[-+]?\d*\.\d+|\d+", duration)
    trackSecs = float(trackLength[0])
    return trackSecs

# returns string with out time in HH:MM:SS format
def getEndTime(tk):
    tkDuration = trackList[tk-1][2]
    timeNow = str(datetime.datetime.now().time())
    timeHour = timeNow[0:2]
    timeMin = timeNow[3:5]
    timeSec = timeNow[6:8]
    tH = int(timeHour)
    tM = int(timeMin)
    tS = int(timeSec)
    tkS = tkDuration % 60
    tkM = (tkDuration - tkS) / 60
    endSec = int(round(tS+tkS, 0))
    endMin = int(tM + tkM)
    endHour = int(tH)
    if endSec > 59:
        endMin += 1
        endSec = endSec % 60
    endHourString = leadingZero(str(endHour))
    endMinString = leadingZero(str(endMin))
    endSecString = leadingZero(str(endSec))
    endTime = endHourString + ":" + endMinString + ":" + endSecString
    return str(endTime)

# adds a leading 0 to single character strings
def leadingZero(n):
    if len(n) == 1:
            n = '0' + n
    return n

# makes strings a fixed length
def colform(txt, width):
    if len(txt) > width:
        txt = txt[:width]
    elif len(txt) < width:
        txt = txt + (" " * (width - len(txt)))
    return txt

# returns the track length in a string M:SS format
def displayDuration(s):
    disTime = int(s)
    sec = disTime % 60
    m = (disTime - sec)/60
    secString = leadingZero(str(sec))
    # if len(secString) == 1:
    #    secString = '0' + secString
    t = str(m) + ":" + secString
    return t

# sets playing status for all tracks to empty string
def clearStatus():
    for y in range(len(trackList)):
        trackList[y][4] = ''

# plays the track using OS X afplay command
# You could try VLC or MPD if using Linux
def playTrack(track):
    song = trackArray[track-1]
    trackString = "afplay " + song
    os.system(trackString)

#open the playlist file and read its contents into a list
playlist = open('playlist.m3u')
trackArray = playlist.readlines()

# clean up the track list array of metadata and \n characters
# iterate over list in reverse order as deleteing items from list as we go
for i in range(len(trackArray)-1,-1,-1):
    if trackArray[i].startswith('\n') or trackArray[i].startswith('#'):
        trackArray.pop(i)
    temp = trackArray[i].strip()
    trackArray[i] = temp

# read tracks into array to hold track info in format:
# filename - display name - duration as float - display duration - track status
trackList = []
for a in range(len(trackArray)):
    trackList.append([trackArray[a],colform(trackArray[a],15),getTrackLength(a),displayDuration(getTrackLength(a)),"status"])

while True:
    clearStatus()
    showTracks()
    trackNo = raw_input('\nWhich track would you like to play? ')
    if trackNo == 'q':
        break
    elif trackNo == "":
        print 'You must enter a track number or q to quit'
        time.sleep(2)
    elif trackNo.isalpha():
        print 'Must be a number'
        time.sleep(2)
    elif int(trackNo) <1 or int(trackNo) > len(trackArray):
        print 'Not a valid track number'
        time.sleep(2)
    else:
        eT = getEndTime(int(trackNo))
        trackList[int(trackNo)-1][4] = 'PLAYING ' + eT
        showTracks()
        playTrack(int(trackNo))
