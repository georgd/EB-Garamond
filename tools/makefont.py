#!/usr/bin/python
#
# invoked by the Makefile

from __future__ import absolute_import, print_function, unicode_literals
import glob
import os
import re
import sys
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
    '--reloadgpos', action="store_true",
    help='Clean GPOS lookups and reimport '
         'them from the feature files before generating '
         'font files. For Developement.')
argparser.add_argument(
    '--reloadgsub', action="store_true",
    help='Clean GSUB lookups and reimport '
         'them from the feature files before generating '
         'font files. For Developement.')
args = argparser.parse_args()

def reloadfeature(feature):
    """Read and merge a certain feature file. Example: For
EBGaramond12-Regular.sfdir, reloadfeature("GPOS") would merge
featurefiles/12-Regular_GPOS.fea and reloadfeature("features") would merge
featurefiles/12-Regular_features.fea (GSUB table)."""
    # Guess prefix of feature file from input, e.g.
    # 'EBGaramond12-Regular.sfdir' becomes inferred_style="12-Regular".
    font_source_name = os.path.split(args.input)[1]
    inferred_style = re.search('\d+-\w+', font_source_name).group(0)
    featurepath = "featurefiles/" + inferred_style + "_%s.fea"
    featurefile = featurepath % feature

    if os.path.exists(featurefile):
        font.mergeFeature(featurefile)
    else:
        sys.stderr.write("Could not find file " + featurefile + 
                ", so one or more --reload*s is not doing anything.\n")

font = fontforge.open(args.input)
font.version = args.version
font.encoding = 'UnicodeFull'
font.selection.all()
font.removeOverlap()
font.autoHint()

for svg in glob.glob(args.input + "/*svg"):
    letter = os.path.splitext(os.path.basename(svg))[0]
    font.createMappedChar(letter).importOutlines(svg)

if args.reloadgpos:
    for lookup in font.gpos_lookups:
        font.removeLookup(lookup)
    reloadfeature("GPOS")

if args.reloadgsub:
    for lookup in font.gsub_lookups:
        font.removeLookup(lookup)
    reloadfeature("features")

extension = os.path.splitext(args.output)[1]
if extension == '.ttf':
    font.correctReferences()
#   we don't scale the font any longer
#    font.em = 2048
    font.round()

font.generate(args.output) #do somthing about 'old-kern'## should we really?
