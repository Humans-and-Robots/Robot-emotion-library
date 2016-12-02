#!/usr/bin/python
#!/bin/bash
# tinylcd35 test program v2
# Texy 12/1/2014
# press UP ans SELECT buttons at the same time to quit
import sys, os, time
#import scipy
#from scipy import ndimage
#from scipy import misc

def main(emotion, display):
#    hello = scipy.misc.imread("test.png")
#    print hello
#    print "end of prog1"
    emodeg = emotion + repr(display)
    os.system("sudo killall -9 fbi")
    os.system("sudo fbi -T 2 -d /dev/fb0 -noverbose -a images/" + emodeg + ".png")

if __name__ == '__main__':
    main(emotion, display)

