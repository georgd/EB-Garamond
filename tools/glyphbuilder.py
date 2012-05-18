import fontforge;

glyphComponents = {
    'dcaron': ('d', 'uni030C.alt',),
    'hcircumflex': ('h', 'uni0302.flat',),
    'lacute': ('l', 'acutecomb.flat',),
    'lcaron': ('l', 'uni030C.alt',),
    'napostrophe': ('n', 'uni030C.alt',),
    'tcaron': ('t', 'uni030C.alt',),
    'uni01E9': ('k', 'uni030C.flat',),
    'aringacute': ('a', 'uni030A.stack', 'acutecomb.flat',),
    'uni021F': ('h', 'uni030C.flat',),
    'uni022D': ('o', 'tildecomb.stack', 'uni0304.stack',),
    'uni0231': ('o', 'uni0307.stack', 'uni0304.stack',),
    'uni1E79': ('u', 'tildecomb.stack', 'acutecomb.stack',),
    'uni1E7B': ('u', 'uni0304.stack', 'uni0308',),
    'uni1EA5': ('a', 'uni0302.stack', 'acutecomb.stack',),
    'uni1EA7': ('a', 'uni0302.stack', 'gravecomb.stack',),
    'uni1EA9': ('a', 'uni0302.stack', 'uni0309.stack',),
    'uni1EAB': ('a', 'uni0302.stack', 'tildecomb.stack',),
    'uni1EAD': ('a', 'uni0323', 'uni0302',),
    'uni1EAF': ('a', 'uni0306.stack', 'acutecomb.stack',),
    'uni1EB1': ('a', 'uni0306.stack', 'gravecomb.stack',),    
    'uni1EB3': ('a', 'uni0306.stack', 'uni0309.stack',),
    'uni1EB1': ('a', 'uni0306.stack', 'gravecomb.stack',),
    'uni1EB5': ('a', 'uni0306.stack', 'tildecomb.stack',),
    'uni1EB7': ('a', 'uni0323', 'uni0306',), 
    'uni1EBF': ('e', 'uni0302.stack', 'acutecomb.stack',),
    'uni1EC1': ('e', 'uni0302.stack', 'gravecomb.stack',),
    'uni1EC3': ('e', 'uni0302.stack', 'uni0309.stack',),
    'uni1EC5': ('e', 'uni0302.stack', 'tildecomb.stack',),
    'uni1EC7': ('e', 'uni0323', 'uni0302',),
    'uni1ED1': ('o', 'uni0302.stack', 'acutecomb.stack',),
    'uni1ED3': ('o', 'uni0302.stack', 'gravecomb.stack',),
    'uni1ED5': ('o', 'uni0302.stack', 'uni0309.stack',),
    'uni1ED7': ('o', 'uni0302.stack', 'tildecomb.stack',),
    'uni1ED9': ('o', 'uni0323', 'uni0302',),
#-----------greek-----------------------------------
    'iotadieresistonos': ('iota', 'uni0308.grkstack', 'acutecomb.grkstack',),
    'alphatonos': ('alpha', 'acutecomb.grk',),
    'epsilontonos': ('epsilon', 'acutecomb.grk',),
    'etatonos': ('eta', 'acutecomb.grk',),
    'iotatonos': ('iota', 'acutecomb.grk',),
    'upsilondieresistonos': ('upsilon', 'uni0308.grkstack', 'acutecomb.grkstack',),
    'omicrontonos': ('omicron', 'acutecomb.grk',),
    'upsilontonos': ('upsilon', 'acutecomb.grk',),
    'omegatonos': ('omega', 'acutecomb.grk',),
    'uni1F00': ('alpha', 'uni0313',),
    'uni1F01': ('alpha', 'uni0314',),
    'uni1F02': ('alpha', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F03': ('alpha', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F04': ('alpha', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F05': ('alpha', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F06': ('alpha', 'uni0313.grkstack', 'uni0342',),
    'uni1F07': ('alpha', 'uni0314.grkstack', 'uni0342',),
    'uni1F10': ('epsilon', 'uni0313',),
    'uni1F11': ('epsilon', 'uni0314',),
    'uni1F12': ('epsilon', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F13': ('epsilon', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F14': ('epsilon', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F15': ('epsilon', 'uni0314.grk', 'acutecomb.grkstack',),
#    'uni1F16': ('epsilon', 'uni0313.grkstack', 'uni0342',),
#    'uni1F17': ('epsilon', 'uni0314.grkstack', 'uni0342',),
    'uni1F20': ('eta', 'uni0313',),
    'uni1F21': ('eta', 'uni0314',),
    'uni1F22': ('eta', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F23': ('eta', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F24': ('eta', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F25': ('eta', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F26': ('eta', 'uni0313.grkstack', 'uni0342',),
    'uni1F27': ('eta', 'uni0314.grkstack', 'uni0342',),
    'uni1F30': ('iota', 'uni0313',),
    'uni1F31': ('iota', 'uni0314',),
    'uni1F32': ('iota', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F33': ('iota', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F34': ('iota', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F35': ('iota', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F36': ('iota', 'uni0313.grkstack', 'uni0342',),
    'uni1F37': ('iota', 'uni0314.grkstack', 'uni0342',),
    'uni1F40': ('omicron', 'uni0313',),
    'uni1F41': ('omicron', 'uni0314',),
    'uni1F42': ('omicron', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F43': ('omicron', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F44': ('omicron', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F45': ('omicron', 'uni0314.grk', 'acutecomb.grkstack',),
#    'uni1F46': ('omicron', 'uni0313.grkstack', 'uni0342',),
#    'uni1F47': ('omicron', 'uni0314.grkstack', 'uni0342',),
    'uni1F50': ('upsilon', 'uni0313',),
    'uni1F51': ('upsilon', 'uni0314',),
    'uni1F52': ('upsilon', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F53': ('upsilon', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F54': ('upsilon', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F55': ('upsilon', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F56': ('upsilon', 'uni0313.grkstack', 'uni0342',),
    'uni1F57': ('upsilon', 'uni0314.grkstack', 'uni0342',),
    'uni1F60': ('omega', 'uni0313',),
    'uni1F61': ('omega', 'uni0314',),
    'uni1F62': ('omega', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F63': ('omega', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F64': ('omega', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F65': ('omega', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F66': ('omega', 'uni0313.grkstack', 'uni0342',),
    'uni1F67': ('omega', 'uni0314.grkstack', 'uni0342',),
    'uni1F70': ('alpha', 'gravecomb.grk',),
    'uni1F71': ('alpha', 'acutecomb.grk',),
    'uni1F72': ('epsilon', 'gravecomb.grk',),
    'uni1F73': ('epsilon', 'acutecomb.grk',),
    'uni1F74': ('eta', 'gravecomb.grk',),
    'uni1F75': ('eta', 'acutecomb.grk',),
    'uni1F76': ('iota', 'gravecomb.grk',),
    'uni1F77': ('iota', 'acutecomb.grk',),
    'uni1F78': ('omicron', 'gravecomb.grk',),
    'uni1F79': ('omicron', 'acutecomb.grk',),
    'uni1F7A': ('upsilon', 'gravecomb.grk',),
    'uni1F7B': ('upsilon', 'acutecomb.grk',),
    'uni1F7C': ('omega', 'gravecomb.grk',),
    'uni1F7D': ('omega', 'acutecomb.grk',),
    'uni1F80': ('alpha', 'uni0345', 'uni0313',),
    'uni1F81': ('alpha', 'uni0345', 'uni0314',),
    'uni1F82': ('alpha', 'uni0345', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F83': ('alpha', 'uni0345', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F84': ('alpha', 'uni0345', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F85': ('alpha', 'uni0345', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F86': ('alpha', 'uni0345', 'uni0313.grkstack', 'uni0342',),
    'uni1F87': ('alpha', 'uni0345', 'uni0314.grkstack', 'uni0342',),
    'uni1F90': ('eta', 'uni0345', 'uni0313',),
    'uni1F91': ('eta', 'uni0345', 'uni0314',),
    'uni1F92': ('eta', 'uni0345', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1F93': ('eta', 'uni0345', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1F94': ('eta', 'uni0345', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1F95': ('eta', 'uni0345', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1F96': ('eta', 'uni0345', 'uni0313.grkstack', 'uni0342',),
    'uni1F97': ('eta', 'uni0345', 'uni0314.grkstack', 'uni0342',),
    'uni1FA0': ('omega', 'uni0345', 'uni0313',),
    'uni1FA1': ('omega', 'uni0345', 'uni0314',),
    'uni1FA2': ('omega', 'uni0345', 'uni0313.grk', 'gravecomb.grkstack',),
    'uni1FA3': ('omega', 'uni0345', 'uni0314.grk', 'gravecomb.grkstack',),
    'uni1FA4': ('omega', 'uni0345', 'uni0313.grk', 'acutecomb.grkstack',),
    'uni1FA5': ('omega', 'uni0345', 'uni0314.grk', 'acutecomb.grkstack',),
    'uni1FA6': ('omega', 'uni0345', 'uni0313.grkstack', 'uni0342',),
    'uni1FA7': ('omega', 'uni0345', 'uni0314.grkstack', 'uni0342',),
    'uni1FB2': ('alpha', 'uni0345', 'gravecomb.grk',),
    'uni1FB4': ('alpha', 'uni0345', 'acutecomb.grk',),
    'uni1FB7': ('alpha', 'uni0345', 'uni0342',),
    'uni1FC2': ('etha', 'uni0345', 'gravecomb.grk',),
    'uni1FC4': ('eta', 'uni0345', 'acutecomb.grk',),
    'uni1FC7': ('eta', 'uni0345', 'uni0342',),
    'uni1FD2': ('iota', 'uni0308.grkstack', 'gravecomb.grkstack',),
    'uni1FD3': ('iota', 'uni0308.grkstack', 'acutecomb.grkstack',),
    'uni1FD7': ('iota', 'uni0308', 'uni0342',),
    'uni1FE2': ('upsilon', 'uni0308.grkstack', 'gravecomb.grkstack',),
    'uni1FE3': ('upsilon', 'uni0308.grkstack', 'acutecomb.grkstack',),
    'uni1FE7': ('upsilon', 'uni0308', 'uni0342',),
    'uni1FF2': ('omega', 'uni0345', 'gravecomb.grk',),
    'uni1FF4': ('omega', 'uni0345', 'acutecomb.grk',),
    'uni1FF7': ('omega', 'uni0345', 'uni0342',),
    }


def composeAccented(glyph):
    """Compose accented glyphs.
    
    Get the components from the dictionary and build the new glyph
    from them."""

    components = glyphComponents[glyph.glyphname]
 
    base = components[0]
    marks = components[1:]

    glyph.clear()
    glyph.addReference(base)
    glyph.useRefsMetrics(base)
    for mark in marks:
        glyph.appendAccent(mark)

def buildAccentedGlyphs(junk,object):
#    """Get the names of the selected glyphs in a font.
#    
#    Call the composing function for every glyph that has an entry 
#    in the dictionary."""
    if type(object).__name__ == "font":
        for glyph in object.selection.byGlyphs:
            if glyph.glyphname in glyphComponents.keys():
                composeAccented(glyph)
            else:
                continue
    else: 
        if object.glyphname in glyphComponents.keys():
            composeAccented(object)
        else:
            logWarning('This glyph has no entry in the dictionary')

fontforge.registerMenuItem(buildAccentedGlyphs,None,None,("Font","Glyph"),None,"Glyphbuilder");