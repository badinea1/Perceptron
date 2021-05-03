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
import os

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

def createEpochStatFile(processed_data, learningRate, percWeights, nameOfEpochFile):
 
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
    
    file = open(nameOfEpochFile, 'w')
    listOfArrays = [array1, array2, array3]
    lines = []
    
    word = 'Learning Rate: ' + str(learningRate) + '\n'
    lines.append(word)
        
    word = 'Initial Weight Vector: ' + str(percWeights) + '\n'
    lines.append(word)
    
    for x in range(0, len(listOfArrays)):
        lines.append('******************\n')
        number = x + 1
        word = 'LP ' + str(number) + '\n'
        lines.append(word)
        lines.append('\n')
        for y in range(0, len(listOfArrays[x])):
            epochNumber = y + 1
            learnedWeights = listOfArrays[x][y][0]
            numOfErrors = listOfArrays[x][y][1]
            string = 'EPOCH ' + str(epochNumber) + ': Learned Weights = ' + str(learnedWeights) + ', ' + '# of errors made on training set = ' + str(numOfErrors) + '\n'
            lines.append(string)
        #
    #
    
    lines.append('******************\n')
    lines.append('\n')
    
    file.writelines(lines)   
    
#

def main():
   
    # Check arguments and assign path to variable
    if len(sys.argv) < 3:
        print("Usage: project4.py [INPUT FILE PATH] [LEARNING RATE]")
        sys.exit()
    #
    
    # sys.argv[1] has path to .data file
    input_path = sys.argv[1]
        
    # sys.argv[2] is learning rate
    learningRate = float(sys.argv[2])
    
    # possibleTasks is an array of task numbers 
    possibleTasks = [2, 3.1, 3.2, 3.3, 4.1, 4.2]
    
    for taskNum in possibleTasks:
        
        processed_data = []
        percWeights = []
        
        if((taskNum == 4.1) | (taskNum == 4.2)):
            
            '''
            if you want to do task 4, you would have to shuffle data from .data file
            provided by input_path
            '''
            
            experiment.shuffleData(input_path)
            processed_data = process_file('shuffledData.data')
            os.system('rm shuffledData.data')
            sizeOfWeightVector = len(processed_data[list(processed_data)[0]][0]) + 1
            percWeights = experiment.getInitWeightVector(sizeOfWeightVector, 4)
            
        else:
            
            # process data from a .data file provided by input_path
            
            processed_data = process_file(input_path)   
            sizeOfWeightVector = len(processed_data[list(processed_data)[0]][0]) + 1
            percWeights = experiment.getInitWeightVector(sizeOfWeightVector, taskNum)
            
        #
        
        nameOfEpochFile = 'T' + str(taskNum) + 'EpochStatFile.txt'
        createEpochStatFile(processed_data, learningRate, percWeights, nameOfEpochFile)
        
    #
    
if __name__ == "__main__":
    
    main()
