# PyPlay
A Python radio/theatre audio player for Macs by Giles Booth / @blogmywiki

PyPlay is designed to play audio files off a Mac one at a time, and tell you at what clock time it will finish playing. This is useful if you're working in radio or theatre and want to play sound files singly, waiting for a the operator to play in the next file manually on cue. It's inspired by the Windows application CoolPlay.

It is a really simple, but not-entirely-trvial, program that I made whilst teaching myself Python.

See http://www.suppertime.co.uk/blogmywiki/2015/04/coolplaymac/ for more information on CoolPlay and how to run it on a Mac.

It only works on Mac OS X - why?
--------------------------------
If you're running Windows, use CoolPlay which is like, way better.

PyPlay uses the OS X **afplay** (audio file play) command, so if you're on Linux, you'll need to edit the code to use VLC, MPD or some other audio player. Using **afplay**, however, means it can play **any** format of audio file your Mac can play: MP3s, WAVs, AIFFs, M4As etc.

It's written in Python 2 - this is because Macs have Python 2 installed by default, and I want this to work without anyone having to install any extra software like Python 3 or a launcher.

How to use it
-------------
Put the PyPlay script **pyplay.py** in the same folder as your audio files. It uses an M3U playlist file called playlist.m3u in the same folder - this is a standard playlist format used by lots of software like iTunes, VLC and indeed CoolPlay. It's just a text file that starts #EXTM3U and then has a list of file names like this:

    #EXTM3U

    Computers.mp3
    Dijjeridoo.mp3
    DripDrop.mp3
    Firework.mp3
    Typing.mp3

If you don't already have an M3U playlist file, this version of PyPlay will scan the directory you're in and make one from any MP3, WAV, M4A and AIFF files it finds. (You can add more file types in the **audioFileTypes** list in line 121). This version also fixes a bug playing file names with spaces in and corrects a bug where the out-time crossed the top of an hour.

You need to run PyPlay from the OS X Terminal by navigating to the directory where it and your audio files are. If you can't work out the path to the folder, find the folder in the Mac Finder, type `cd ` (space after cd) in the Terminal and drag the folder into the Terminal window, then press enter. Then type `python pyplay.py` to run it.

![PyPlay window](http://www.suppertime.co.uk/pyplay/pyplay.png)

The program runs in a little terminal window. You enter a number to pick the track you want to play, it plays it and displays the 'out time' - the clock time when it will finish playing.

It will probably play long files but the display won't cope very well with audio files longer than an hour and the out times may be wrong.

You can break out of playing a track by pressing ctrl-c, and close PyPlay by typing 'q' instead of a track number.

Changes
-------
- Bug replacing multiple spaces in filenames fixed in version 4
- Bug handling apostrophes in filenames fixed in version 4

To do list
----------
- ~~Have PyPlay make a playlist file from all the audio files in the directory if one isn't already there.~~
- Handle long audio files in display better.
- Error handling if no audio files found.
- Have a much more CoolPlay-like interface where you scroll up and down a list to select which track plays next, possibly just by pressing the space bar.
- Have a 'cartwall' mode where you press a key and it plays a file immediately.
- Some clever threading to show elapsed / remaining time of playing track and have on-screen clock update.
- Make it work with relative or absolute file paths outside its directory. (May already work, I haven't tried it)
- Allow editing of playlists.
- Package it up so you drop it in the folder and run it from the Finder.
- GUI. Yeah, right.
