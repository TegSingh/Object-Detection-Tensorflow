# Utility file to rename all files in the dataset
import os
import sys

def main():

    # Get the Path for the directory from the terminal input
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)

    # Loop through the file list
    for i in range(file_count):
        file_name = files[i].split('.')[0]
        file_type = files[i].split('.')[1]
        if file_type == "jpg" or file_type == "xml":
            src_path = directory_path + "/" + files[i]
            print(src_path)
            destination_path = directory_path + "/" + file_name + "_online." + file_type
            print(destination_path)
            os.rename(src_path, destination_path)


if __name__ == "__main__":
    main()