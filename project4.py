import csv
import sys
import perceptron
import experiment
import os
import matplotlib.pyplot as plt

'''
Gordon Petry
Yuriy Deyneka
Amulya Badineni
Vihan Patel
'''

def process_file(path):
    
    """
    input: path is a string representing an absolute or relative path to a .csv or .data file 
    output: a dictionary where each element has a ...
        -> key = a string (i.e. 'Iris-setosa')
        -> value = a list containing training examples associated with the key 
    """
    
    processed_data = dict()

    with open(path, newline='') as csvfile:
        
        for row in csvfile:
            
            # Remove any newline characters from a line in a .data or .csv file 
            row = row.rstrip()
            
            if(len(row) > 0):
                
                # create a list from a line we just removed newline characters from 
                row = row.split(',')
                label = row.pop()
                row = list(map(float, row))
                row.insert(0,1)
                
                # place the list we just created into a dictionary 
                if label in processed_data:
                    processed_data[label].append(row)
                else:
                    if label != '':
                        processed_data[label] = list()
                        processed_data[label].append(row)
                    #
                #
                
            #
            
        #
        
    #

    return processed_data

#

#creates training data needed for learning problem 1,2 or 3 of the project 
def getTrainingDataForLP(label, processed_data):
    
    '''
    input: label is a string (i.e. 'Iris-virginica'), processed_data is a 
    dictionary created using the process_file function 
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
               # set the array with the data
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

#creates an epoch stats file needed for the project 
def createEpochStatFile(processed_data, learningRate, percWeights, nameOfEpochFile):
    
    '''
    input: processed_data is a dictionary created using the process_file function, learningRate is a float, 
    percWeights is a list of initial weights for a perceptron, nameOfEpochFile is a string representing the 
    name of the epoch file which will be outputted from this function
    output: an epoch stats file 
    '''
    
    learningProblems = []
    items = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    titles = ['Iris-setosa vs. not Iris-setosa', 'Iris-versicolor vs. not Iris-versicolor', 'Iris-virginica vs. not Iris-virginica']
    copyOfPercWeights = percWeights.copy()
    
    for x in range(0, len(items)):
        trainingSet = getTrainingDataForLP(items[x], processed_data)
        array = perceptron.learnFromDataSet(learningRate, percWeights, trainingSet)
        learningProblems.append(array)
    #
    
    file = open(nameOfEpochFile, 'w')
    lines = []
    
    word = 'Learning Rate: ' + str(learningRate) + '\n'
    lines.append(word)
    
    word = 'Initial bias: ' + str(copyOfPercWeights[0]) + '\n'
    lines.append(word)
    
    copyOfPercWeights.pop(0)
    
    for x in range(0, len(copyOfPercWeights)):
        copyOfPercWeights[x] = 'w_' + str(x + 1) + ' = ' + str(copyOfPercWeights[x])
    #   
        
    word = 'Initial Weight Vector: ' + str(copyOfPercWeights) + '\n'
    lines.append(word)
    
    for x in range(0, len(learningProblems)):
        lines.append('******************\n')
        number = x + 1
        word = 'LP' + str(number) + ' (' + titles[x] + ')' + '\n'
        lines.append(word)
        lines.append('\n')
        for y in range(0, len(learningProblems[x])):
            epochNumber = y + 1
            learnedWeights = learningProblems[x][y][0]
            info = 'Learned bias = ' + str(learnedWeights[0])
            learnedWeights.pop(0)
            for k in range(0, len(learnedWeights)):
                learnedWeights[k] = 'w_' + str(k + 1) + ' = ' + str(learnedWeights[k])   
            #
            numOfErrors = learningProblems[x][y][1]
            string = 'EPOCH ' + str(epochNumber) + ': ' + info + ', Learned Weights =  ' + str(learnedWeights) + ', ' + '# of errors made on training data = ' + str(numOfErrors) + '\n'
            lines.append(string)
        #
    #
    
    lines.append('******************\n')
    lines.append('\n')
    
    file.writelines(lines)   
    
#

#creates plots needed for the project
def createPlotFile(processed_data, learningRate, percWeights, task):
    
    '''
    input: processed_data is a dictionary created using the process_file function, learningRate is a float, 
    percWeights is a list of initial weights for a perceptron, task is a string giving information about
    whether a plot is for task 2, 3.1, 3.2, 3.3, 4.1, or 4.2 
    output: three .png files
        -> The format of the name for the output files is T#LP@Plot.png, where # is a task number (i.e. 3.1) and @ is 1, 2 or 3. 
        If the name of an output file is T3.1LP1Plot.png, it means that the plot is for learning problem 1 (Iris-setosa vs. not Iris-setosa) 
        of task 3.1.
    '''
    
    learningProblems = []
    items = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    titles = ['Iris-setosa vs. not Iris-setosa', 'Iris-versicolor vs. not Iris-versicolor', 'Iris-virginica vs. not Iris-virginica']
    copyOfPercWeights = percWeights.copy()
    
    for x in range(0, len(items)):
        trainingSet = getTrainingDataForLP(items[x], processed_data)
        array = perceptron.learnFromDataSet(learningRate, copyOfPercWeights, trainingSet)
        learningProblems.append(array)
    #

    for x in range(0, len(learningProblems)):
        number = x + 1
        word = task + 'LP' + str(number) + 'Plot.png'
        xValues = []
        yValues = []
        for y in learningProblems[x]:
            yValues.append(y[len(y) - 1])
        #
        for y in range(0, len(yValues)):
            number = y + 1
            xValues.append(number)   
        #
        xValues.insert(0,0)
        yValues.insert(0,0)
        plt.plot(xValues, yValues)
        plt.xlabel('epoch # of learning')
        plt.ylabel('# of errors made on training data')
        plt.title(titles[x])
        plt.savefig(word)
        plt.clf()
    #
       
#

def main():
   
    '''
    if a user provides < 3 command-line arguments, he/she
    will be notified of how to use python4.py and the 
    program will terminate  
    '''
    
    if len(sys.argv) < 3:
        print("Usage: project4.py [INPUT FILE PATH] [LEARNING RATE]")
        sys.exit()
    #
    
    # sys.argv[1] is a relative or absolute path to an input file 
    input_path = sys.argv[1]
        
    # sys.argv[2] represents a learning rate 
    learningRate = float(sys.argv[2])
    
    # possibleTasks is a list of task numbers 
    possibleTasks = [2, 3.1, 3.2, 3.3, 4.1, 4.2]
    
    os.system('rm D2/* > /dev/null 2>&1')
    os.system('rm D3/* > /dev/null 2>&1')
    os.system('rm D4/* > /dev/null 2>&1')
    os.system('rm -d D2 > /dev/null 2>&1')
    os.system('rm -d D3 > /dev/null 2>&1')
    os.system('rm -d D4 > /dev/null 2>&1')
    
    os.system('mkdir D2')
    os.system('mkdir D3')
    os.system('mkdir D4')
    
    # for loop below creates ALL epoch stats files and plots needed for the project
    for taskNum in possibleTasks:
        
        processed_data = []
        percWeights = []
        
        if((taskNum == 4.1) | (taskNum == 4.2)):
            
            '''
            if you want to do task 4.1 or 4.2, you would have to shuffle data from 
            file provided by input_path 
            '''
            
            experiment.shuffleData(input_path)
            processed_data = process_file('shuffledData.data')
            os.system('rm shuffledData.data')
            sizeOfWeightVector = len(processed_data[list(processed_data)[0]][0])
            percWeights = experiment.getInitWeightVector(sizeOfWeightVector, 4)
            percWeights[0] = 0
            
        else:
            
            # process data from file provided by input_path 
            
            processed_data = process_file(input_path)   
            sizeOfWeightVector = len(processed_data[list(processed_data)[0]][0])
            percWeights = experiment.getInitWeightVector(sizeOfWeightVector, taskNum)
            percWeights[0] = 0
            
        #
        
        nameOfEpochFile = 'T' + str(taskNum) + 'EpochStatFile.txt'
        task = 'T' + str(taskNum)
        folder = ''
        
        if(int(taskNum) == 2):
           folder = 'D2/'
        elif(int(taskNum) == 3):
           folder = 'D3/'
        elif(int(taskNum) == 4):
           folder = 'D4/'   
        #
        
        nameOfEpochFile = folder + nameOfEpochFile
        task = folder + task
        
        createEpochStatFile(processed_data, learningRate, percWeights, nameOfEpochFile)
        createPlotFile(processed_data, learningRate, percWeights, task)
        
    #
    
if __name__ == "__main__":
    
    main()
    
#
