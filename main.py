import os
import json

Path="D:/EasyNoteTaker" #Defeat path

def init():
    try:
        os.chdir(Path)
    except FileNotFoundError:
        os.mkdir(Path)

init()

class depository(): # class that store one type of note
    def __init__(self,path="lib01",language="English",libs=[]):
        self.path=path
        self.language=language
        self.localLibs=libs
    def getPath(self):
        return self.path
    def chPath(self,newPath):
        self.path=newPath
        return
    def getLanguage(self):
        return self.language
    def chLanguage(self,newLanguage):
        self.language=newLanguage
        return
    def store(self):
        os.chdir(Path)
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            os.mkdir(self.path)
            os.chdir(self.path)
            settings={"Language":self.language,"Path":self.path}
            s=open("settings.txt","w")
            s.write(json.dumps(settings))
            s.close()
            return 
        else:
            print("DepHasCreated")
    def newLib(self,lib):
        try:
            os.chdir(Path+'/'+self.path)
        except FileNotFoundError:
            self.localLibs.append()
            s=open(lib+'.txt',"w")
            s.close()
        else:
            print("LibHasCreated")
    def getLibs(self):
        return self.localLibs
    def add(self,libName,addThing):
        try:
            open(libName+'.txt','r')
        except FileNotFoundError:
            print("LibHasNotCreated")
        else:
            a=open(libName+'.txt','a')
            if isinstance(addThing,str): #add str
                if addThing[-1]=='\n':
                    a.write(addThing)
                else:
                    a.write(addThing+'\n')
            else:#type list
                for i in addThing:
                    if i[-1]=='\n':
                        a.write(i)
                    else:
                        a.write(i+'\n')
            a.close()
        return

def readJson(file): # give file
    fs=open(file,"r").readline()
    return json.loads(fs)

libs=[]

def Scan():
    os.chdir(Path)
    global libs
    for file in os.listdir():
        if '.' not in file: # actually a lib, not a settings file
            #libs.append(file)

            se=readJson(file+'/settings.txt')
            os.chdir(file)
            locLib=os.listdir()
            #print(locLib)

            if len(locLib)==1: #only settings
                locLib=[]
            else:
                print(locLib)
                locLib.remove("settings.txt")
                for i in range(len(locLib)):
                    locLib[i]=(locLib[i].split('.txt'))[0]
            libs.append(depository(se["Path"],se["Language"],locLib))
    return libs


