import os

def createGTK3(name, location):
    os.makedirs(location + "/" + name + "/gtk-3.0")
    createCSS(name, location)
    
def createGTK4(name, location):
    os.makedirs(location + "/" + name + "/gtk-4.0")
    createCSS(name, location)

def createCSS(name, location):
    cssFile = open(location + "/" + name + "/gtk-3.0/gtk.css","w")
    cssFile.write(str(open("gtk.css", "r").read()))
    cssFile.close()
