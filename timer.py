#!/usr/bin/env python
"Print current time and remaining time"
import art
import os
import datetime
import time
import argparse

RTHF   = argparse.RawTextHelpFormatter
PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=RTHF)
PARSER.add_argument('hour', help='hour goal', type=int)
PARSER.add_argument('minute', help='minute goal', type=int)
PARSER.add_argument('second', help='second goal', nargs='?', type=int, default=0)
ARGS  = PARSER.parse_args()

goal = datetime.datetime.now()
goal = datetime.datetime.now().replace(hour=ARGS.hour, minute=ARGS.minute, second=ARGS.second)

while True:
    now = datetime.datetime.now()
    delta = goal - now
    minutes = (delta.seconds // 60)
    seconds = (delta.seconds - 60 * minutes)
    os.system('clear')
    art.tprint(now.strftime("%H:%M:%S"), font='big')
    art.tprint('es bleiben', font='big')
    art.tprint(f'{minutes}min {seconds}s', font='big')
    time.sleep(1)
