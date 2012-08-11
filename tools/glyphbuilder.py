import fontforge
from glyphcomponents import glyphComponents

#def componentsByFontname(font, fontname):
#    module_name = fontname + "_components"
#    module = __import__(module_name)

def composeAccented(glyph):
    """Compose accented glyphs.
    
    Get the components from the dictionary and build the new glyph
    from them."""
    
    glif = glyph

    components = glyphComponents[glif.glyphname]
 
    base = components[0]
    marks = components[1:]
    
    greekUC = ['Alpha', 'Epsilon', 'Eta', 'Iota', 'Omicron', 'Rho', 'Upsilon', 'Omega']

    glif.clear()
    glif.addReference(base)

    glif.useRefsMetrics(base)

    for mark in marks:
        glif.appendAccent(mark)

    l = glif.left_side_bearing
    
    if base in greekUC:
        if l < -19:
            glif.useRefsMetrics(base, False)
            glif.left_side_bearing = -20
        else:
            glif.useRefsMetrics(base, True)
        
    elif base == 'space.stack':
            glif.useRefsMetrics(base, False)
            glif.left_side_bearing = 30
            glif.right_side_bearing = 30
    else:
        glif.useRefsMetrics(base, True)

def buildAccentedGlyphs(junk,object):
#    """Get the names of the selected glyphs in a font.
#    
#    Call the composing function for every glyph that has an entry 
#    in the dictionary."""
#    componentsByFontname(font, font.fontname)
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
