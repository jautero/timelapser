VERSION := 0.5
PROGRAM := netf
TARDIR := $(PROGRAM)-$(VERSION)
TARFILE := $(TARDIR).tar.gz
SOURCE := Makefile netf.py screensaver.sh README.md

all: install

install: $(SOURCE)
	echo "Not implemented"

tarball: $(TARFILE)

$(TARFILE): $(TARDIR)
	tar czf $@ $</*

$(TARDIR): $(SOURCE)
	mkdir $@
	cp $(SOURCE) $(TARDIR)

clean:
	rm -rf $(TARDIR)
