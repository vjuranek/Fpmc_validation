#!/usr/bin/env python
import os


#najde posledni vyskyt retezce v souboru a vrati to, co je za tim - tj. v napr. ucinny prurez (cislo)
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


#nahradi v souboru retezec str1 retezcem str2
def replaceInFile(file,str1,str2):
    import fileinput
    for line in fileinput.FileInput(file,inplace=1):
        if str1 in line:
            print str2,
        else:
            print line,

#zapise text do souboru
def writeInFile(file,text):
    f = open(file,'a')
    try:
        f.write(text)
    finally:
        f.close()

cardFile = './Datacards/dataExcCHIDe_Higgs'
outFile = 'output.log'
dataFile = 'data.txt'
str1 = 'HMASS       '
str2 = '.\n'
cstr = 'CROSS SECTION (PB) ='
command = './module < ' + cardFile + ' > ' + outFile
print 'commad = ' + command
for hmass in [115,120,130,140,150,160,170,180,190,200]:
    print 'zpracovavam Higgs mass\t=\t' + str(hmass) 
    ptstr = str1 + str(hmass) + str2
    replaceInFile(cardFile,str1,ptstr)
    os.system(command)
    cs = findLastInFile(outFile,cstr)
    text = str(hmass) + '\t' + cs + '\n'
    writeInFile(dataFile,text)
    
