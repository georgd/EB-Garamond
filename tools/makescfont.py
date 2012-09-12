#!/usr/bin/python

import re
import argparse
import fontforge

argparser = argparse.ArgumentParser(description=
    "Generate a small-caps variant of a font out of a source \
for older programs that do not support OpenType features.")
argparser.add_argument(
    'input', 
    help='Input font source, e.g. "/some/path/Bla.sfdir"')
argparser.add_argument(
    'output', 
    help='Output font file, e.g. "/some/path/Bla.otf"')
argparser.add_argument(
    'version', 
    help='Version string to embed into the font file, e.g. "v1.1"')
args = argparser.parse_args()

font = fontforge.open(args.input)
font.version = args.version
font.encoding = 'UnicodeFull'

for glyph in font:
    # match all glyphs that start with a lower-case letter (to avoid the
    # c2sc-variants) and end with ".sc".
    match = re.search("^([a-z].*)\.sc$", glyph)

    if match:
        lowercase_glyph = match.group(1)
        smallcaps_replacement = glyph

        font.selection.select(smallcaps_replacement)
        font.copy()
        font.selection.select(lowercase_glyph)
        font.paste()

font.generate(args.output)
