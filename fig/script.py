#!/usr/bin/env python
import sys
import os

if __name__ == "__main__":

    os.system("ls -1 | grep eps$ > lst")
    files = [x.strip() for x in open("lst","r").readlines()]
    print files

    for f in files:
        radical = f.split(".")[0]
        try:
            os.system("ps2pdf %s.eps" % radical)
            os.system("pdf2svg %s.pdf svg/%s.svg" % (radical,radical))
            print "converted %s" % f
        except:
            print "could not convert %s" % f
