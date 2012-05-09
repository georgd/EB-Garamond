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
import sys
import getopt
import unicodedata as ucd
from fontTools.ttLib import TTFont

name = 'EBGaramond'
styles = ['Regular', 'Italic','SC','AllSC','Bold','Initials']
source = 'SFD'
build = 'build'
feafiles = 'featurefiles'

#def getHeights(font):
    # ymax + ymin, using the later as an overshoot
#    xHeight = font['x'].boundingBox()[3] + font['x'].boundingBox()[1]
#    cHeight = font['H'].boundingBox()[3] + font['H'].boundingBox()[1]

#    return int(xHeight), int(cHeight)

def mergeGpos(font):
    """ Clean GPOS lookups and merge them from the feature files """
    for lookup in font.gpos_lookups:
        font.removeLookup(lookup)
    
    font.mergeFeature('%s/%s_GPOS.fea' %(feafiles, style))

def generate(font, extension):
    """ Clean GSUB lookups and merge them from the feature files """
    for lookup in font.gsub_lookups:
        font.removeLookup(lookup)
    
    font.mergeFeature('%s/%s_features.fea' %(feafiles, style))

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
    
def usage(extramessage, code):
    if extramessage:
        print extramessage

    message = """Usage: %s OPTIONS...

Options:
  --withgpos		merge gpos featurefiles

  -h, --help            print this message and exit
""" % os.path.basename(sys.argv[0])

    print message
    sys.exit(code)
    
if __name__ == "__main__":
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                "h",
                ["help","withgpos"])
    except getopt.GetoptError, err:
        usage(str(err), -1)

    withgpos = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage("", 0)
        elif opt == "--withgpos": withgpos = True
        
    if not withgpos:
        for style in styles:
    	    f = fontforge.open('%s/%s-%s.sfdir' %(source, name, style))

    	    generate(f, 'otf')
    	    generate(f, 'ttf')
    	    
    else:
        for style in styles:
    	    f = fontforge.open('%s/%s-%s.sfdir' %(source, name, style))

    	    mergeGpos(f)
    	    generate(f, 'otf')
    	    generate(f, 'ttf')
