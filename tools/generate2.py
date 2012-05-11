#!/usr/bin/python
#
# Run from trunk directory like this:
# trunk$ python tools/generate.py

import fontforge
import os
import sys
from fontTools.ttLib import TTFont

def getHeights(font):
    # ymax + ymin, using the later as an overshoot
    xHeight = font['x'].boundingBox()[3] + font['x'].boundingBox()[1]
    cHeight = font['H'].boundingBox()[3] + font['H'].boundingBox()[1]

    return int(xHeight), int(cHeight)

def generate(font, path):
    extension = os.path.splitext(outfilepath)[1]

    font.selection.all()
    font.autoHint()

    if extension == '.ttf':
        font.em = 1024
        font.round()

    tmp_path = '%s.tmp%s' %(path, extension)

    font.generate(tmp_path)

    tmp_font = TTFont(tmp_path)
    tmp_font['OS/2'].sxHeight, tmp_font['OS/2'].sCapHeight = getHeights(font)
    tmp_font.save(path)
    tmp_font.close()
    os.remove(tmp_path)

if len(sys.argv) > 3:
    infilepath = sys.argv[1]
    outfilepath = sys.argv[2]
    version = sys.argv[3]

    font = fontforge.open(infilepath)
    font.version = version

    generate(font, outfilepath)
