#!/usr/bin/env python3.5


import sys
import os
import re

import xml
import xml.etree.ElementTree as ET
global VERSION
global HOW_MANY_STARTS
 
HOW_MANY_STARTS = 100
VERSION = 0.1 
 
 
def  DecodeArguments():
    
    global SCRIPT_FOLDER
    global FILENAME
    
    typeOfBuild = ""
    typeOfVersion = ""
    FILENAME = ""
    SCRIPT_FOLDER = sys.argv[0]
    
    i=sys.argv[0].find(os.path.basename(__file__))
    
    SCRIPT_FOLDER = SCRIPT_FOLDER[0:i]
    
    # print("\nThe script is in ",sys.argv[0],"\n")
    print("The script is in ",SCRIPT_FOLDER)
    print("\n Script version  ",VERSION," \n")
    print(" python version ",sys.version_info)
    
    for arguments in sys.argv:
        print(arguments)
        arguments = arguments.strip()
        if "file=" in arguments:
            tab = arguments.split("=")
            # print(tab)
            FILENAME = tab[1]
        
        

    
def  XMLAnalysis():
    print("*"*HOW_MANY_STARTS)
    print(" I am analysing  ",FILENAME)
    print("*"*HOW_MANY_STARTS)
    file_xml = ET.parse(FILENAME)
    root = file_xml.getroot()
    
    for child in root:
        print(child.tag)

        print(child.text)
                
    print("*"*HOW_MANY_STARTS)
    
def main():
    
    DecodeArguments()
    XMLAnalysis()
    
        

if __name__ == "__main__":
    main()