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

    Notes:
        Assumes the label for the data lies in the final column
        Assumes the file is formatted as a csv

    Arguments:
        path : str : relative or absolute path to a csv file

    Returns:
        rows : a list of rows of a csv file
    """

    rows = []

    with open(path, newline='') as csvfile:
        
        for row in csvfile:
            # Remove any newline characters
            row = row.rstrip()
            
            if(len(row) > 0):
                # Split row of file on ',' characters
                row = row.split(',')
                
                rows.append(row)
            #
            
         #
        
    #
    
    return rows

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
    
    # Call perceptron algorithm

if __name__ == "__main__":
    
    main()
