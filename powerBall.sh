#!/bin/bash

# Fuck the powerball. You're never gonna win at this shit.
# But I can't quit buying tickets.

# -s is for silent
# -L is for the case in which the web address has moved
# grep numbers something like ">9<" or ">24<" -- the source code makes this obvious
#
# fuck awk -- how do you use this shit? I just decided to pipe to another awk
# using '<' and '>' as delimiters

curl -s -L powerball.com | grep '>[0-9][0-9]*<' | awk -F'>' 'BEGIN{OFS=" ";} {print $2}' | awk -F'<' 'BEGIN{OFS=" ";} {print $1}'