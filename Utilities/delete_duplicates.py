# Utility Script to delete duplicate script
import os
import sys

def main():

    # Get the Path for the directory from the terminal input
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)
    occurance = {}

    # Display all files to check directory correctness
    # for i in range(file_count):
        # print(files[i])

    # Initialize your dictionary
    for i in range(file_count):
        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]
        
        if file_type == "jpg" or file_type == "xml":
            occurance[file_name] = 0

    # Combine occurances
    for i in range(file_count):
        file_name = files[i].split(".")[0]
        file_type = files[i].split(".")[1]
        
        if file_type == "jpg" or file_type == "xml":
            occurance[file_name] += 1

    print("Number of distinct Images and XML Files: ", len(occurance))
    validity = True
    for k, v in occurance.items():
        if v != 2:
            # The code assumes there are extra JPG files
            os.remove(directory_path + "\\" + k + ".jpg")
            print("Invalid File: ", k, " Number of occurances: ", v)
    



if __name__ == "__main__":
    main()