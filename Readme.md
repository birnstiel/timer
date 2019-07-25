# Simple terminal timer

Terminal timer refreshing every second. Will print the time and remaining time. For details, call the help with

	python timer.py -h

--------

	usage: timer.py [-h] [-d DURATION] [-f FONT] [-r RATE]
			[hour] [minute] [second]

	Print current time and remaining time

	positional arguments:
	  hour                  hour goal
	  minute                minute goal
	  second                second goal

	optional arguments:
	  -h, --help            show this help message and exit
	  -d DURATION, --duration DURATION
				duration in minutes
	  -f FONT, --font FONT  art package font
	  -r RATE, --rate RATE  refresh every RATE seconds
