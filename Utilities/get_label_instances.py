# Script to remove specific class labels from Pascal VOC XML files
from bs4 import BeautifulSoup as bfs
import os
import sys
from xml.dom import minidom


def main():

    # Read from the xml file
    path = sys.argv[1]
    with open(path) as f:
        data = f.read()

    # Use beautiful soup parser
    xml_data = bfs(data, "xml")

    # pass class label to remove as argument
    stat_label = sys.argv[2]

    # Extract all tags using find_all() method
    filter = xml_data.find_all('object')
    count = 0

    for object in filter:
        # Get the child tag name under object
        name_tag = object.find('name')
        # Compare the text with the label to remove
        if name_tag.text == stat_label:
            count += 1

    # Get file name from path
    path_list = path.split("\\")
    file_path_index = len(path_list) - 1
    file_name = path_list[file_path_index]

    print("#Instances of " + stat_label +
          " in " + file_name + ": " + str(count))


if __name__ == '__main__':
    main()
