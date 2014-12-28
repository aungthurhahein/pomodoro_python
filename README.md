### Simple Terminal Pomodoro timer 

This is a simple pomodoro timer written with Python 2.x and tested at debian system. 

#### Usage
python pomodoro.sh

After 1 pomodori, it will ask for another cycle.

#### Requirements

Python 2.x

For sound notification, it is necessary to install <a href="http://sox.sourceforge.net/">sox</a>.

$ sudo apt-get install sox libsox-fmt-all

#### settings
To change the default parameters, please see the parameters section at pomodoro.py.

To change notification tone, put any mp3 files and replace with default files:

    * chime.mp3: short break tone
    * chime2.mp3: long breack tone
    * chime3.mp3: pomodori finished tone
    
#### Recommendation

Clone this git at /home/user/ directory and put the pomodoro.sh wrapper to /bin directory.

 

