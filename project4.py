"""
Run the program using this file

    > python3 project4.py input_path

    where
        input_path : the path to a csv to create perceptron from
"""

import csv
import sys
import perceptron
import experiment

def process_file(path):
    
    """
    Takes in a data file and processes data into a set

    Notes:
        Assumes the label for the data lies in the final column
        Assumes the file is formatted as a csv

    Arguments:
        path : str : relative or absolute path to a csv file

    Returns:
        processed_data : ({label_i : [data_i]}) : a key-value dictionary,
            data contains a list of doubles
    """

    processed_data = dict()

    with open(path, newline='') as csvfile:
        for row in csvfile:
            # Remove any newline characters
            row = row.rstrip()
            # Split file on ',' characters
            row = row.split(',')
            # Remove the label from the data
            label = row.pop()
            # Convert list items to floats
            row = list(map(float, row))
            # Either append data to existing data list or
            if label in processed_data:
                processed_data[label].append(row)
            # Add a new key to the dictionary and append data to list
            else:
                # Ensure the row isn't empty
                if label != '':
                    processed_data[label] = list()
                    processed_data[label].append(row)

    return processed_data

#

#creates training data needed for learning problem 1,2 or 3 of task 2
def getTrainingDataForLP(label, processed_data):
    
    '''
    input: label is a string (i.e. 'Iris-virginica'), processed_data is a dictionary created from
    using the process_file function for a .data file
    output: a two dimensional list representing training data
    '''
    
    trainingSet = []
    
    for x in processed_data:
        if(x == label):
           for y in processed_data[x]:
               array = y.copy()
               array.append(1)
               for k in range(0, len(array)):
                   array[k] = float(array[k])
               #
               trainingSet.append(array)
           #
        else:
           for y in processed_data[x]:
               array = y.copy()
               array.append(-1)
               for k in range(0, len(array)):
                   array[k] = float(array[k])
               #
               trainingSet.append(array)
           #
        #
    #
    
    return trainingSet
       
#

def main():
   
    # Check arguments and assign path to variable
    if len(sys.argv) < 2:
        print("Usage: main.py [INPUT FILE PATH]")
        sys.exit()
    #
    
    input_path = sys.argv[1]
    
    # Obtain rows of file specified by sys.argv[1]
    processed_data = process_file(input_path)

    #write additional code

if __name__ == "__main__":
    
    main()
