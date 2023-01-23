import os
import csv
import matplotlib.pyplot as plt
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some file list path.')

# Add the argument
parser.add_argument('file_list_path', type=str, help='Path to the file containing the list of file paths')

# Parse the argument
args = parser.parse_args()

# columns numbers to extract from each file
column_numbers = list(map(int, input("Which column numbers would you like to extract from each file, separated by commas? ").split(",")))

# open the file containing the list of file paths
with open(args.file_list_path, "r") as file_list:
    # read the list of file paths
    paths = file_list.readlines()
    # remove newline characters from the file paths
    paths = [path.strip() for path in paths]

# iterate over the list of file paths
for path in paths:
    # check if the file path is valid
    if os.path.isfile(path):
        # open the file
        with open(path, "r") as file:
            # create a CSV reader object
            reader = csv.reader(file)
            # create a list to store the x values
            x_values = []
            # create a list of lists to store the y values
            y_values = []
            for i in range(1,len(column_numbers)):
                y_values.append([])
            # iterate over the rows in the file
            for row in reader:
                x_values.append(float(row[column_numbers[0]-1]))
                for i in range(1,len(column_numbers)):
                    y_values[i-1].append(float(row[column_numbers[i]-1]))
            # plot the data
            for i in range(len(y_values)):
                plt.plot(x_values, y_values[i])
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('Plot of Data')
            plt.show()
    else:
        print(f"{path} is not a valid file path.")
