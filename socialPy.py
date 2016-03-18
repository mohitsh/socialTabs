#!/usr/bin/env python3

import sys,pyperclip,webbrowser

def opentab(link):
    if link == 'f':
        webbrowser.open('https://www.facebook.com')
    elif link == 'm':
         webbrowser.open('https://mail.google.com')
    elif link == 'y':
         webbrowser.open('https://www.youtube.com')
    elif link == 'taz':
        webbrowser.open('https://www.youtube.com/watch?v=a18py61_F_w')
    
arguments = sys.argv[1:]
print(arguments)
if len(arguments)==1:
    dude, = arguments
    opentab(dude)
elif len(arguments) > 1:
    for link in arguments:
        opentab(link)
else:
     ls = ['m','f','y','taz']
     for elem in ls:
         opentab(elem)


