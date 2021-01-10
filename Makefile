NAME=EBGaramond
VERSION=0.016

SRC=SFD
BLD=build
WEB=web
SPEC=specimen
PACK=$(NAME)-$(VERSION)
WPCK=$(NAME)-$(VERSION)-web
DIST=$(NAME)-$(VERSION)-complete

#Call script through fontforge, not python. https://github.com/fontforge/fontforge/issues/528
FF=fontforge
#Return to python because we don’t scale the font any longer.
PYTHON?=python
SCRIPT=tools/makefont.py

#SIZES=08 12
#STYLES=Regular SC Allsc Italic Bold
#SPECIAL=Initials InitialsF1 InitialsF2
FONTS=08-Regular 08-Italic 12-Regular SC12-Regular 12-AllSC 12-Italic  -Initials -InitialsF1 -InitialsF2 SC08-Regular # SC12-Italic 12-Bold

SFD=$(FONTS:%=$(SRC)/$(NAME)%.sfdir)
OTF=$(FONTS:%=$(BLD)/$(NAME)%.otf)
TTF=$(FONTS:%=$(BLD)/$(NAME)%.ttf)
WOF=$(FONTS:%=$(WEB)/$(NAME)%.woff)
PDF=$(FONTS:%=$(SPEC)/$(NAME)%-Glyphs.pdf)

all: otf ttf webfonts # pdfs
pack: dpack wpack

otf: $(OTF)
ttf: $(TTF)
webfonts: $(WOF)
pdfs: $(PDF)

$(BLD):
	@mkdir $@
$(WEB):
	@mkdir -p $@
$(SPEC):
	@mkdir -p $@

$(BLD)/%.otf: $(SRC)/%.sfdir Makefile $(SCRIPT) | $(BLD)
	@echo "Generating	$@"
	@$(PYTHON) $(SCRIPT) $< $@ $(VERSION)

$(BLD)/%.ttf: $(SRC)/%.sfdir Makefile $(SCRIPT) | $(BLD)
	@echo "Generating	$@"
	@$(PYTHON) $(SCRIPT) $< $@ $(VERSION)
	@echo "Autohinting	$@"
	@ttfautohint -x 0 -a sss $@ $@.tmp
	@mv $@.tmp $@

$(WEB)/%.woff: $(BLD)/%.ttf | $(WEB) $(BLD)
	@echo "Generating	$@"
	@fontforge -lang=ff -c 'Open($$1); Generate($$2)' $< $@

$(SPEC)/%-Glyphs.pdf: $(BLD)/%.ttf $(SPEC)
	@echo "Generating	$@"
	@fntsample -f $< -o $@ -l > $@.outline
	@pdfoutline $@ $@.outline $@
	@rm $@.outline

dpack: $(OTF) $(TTF)
	@echo "Packing fonts to zipfile"
	@mkdir -p $(PACK)/otf
	@mkdir -p $(PACK)/ttf
	@mkdir -p $(PACK)/specimen
	@cp $(OTF) $(PACK)/otf
	@cp $(TTF) $(PACK)/ttf
#	@cp $(PDF) $(PACK)/specimen        #Temporarily out of order
	@cp $(SPEC)/Specimen.pdf  $(PACK)/specimen
	@cp Changes README.markdown README.xelualatex COPYING $(PACK)
	@zip -r $(PACK).zip $(PACK)

wpack: $(WOF)
	@echo "Packing webfonts to zipfile"
	@mkdir -p $(WPCK)
	@cp $(WOF) README.markdown COPYING $(WPCK)
	@zip -r $(WPCK).zip $(WPCK)

dist: $(OTF) $(TTF) $(WOF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(BLD)
	@mkdir -p $(DIST)/$(WEB)
	@mkdir -p $(DIST)/tools
	@mkdir -p $(DIST)/$(SPEC)
	@cp -r $(SFD) $(DIST)/$(SRC)
	@cp $(OTF) $(TTF) $(DIST)/$(BLD)
#	@cp $(PDF) $(SPEC)/Specimen.pdf $(DIST)/$(SPEC) #Temporarily out of order
	@cp $(SPEC)/Specimen.pdf $(DIST)/$(SPEC)
	@cp $(SCRIPT) $(DIST)/tools
	@cp Changes Makefile README.md README.xelualatex COPYING $(DIST)
	@zip -r $(DIST).zip $(DIST)

cleanpack:
	@rm -rf $(PACK) $(PACK).zip  $(WPCK) $(WPCK).zip

clean:
	@rm -rf $(OTF) $(TTF) $(WOF) $(PDF) $(PACK) $(PACK).zip $(WPCK) $(WPCK).zip $(DIST) $(DIST).zip
