# PyPlay
A Python radio/theatre audio player for Macs

PyPlay is designed to play audio files off a Mac one at a time, and tell you what clock time it will finish playing. This is useful if you're working in radio or theatre and want to play sound files singly, waiting for a the operator to play in the next file manually on cue. It's inspired by the Windows application CoolPlay.

It only works on Mac OS X.
Why?
If you're running Windows, use CoolPlay which is much better.
It uses the OS X afplay command, so if you're on Linux, you'll need to edit the code to use VLC, MPD or some other audio player. Using afplay, however, means it can play any audio file your Mac can play.

It's written in Python 2 - this is because Macs have Python 2 installed by default, and I want this to work without anyone having to install any extra software like Python 3 or a launcher.

How to run it:
Put the PyPlay script in the same folder as your audio files. You also need to have an M3U playlist file called playlist.m3u in the same folder - this is a standard playlist format used by lots of software. It's just a text file that starts #EXTM3U and then has a list of file names like this:

    #EXTM3U

    Computers.mp3
    Dijjeridoo.mp3
    DripDrop.mp3
    Firework.mp3
    Typing.mp3


To do list:
- Have PyPlay make a playlist file from all the audio files in the directory if one isn't already there.
- Have a much more CoolPlay-like interface where you scroll up and down a list to select which track plays next.
- Some clever threading to show elapsed / remaining time of playing track and have on-screen clock update.
- Make it work with relative file paths.
- Allow editing of playlists.
- Package it up so you drop it in the folder and run it from the 
- GUI. Yeah, right.
