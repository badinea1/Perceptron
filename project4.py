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
    if len(sys.argv) < 4:
        print("Usage: project4.py [INPUT FILE PATH] [TASK NUMBER] [LEARNING RATE]")
        sys.exit()
    #
    
    # sys.argv[1] has path to .data file
    input_path = sys.argv[1]
    
    # sys.argv[2] is task number
    taskNum = float(sys.argv[2])
    
    # sys.argv[3] is learning rate
    learningRate = float(sys.argv[3])
    
    # possibleTasks is an array of task numbers 
    possibleTasks = [2, 3.1, 3.2, 3.3, 4.1, 4.2]
    index = -1
    
    for x in range(0, len(possibleTasks)):
        if(possibleTasks[x] == taskNum):
            index = x
            break
        #
    #
    
    if(index == -1):
        print()
        print("Possible Task Numbers -> {2, 3.1, 3.2, 3.3, 4.1, 4.2}")
        print("You entered an invalid task number")
        print()
        sys.exit()
    #
    
    print()
    print('Task Number:', taskNum)
    
    # process data from a .data file provided by input_path
    processed_data = process_file(input_path)
    
    '''
    if you want to do task 4, you would have to shuffle data from .data file
    provided by input_path
    '''
    
    if((taskNum == 4.1) | (taskNum == 4.2)):
        taskNum = 4
        experiment.shuffleData(input_path)
        processed_data = process_file('shuffledData.data')
        os.system('rm shuffledData.data')
    #

    # Create initial weights based on task number
    sizeOfWeightVector = len(processed_data[list(processed_data)[0]][0]) + 1
    percWeights = experiment.getInitWeightVector(sizeOfWeightVector, taskNum)
    
    print('Initial Weight Vector:', percWeights)
    print()
    
    # Create training data for LP 1
    trainingSet1 = getTrainingDataForLP('Iris-setosa', processed_data)
    
    # Create training data for LP 2
    trainingSet2 = getTrainingDataForLP('Iris-versicolor', processed_data)
    
    # Create training data for LP 3
    trainingSet3 = getTrainingDataForLP('Iris-virginica', processed_data)
    
    # get information about every epoch of learning for trainingSet1
    array1 = perceptron.learnFromDataSet(learningRate, percWeights, trainingSet1)
    
    # get information about every epoch of learning for trainingSet2
    array2 = perceptron.learnFromDataSet(learningRate, percWeights, trainingSet2)
    
    # get information about every epoch of learning for trainingSet3
    array3 = perceptron.learnFromDataSet(learningRate, percWeights, trainingSet3)

if __name__ == "__main__":
    
    main()
