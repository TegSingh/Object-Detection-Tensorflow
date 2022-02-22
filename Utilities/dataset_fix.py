# Utility file to run when renaming a dataset to numbers 1-n directories
import os
import sys


def main():

    # Get the Path for the directory from the terminal input
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)
    file_num = 1

    # Loop through the file list
    for i in range(file_count):
        # print(files[i])
        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]
        
        if file_type == "jpg":
        
            for j in range(file_count):
        
                file_name_xml = files[j].split(".")[0]
                file_type_xml = files[j].split(".")[1]
        
                if file_name == file_name_xml and file_type_xml == "xml":
                    # print(i, files[i], files[j])
                    src_path_jpg = directory_path + "\\" + files[i]
                    src_path_xml = directory_path + "\\" + files[j]
                    destination_path_jpg = directory_path + "\\New\\" + str(file_num) + ".jpg"
                    destination_path_xml = directory_path + "\\New\\" + str(file_num) + ".xml"
                    print()
                    print(src_path_jpg)
                    print(src_path_xml)
                    print(destination_path_jpg)
                    print(destination_path_xml)
                    file_num += 1
                    os.rename(src_path_jpg, destination_path_jpg)
                    os.rename(src_path_xml, destination_path_xml)

    # try:
    #     f = open(directory_path, 'r')
    #     print("File opened successfully")
    # except:
    #     print("Error opening file")


if __name__ == "__main__":
    main()