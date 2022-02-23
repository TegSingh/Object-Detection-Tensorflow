# Utility file to get a update the labels: number of instances
# from bs4 import BeautifulSoup as bfs
import os
import sys
from xml.dom import minidom
import xml.etree.ElementTree as ET

def main():

    # Read the directory
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)
    
    for i in range(file_count):

        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]

        if file_type == "xml":        
            tree = ET.parse(directory_path + "\\" + files[i])
            root = tree.getroot()
           
            for x in root.findall('filename'):
                print(x.text)        
                x.text = file_name + ".jpg"

            tree.write(directory_path + "\\" + files[i])


if __name__ == '__main__':
    main()
