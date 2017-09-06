PY = python
PYFLAGS = -m unittest discover -s 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = doxConfig

SRC = src/

.PHONY: all test doc clean

test: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: test doc

clean:
	rm -rf html
	rm -rf latex
