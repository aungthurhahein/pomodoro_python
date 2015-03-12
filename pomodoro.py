#!/usr/bin/env python
"""
# pomodor timer
# usage: to save our fingers, hard coding with standard parameters for pomodoro techniques
#        change as you prefer at #parameters section
# Dev: Aung
# Date: 28122014
"""

from subprocess import call
import time
import sys

# parameters in minutes
duration = 25  # duration of 1 pomodoro
short_brk = 5  # short break duration
long_brk = 15  # long break duration
One_pomodori = 4  # for 1 pomodori, how many number of pomodoros
duration_count = duration

# audio vairable
file_path = sys.path[0] # the absolute file path of this script
chime_short = file_path + "/chime/chime.mp3"  # short break
chime_long = file_path + "/chime/chime2.mp3"  # long break
chime_pomodoro = file_path + "/chime/chime3.mp3"  # pomodoro tone


def pomodoro(one_pomodori, short_brk, long_brk, duration, duration_count):
    for i in range(1,one_pomodori):
        duration = duration_count
        while duration > 0:
            call("clear", shell=True)
            print "%d min working..." % int(duration_count - duration)
            time.sleep(60)
            duration -= 1

        # short break
        call("play " + chime_short, shell=True)
        call("clear", shell=True)
        print "Take short %d min break" % short_brk
        time.sleep(60*int(short_brk))

        call("play " + chime_short, shell=True)
        call("clear", shell=True)
        print "Back to work..."

    # long break
    call("play " + chime_long, shell=True)
    call("clear", shell=True)
    print "Well done.Take long %d min break" % long_brk
    time.sleep(60*int(long_brk))
    call("play " + chime_long, shell=True)

def wrapper():
    pomodoro(One_pomodori, short_brk, long_brk, duration, duration_count)
    call("play " + chime_pomodoro, shell=True)
    print("A pomodori finished. Again?(y/n)")

    encore = raw_input(">")
    if encore == "y":
        wrapper()
    elif encore == "n":
        exit(0) # tada
    else:
        print "I dont't get that one.Try again"

if __name__ == "__main__":
    wrapper()
