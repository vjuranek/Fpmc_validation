#!/usr/bin/env python
import os


#najde posledni vyskyt retezce v souboru
def findLastInFile(file,str):
    css = []
    i = 0
    f = open(file,'r')
    try:
        for line in f:
            if(str in line):
                css.append(line)
                i = i+1
    finally:
        f.close()
    csstr = css[i-1].strip()
    csstr = csstr.split(str)
    cs = csstr[len(csstr)-1].strip()
    print cs
    return cs



def replaceInFile(file,str1,str2):
    import fileinput
    for line in fileinput.FileInput(file,inplace=1):
        if str1 in line:
            #line=line.replace(str1,str2)
            #print line,
            print str2,
        else:
            print line,

def writeInFile(file,text):
    f = open(file,'a')
    try:
        f.write(text)
    finally:
        f.close()

cardFile = './Datacards/dataSD_W'
outFile = 'output.log'
dataFile = 'data.txt'
str1 = 'PTMIN       '
str2 = '.\n'
cstr = 'CROSS SECTION (PB) ='
command = './module < ' + cardFile + ' > ' + outFile
print 'commad = ' + command
for ptmin in [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,100,150,200,250,300,350,400]:
#for ptmin in [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,100]:
    print 'zpracovavam ptmin\t=\t' + str(ptmin) 
    ptstr = str1 + str(ptmin) + str2
    replaceInFile(cardFile,str1,ptstr)
    os.system(command)
    cs = findLastInFile(outFile,cstr)
    text = str(ptmin) + '\t' + cs + '\n'
    writeInFile(dataFile,text)
    
