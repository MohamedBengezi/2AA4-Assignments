PY = python
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = testdoc

SRC = testCircles.py

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
