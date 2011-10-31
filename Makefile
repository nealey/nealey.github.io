DESTDIR = $(HOME)/public_html

TEMPLATE = template.xml
MDWNTOHTML = ./mdwntohtml $(TEMPLATE)

# HTML to be generated
HTML = index.html

# Things to copy
COPY += mdwntohtml template.xml
COPY += face.png chumby-photo.cgi
COPY += format.css default.css print.css
COPY += gitweb.cgi git-logo.png gitweb.css gitweb.conf

# Directories in which %.mdwn generates %.html
PLAIN = . papers poems misc

# Other targets for "make all"
TARGETS = html copy 
TARGETS += $(DESTDIR)/tmp $(DESTDIR)/footer.xml $(DESTDIR)/projects
TARGETS += $(DESTDIR)/geneweb.cgi

all: default

include */*.mk

$(DESTDIR)/%.html: %.mdwn $(TEMPLATE)
	@mkdir -p $(dir $@)
	$(MDWNTOHTML) < $< > $@

$(DESTDIR)/%: %
	@mkdir -p $(dir $@)
	cp $< $@

$(DESTDIR)/tmp:
	mkdir -p $@

$(DESTDIR)/footer.xml: $(TEMPLATE)
	awk '(/FOOT/) { a += 1; next; } (a == 1) { print; }' $< > $@

$(DESTDIR)/projects:
	ln -s $(HOME)/projects $@

$(DESTDIR)/geneweb.cgi: geneweb.c
	$(CC) -o $@ $<
	chmod +s $@

$(DESTDIR)/%-sm.jpg: %.jpg
	jpegtopnm $< | pnmscale -xysize 200 200 | pnmtojpeg > $@

default: $(TARGETS)

MDWN = $(wildcard $(addsuffix /*.mdwn, $(PLAIN)))
HTML += $(patsubst %.mdwn, %.html, $(MDWN))

html: $(addprefix $(DESTDIR)/, $(HTML))
copy: $(addprefix $(DESTDIR)/, $(COPY))

clean:
	rm -rf $(wildcard $(DESTDIR)/*)