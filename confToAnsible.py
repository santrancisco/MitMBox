#!/usr/local/bin/python

import argparse
import io
import os
import re

class AnsibleOut():
    def __init__(self,filename,targetfolder):
        templatefile = targetfolder+"/templates/"+filename+".j2"
        defaultfile = targetfolder+"/defaults/"+filename+".yml"
        if not os.path.exists(os.path.dirname(templatefile)):
            try:
                os.makedirs(os.path.dirname(templatefile))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        if not os.path.exists(os.path.dirname(defaultfile)):
            try:
                os.makedirs(os.path.dirname(defaultfile))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        self.template = open(templatefile , 'w')
        self.default = open(defaultfile , 'w')
    def writetemplate(self, line):
        self.template.write(line+"\n")
    def writedefault(self, line):
        self.default.write(line+"\n")
    def close(self):
        self.template.close()
        self.default.close()
## Only allow alpha & numeric number to goes through and replace '-' or '.' with '_'
def cleanvar(variable):
    return filter(lambda c: (c.isalnum() or c=="_"), variable.replace("-","_").replace(".","_"))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--delimeter',action="store",help='delimeter', default="=")
    parser.add_argument('targetfile', help='config file')

    parser.add_argument('-t', '--targetfolder', help='destination folder for template file and default conf', default="./")
    args = parser.parse_args()
    filename = os.path.basename(args.targetfile)
    targetfolder = os.path.dirname(args.targetfolder+"/") #Make sure it is a folder path by putting / at the end :)
    try:
        f = open(args.targetfile,"r")
    except IOError as err:
      print ("Error: {0}".format(err))
      raise
    a=AnsibleOut(filename,targetfolder)
    ansibleglobalvar = cleanvar(filename)
    a.writedefault("### This file is generated by conftoAnsible script.")
    a.writedefault("### Copy content to default/main.yml because defaults folder does not include multiple .yml")
    a.writedefault(ansibleglobalvar + ":")
    for line in f.readlines():
        line = line.strip()
        if (not re.match("^ *#",line) and (re.match("^.+=.+",line))):
            varname = line[:line.index(args.delimeter)]
            defaultvar = line[(line.index(args.delimeter)+1):]
            a.writetemplate(varname + args.delimeter +"{{"+ ansibleglobalvar+"."+cleanvar(varname) +"}}")
            a.writedefault("  "+varname+ " : '"+defaultvar+"'")
        else:
            a.writetemplate(line)
    a.close()
