import os
import argparse
from glyphcomponents import glyphComponents

argparser = argparse.ArgumentParser(description=
    'Writes the feature file (ccmpcomp.fea) for glyph composition '
    '(the "ccmp" table in OpenType) for a given style.')
argparser.add_argument('style', 
                       help='The style for which to generate the ccmp feature file. '
                            'Actually the directory names in ../featurefiles, so e.g. "Regular".')
style = argparser.parse_args().style

with open('../featurefiles/%s/ccmpcomp.fea' % style, 'w') as f:
    f.write('lookup CCMP_Precomp {\n')
    
    for sub, by in glyphComponents.iteritems():
        f.write('    sub ' + sub + ' by ' + " ".join(by) + ' ;\n')
    
    f.write('} CCMP_Precomp;\n')
