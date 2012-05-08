#!/usr/bin/python
# coding: utf-8
##
## Based on Sebastian Kosch’s generate.py for Crimsontext
##
## Run from trunk directory like this:
## trunk$ python tools/generate.py

import fontforge
import psMat
import os
import unicodedata as ucd
from fontTools.ttLib import TTFont

name = 'EBGaramond'
styles = ['', '-It','SC','AllSC','-Bold','Initials']
source = 'SFD'
build = 'build'

#def getHeights(font):
    # ymax + ymin, using the later as an overshoot
#    xHeight = font['x'].boundingBox()[3] + font['x'].boundingBox()[1]
#    cHeight = font['H'].boundingBox()[3] + font['H'].boundingBox()[1]

#    return int(xHeight), int(cHeight)

def generate(font, extension):
    font.selection.all()
    font.autoHint()

    if extension == 'ttf':
#        font.em = 2048
        font.round()
        font.autoInstr()

    path = '%s/%s.%s' %(build, font.fontname, extension)
    tmp_path = '%s.tmp.%s' %(font.fontname, extension)

    font.generate(tmp_path)

    tmp_font = TTFont(tmp_path)
#    tmp_font['OS/2'].sxHeight, tmp_font['OS/2'].sCapHeight = getHeights(font)
    tmp_font.save(path)
    tmp_font.close()
    os.remove(tmp_path)
    

for style in styles:
    f = fontforge.open('%s/%s%s.sfdir' %(source, name, style))
 
    generate(f, 'otf')
    generate(f, 'ttf')
