# Utility script to check if the dataset is valid or not
import os
import sys


def main():

    # Get the Path for the directory from the terminal input
    directory_path = sys.argv[1]
    path, dirs, files = next(os.walk(directory_path))
    file_count = len(files)
    occurance = {}

    # Display all files to check directory correctness
    for i in range(file_count):
        print(files[i])

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
    for i in occurance.values():
        if i != 2:
            validity = False
    
    if validity:
        print("Dataset valid")
    else:
        print("Dataset invalid")


if __name__ == "__main__":
    main()