VERSION := 0.5
PROGRAM := netf
TARDIR := $(PROGRAM)-$(VERSION)
TARFILE := $(TARDIR).tar.gz
SOURCE := Makefile netf.py netf.sh netf.desktop README.md

all: install

install: $(SOURCE)
	install netf.desktop /usr/share/applnk/System/ScreenSavers/

tarball: $(TARFILE)

$(TARFILE): $(TARDIR)
	tar czf $@ $</*

$(TARDIR): $(SOURCE)
	mkdir $@
	cp $(SOURCE) $(TARDIR)

clean:
	rm -rf $(TARDIR) $(TARFILE)
