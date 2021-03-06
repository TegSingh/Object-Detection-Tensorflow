# Utility file to get a dictionary containing the labels: number of instances
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
    # Get label 
    labels = {}
    count_xml = 0
    for i in range(file_count):

        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]

        if file_type == "xml":        
            count_xml += 1
            tree = ET.parse(directory_path + "\\" + files[i])
            root = tree.getroot()
           
            for x in root.findall('object'):
                label_name = x.find('name').text
                labels[label_name] = 0


    for i in range(file_count):

        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]

        # print(files[i])
        if file_type == "xml":        
            tree = ET.parse(directory_path + "\\" + files[i])
            root = tree.getroot()
           
            for x in root.findall('object'):
                label_name = x.find('name').text
                labels[label_name] += 1
                if label_name == "Motorcycle":
                    print(file_name)

    print("Number of Label XML files: " + str(count_xml))
    for i in labels.items():
	    print(i)


if __name__ == '__main__':
    main()
