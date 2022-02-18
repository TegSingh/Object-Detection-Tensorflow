import os
import xml.etree.ElementTree as ET
import sys

# assign directory
directory = sys.argv[1]
class_list = ['Tree', 'Pole', 'Boat', 'Stop Sign', 'Train', 'Bench', 'Animal']

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(filename)
    
    # checking if it is a file
    if os.path.isfile(f) and f != 'label2.py':
        tree = ET.parse(f)
        parent=tree.getroot()
    
        for x in parent.findall('object'):
            item = x.find('name').text
    
            if item in class_list :
                parent.remove(x)
    
        tree.write(f)