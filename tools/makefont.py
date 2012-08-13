#!/usr/bin/python
#
# invoked by the Makefile

import os
import argparse
import fontforge

argparser = argparse.ArgumentParser(description=
    "Generate a font file out of a source. Best invoked from the Makefile.")
argparser.add_argument(
    'input', 
    help='Input font source, e.g. "/some/path/Bla.sfdir"')
argparser.add_argument(
    'output', 
    help='Output font file, e.g. "/some/path/Bla.otf"')
argparser.add_argument(
    'version', 
    help='Version string to embed into the font file, e.g. "v1.1"')
argparser.add_argument(
    '--reloadlookups',
    help='Clean lookups (GPOS and GSUB) and reimport '
         'them from the feature files before generating '
         'font files. For Developement. Give the '
         'identifier-prefix for the font from featurefiles/, '
         'e.g. "Regular" when you want to make "EBGaramond12-Regular.sfdir". '
         'When using this option, execute the script from '
         'the top-level directory so it can find the feature files!')
args = argparser.parse_args()

font = fontforge.open(args.input)
font.version = args.version
font.encoding = 'UnicodeFull'
font.selection.all()
font.autoHint()

if args.reloadlookups:
    for lookup in font.gpos_lookups:
        font.removeLookup(lookup)
    for lookup in font.gsub_lookups:
        font.removeLookup(lookup)
    
    featurepath = "featurefiles/" + args.reloadlookups + "_%s.fea"
    featurefile = featurepath % "features"
    if os.path.exists(featurefile):
        font.mergeFeature(featurefile)
    gpos_featurefile = featurepath % "GPOS"
    if os.path.exists(gpos_featurefile):
        font.mergeFeature(gpos_featurefile)

extension = os.path.splitext(args.output)[1]
if extension == '.ttf':
    font.correctReferences()
    font.em = 2048
    font.round()

font.generate(args.output)
