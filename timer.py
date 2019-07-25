#!/usr/bin/env python
"Print current time and remaining time"
import art
import os
import datetime
import time
import argparse

RTHF   = argparse.RawTextHelpFormatter
PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=RTHF)
PARSER.add_argument('hour', help='hour goal', nargs='?', type=int, default=0)
PARSER.add_argument('minute', help='minute goal', nargs='?', type=int, default=0)
PARSER.add_argument('second', help='second goal', nargs='?', type=int, default=0)
PARSER.add_argument('-d', '--duration', help='duration in minutes', type=int, default=0)
PARSER.add_argument('-f', '--font', help='art package font', type=str, default='big')
PARSER.add_argument('-r', '--rate', help='refresh every RATE seconds', type=float, default=1)
ARGS  = PARSER.parse_args()

if ARGS.duration > 0:
    goal = datetime.datetime.now() + datetime.timedelta(minutes=ARGS.duration)
else:
    goal = datetime.datetime.now().replace(hour=ARGS.hour, minute=ARGS.minute, second=ARGS.second)

delta = goal - datetime.datetime.now()

while delta.seconds > 0:
    now = datetime.datetime.now()
    delta = goal - now
    minutes = (delta.seconds // 60)
    seconds = (delta.seconds - 60 * minutes)
    os.system('clear')
    art.tprint(now.strftime("%H:%M:%S"), font=ARGS.font)
    art.tprint('es  bleiben', font=ARGS.font)
    art.tprint(f'{minutes}min {seconds}s', font=ARGS.font)
    time.sleep(ARGS.rate)

os.system('clear')
art.tprint('GAME OVER', font=ARGS.font)
