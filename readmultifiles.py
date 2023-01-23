import os
import csv

# path to the file containing the list of file paths
file_list_path = "path/to/file_list.txt"

# column number to extract from each file
column_number = int(input("Which column number would you like to extract from each file? "))

# open the file containing the list of file paths
with open(file_list_path, "r") as file_list:
    # read the list of file paths
    paths = file_list.readlines()
    # remove newline characters from the file paths
    paths = [path.strip() for path in paths]

# create a new file to write the column data to
with open("output.csv", "w") as output_file:
    # create a CSV writer object
    writer = csv.writer(output_file)
    # iterate over the list of file paths
    for path in paths:
        # check if the file path is valid
        if os.path.isfile(path):
            # open the file
            with open(path, "r") as file:
                # create a CSV reader object
                reader = csv.reader(file)
                # iterate over the rows in the file
                for row in reader:
                    # write the specified column to the output file
                    writer.writerow([row[column_number-1]])
        else:
            print(f"{path} is not a valid file path.")
