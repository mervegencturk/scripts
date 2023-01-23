import os
import csv
import matplotlib.pyplot as plt

# Define the path to the file containing the list of file paths
file_list_path = 'file_list.txt'

# Define the column numbers to extract from each file
column_numbers = [1, 2, 3]

# open the file containing the list of file paths
with open(file_list_path, "r") as file_list:
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
                    y_values[i-1].append(float(row[column_numbers[

    for i in range(len(y_values)):
        plt.plot(x_values, y_values[i])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Plot of Data')
    plt.show()

