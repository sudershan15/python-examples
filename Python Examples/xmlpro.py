import xml.parsers.expat
from xml.etree.ElementTree import ElementTree

# 3 handler functions
def start_element(name, attrs):
    f=open("tags.txt","a")
    T=str(name+" ")
    f.write(T)
    print name
    f.close()

tree = ElementTree()
words=0
count=1
tempwords=[]
p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1><child1 name="pauline">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)

f=open("tags.txt","r")
for line in f:
    tempwords=line.split(None)
    words+=len(tempwords)
f.close()
w=tempwords[1]
for i in range(1,words):
    if(w!=tempwords[i]):
        if(count==0):
            w=tempwords[i]
            count+=1
        else:
            count-=1
    else:
        count+=1
print "XML Tag most used is: ", w
