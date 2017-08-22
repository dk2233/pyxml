import xml.etree.ElementTree as ET


def main():
    
    tree = ET.parse('Config.xml')
    root = tree.getroot()
    #print(root)

    for child in root:
        print(child.tag)
        if ( 'QAC' in child.tag):
            
            print(child.findall("EXCLUDE"))
            
            for i in child.findall("EXCLUDE"):
                print(i.tag)
                print(i.text)
                print(i.attrib)
        

if __name__ == "__main__":
    main()