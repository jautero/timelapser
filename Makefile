VERSION := 0.5
PROGRAM := netf
TARDIR := $(PROGRAM)-$(VERSION)
TARFILE := $(TARDIR).tar.gz
SOURCE := Makefile netf.py netf-display netf.desktop README.md

all: install

install: $(SOURCE)
	install netf.desktop /usr/share/applications/screensavers/
	install netf-display /usr/lib/xscreensaver/
	ln -s /usr/lib/xscreensaver/netf-display /usr/bin

tarball: $(TARFILE)

$(TARFILE): $(TARDIR)
	tar czf $@ $</*

$(TARDIR): $(SOURCE)
	mkdir $@
	cp $(SOURCE) $(TARDIR)

clean:
	rm -rf $(TARDIR) $(TARFILE)
