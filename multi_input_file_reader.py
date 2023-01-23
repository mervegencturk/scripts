import os
import csv

# path to the file containing the list of file paths
file_list_path = "path/to/file_list.txt"

# columns numbers to extract from each file
column_numbers = list(map(int, input("Which column numbers would you like to extract from each file, separated by commas? ").split(",")))

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
                    # create a new list to store the specified columns
                    selected_columns = []
                    # iterate over the column numbers
                    for column_number in column_numbers:
                        # add the specified column to the new list
                        selected_columns.append(row[column_number-1])
                    # write the new list to the output file
                    writer.writerow(selected_columns)
        else:
            print(f"{path} is not a valid file path.")
