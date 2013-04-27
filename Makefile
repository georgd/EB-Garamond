NAME=EBGaramond
VERSION=0.015c

SRC=SFD
BLD=build
WEB=web
SPEC=specimen
PACK=$(NAME)-$(VERSION)
WPCK=$(NAME)-$(VERSION)-web
DIST=$(NAME)-$(VERSION)-complete

#Call script through fontforge, not python. https://github.com/fontforge/fontforge/issues/528
#FF=fontforge
#Return to python because we don’t scale the font any longer.
PY=python
SCRIPT=tools/makefont.py
SFNTTOOL=java -jar sfnttool.jar

#SIZES=08 12
#STYLES=Regular SC Allsc Italic Bold
#SPECIAL=Initials InitialsF1 InitialsF2
FONTS=08-Regular 08-SC 08-Italic 12-Regular 12-SC 12-AllSC 12-Italic  -Initials -InitialsF1 -InitialsF2  #12-Bold

SFD=$(FONTS:%=$(SRC)/$(NAME)%.sfdir)
OTF=$(FONTS:%=$(BLD)/$(NAME)%.otf)
TTF=$(FONTS:%=$(BLD)/$(NAME)%.ttf)
WTT=$(FONTS:%=$(WEB)/$(NAME)%.ttf)
WOF=$(FONTS:%=$(WEB)/$(NAME)%.woff)
EOT=$(FONTS:%=$(WEB)/$(NAME)%.eot)
PDF=$(FONTS:%=$(SPEC)/$(NAME)%-Glyphs.pdf)

all: otf ttf web # pdfs
pack: dpack wpack

otf: $(OTF)
ttf: $(TTF)
web: $(WOF) $(EOT)
pdfs: $(PDF)

$(BLD)/%.otf: $(SRC)/%.sfdir Makefile $(SCRIPT)
	@echo "Generating	$@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION) 

$(BLD)/%.ttf: $(SRC)/%.sfdir Makefile $(SCRIPT)
	@echo "Generating	$@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION) 
	@echo "Autohinting	$@"
	@ttfautohint -x 0 -w 'gGD' $@ $@.tmp
	@mv $@.tmp $@

$(WEB)/%.woff: $(BLD)/%.ttf
	@echo "Generating	$@"
	@$(SFNTTOOL) -w $< $@
#	@sfnt2woff $<

$(WEB)/%.eot: $(BLD)/%.ttf
	@echo "Generating	$@"
	@$(SFNTTOOL) -e -x $< $@
#	@ttf2eot $< > $@

$(SPEC)/%-Glyphs.pdf: $(BLD)/%.ttf 
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
	@cp README.markdown README.xelualatex COPYING $(PACK)
	@zip -r $(PACK).zip $(PACK)

wpack: $(WOF) $(EOT)
	@echo "Packing webfonts to zipfile"
	@mkdir -p $(WPCK)
	@cp $(WOF) $(EOT) README.markdown COPYING $(WPCK)
	@zip -r $(WPCK).zip $(WPCK)

dist: $(OTF) $(TTF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(BLD)
	@mkdir -p $(DIST)/$(WEB)
	@mkdir -p $(DIST)/tools
	@mkdir -p $(DIST)/$(SPEC)
	@cp -r $(SFD) $(DIST)/$(SRC)
	@cp $(OTF) $(TTF) $(DIST)/$(BLD)
	@cp $(WOF) $(EOT) $(DIST)/$(WEB)
	@cp $(PDF) $(SPEC)/Specimen.pdf $(DIST)/$(SPEC)
	@cp $(SCRIPT) $(DIST)/tools
	@cp Makefile README.markdown README.xelualatex COPYING $(DIST)
	@zip -r $(DIST).zip $(DIST)

cleanpack:
	@rm -rf $(PACK) $(PACK).zip  $(WPCK) $(WPCK).zip

clean:
	@rm -rf $(OTF) $(TTF) $(WTT) $(WOF) $(EOT) $(PDF) $(PACK) $(PACK).zip $(WPCK) $(WPCK).zip $(DIST) $(DIST).zip
