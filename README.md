### Simple Terminal Pomodoro timer 

This is a simple pomodoro timer written with Python 2.x and tested at debian system.

#### Usage
    python pomodoro.sh

After 1 pomodori, it will ask for the user to start another cycle.

Before and after short and long break, it will give you a short notification tone if you are working away from termial.

#### Requirements

* Python 2.x

* For sound notification, it is necessary to install <a href="http://sox.sourceforge.net/">sox</a>.

    $ sudo apt-get install sox libsox-fmt-all

#### settings
To change the default parameters, please edit the *parameters* section at pomodoro.py file.

To change notification tone, put any mp3 files and replace with default files:

    * chime.mp3: short break tone
    * chime2.mp3: long break tone
    * chime3.mp3: pomodori finished tone
    
#### Recommendation

Clone this git at /home/user/ directory and put the pomodoro.sh wrapper to /bin directory and call it from terminal as 
    
    $ pomodoro.sh 

#### Extended work on this project

It sends short and long breaks through twitter direct message channel.
Take a look at https://github.com/akaes/Pomodoro/blob/master/readme_en_pomodoro_std.md
  

