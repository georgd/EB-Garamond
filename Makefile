NAME=EBGaramond
VERSION=0.014b

SRC=SFD
BLD=build
WEB=web
PACK=$(NAME)-$(VERSION)
DIST=$(NAME)-$(VERSION)-complete

PY=python
SCRIPT=tools/generate2.py
SFNTTOOL=sfnttool.jar

#SIZES=08 12
FONTS=08-Regular 08-Italic 12-Regular 12-SC 12-AllSC 12-Italic -Initials #Bold BoldItalic Semibold SemiboldItalic


SFD=$(FONTS:%=$(SRC)/$(NAME)%.sfdir)
OTF=$(FONTS:%=$(BLD)/$(NAME)%.otf)
TTF=$(FONTS:%=$(BLD)/$(NAME)%.ttf)
WTT=$(FONTS:%=$(WEB)/$(NAME)%.ttf)
WOF=$(FONTS:%=$(WEB)/$(NAME)%.woff)
EOT=$(FONTS:%=$(WEB)/$(NAME)%.eot)

all: otf ttf web

otf: $(OTF)
ttf: $(TTF)
web: $(WTT) $(WOF) $(EOT)

$(BLD)/%.otf: $(SRC)/%.sfdir Makefile $(SCRIPT)
	@echo "Generating	$@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION)
	
$(BLD)/%.ttf: $(SRC)/%.sfdir Makefile $(SCRIPT)
	@echo "Generating	$@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION)
	@echo "Autohinting	$@"
	@ttfautohint -x 0 -w 'gGD' $@ $@.tmp
	@mv $@.tmp $@
	
$(WEB)/%.ttf: $(BLD)/%.ttf
	@echo "Copying		$@"
	@cp $< $@
		
$(WEB)/%.woff: $(WEB)/%.ttf
	@echo "Generating	$@"
	@$(SFNTTOOL) -w $< $@
	
$(WEB)/%.eot: $(WEB)/%.ttf
	@echo "Generating	$@"
	@$(SFNTTOOL) -e -x $< $@

pack: $(OTF) $(TTF)
	@echo "Packing fonts to zipfile"
	@mkdir -p $(PACK)/otf
	@mkdir -p $(PACK)/ttf
	@cp $(OTF) $(PACK)/otf
	@cp $(TTF) $(PACK)/ttf
	@cp README $(PACK)
	@zip -r $(PACK).zip $(PACK)

dist: $(OTF) $(TTF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(BLD)
	@mkdir -p $(DIST)/tools
	@cp -r $(SFD) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)/$(BLD)
	@cp $(TTF) $(DIST)/$(BLD)
	@cp $(SCRIPT) $(DIST)/tools
	@cp Makefile README $(DIST)
	@zip -r $(DIST).zip $(DIST)

cleanpack:
	@rm -rf $(PACK) $(PACK).zip

clean:
	@rm -rf $(OTF) $(TTF) $(WTT) $(WOF) $(EOT) $(PACK) $(PACK).zip $(DIST) $(DIST).zip
