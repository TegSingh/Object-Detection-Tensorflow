# Utility file to run when renaming a dataset to numbers 1-n directories
import os
import sys


def main():

    # Get the Path for the directory from the terminal input
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)

    # Loop through the file list
    for i in range(file_count):
        print(files[i])
        src_path = directory_path + "/" + files[i]
        destination_path = directory_path + "/" + str(i+1) + ".jpg"
        os.rename(src_path, destination_path)

    try:
        f = open(directory_path, 'r')
        print("File opened successfully")
    except:
        print("Error opening file")


if __name__ == "__main__":
    main()