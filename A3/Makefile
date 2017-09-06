DOC =javadoc
DOCFLAGS =-d doc/
DOCCONFIG =src/*.java
SRC =src/TestPathCalculation.java
JFLAGS = -g
JCLASS = -cp $(CLASSPATH):.:/opt/local/share/java/junit.jar:/opt/local/share/java/hamcrest-core.jar
#JCLASS = -cp $(CLASSPATH):.:/usr/share/java/junit4.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
		src/*.java \

MAIN = TestPathCalculation
default: classes

classes: $(CLASSES:.java=.class)

test: $(MAIN).class
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: test doc
clean:
	$(RM) *.class