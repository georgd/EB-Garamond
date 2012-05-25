import os
import sys
import getopt

from glyphbuilder import glyphComponents

def printCCMPLookups(file):
    file.write('lookup CCMP_Precomp {\n')
    
    for key in glyphComponents.keys():
        components = glyphComponents[key]
        file.write('    sub ' + key + ' by ')
        for component in components:
            file.write(component + ' ')
        file.write(';\n')
    
    file.write('} CCMP_Precomp;\n')

def generateFeatureFile(style):
    feature_file_name = 'ccmpcomp.fea'
    dirname = '../featurefiles/%s' %(style)
    os.chdir(dirname)
    feature_file = open(feature_file_name, 'w')
    printCCMPLookups(feature_file)
    feature_file.close()
    
def usage(extramessage, code):
    if extramessage:
        print extramessage
    
    message = """Usage: %s OPTIONS...
    Options:
        --style=STYLE       style name of font
        
        -h, --help          print this message and exit    
    """ % os.path.basename(sys.argv[0])
    
    print message
    sys.exit(code)
    
if __name__ == "__main__":
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                "h",
                ["help","style="])
    except getopt.GetoptError, err:
        usage(str(err), -1)
    
    style = None
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage("", 0)
        elif opt == '--style': style = arg
        
        if not style:
            usage("No style name", -1)
    
    generateFeatureFile(style)
