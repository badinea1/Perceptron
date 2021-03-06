import math
import random
import perceptron
import csv
import os

'''
Gordon Petry
Yuriy Deyneka
Amulya Badineni
Vihan Patel
'''

#initializes a weight vector for tasks 2, 3.1, 3.2, 3.3, 4 
def getInitWeightVector(sizeOfWeightVector, taskNum):
  
    '''
    input: sizeOfWeightVector represents the size of the weight vector that needs to be initialized, taskNum represents a task number 
    output: a list of weights 
    '''
    
    array = []
    taskNum = float(taskNum)
    
    #for tasks 2 and 4, create a weight vector that has 0s ONLY 
    if((taskNum == 2) | (taskNum == 4)):
       array = [0] * sizeOfWeightVector
               
    #for task 3.1, create a weight vector that has 1s ONLY 
    elif(taskNum == 3.1):
       array = [1] * sizeOfWeightVector
        
    #for tasks 3.2 and 3.3, create a weight vector that has decimals greater than 0 and less than 1 
    elif((taskNum == 3.2) | (taskNum == 3.3)):
       for x in range(0, sizeOfWeightVector):
           number = random.random()
           array.append(number)
       #
    #
        
    return array
    
#

#randomly shuffles data from a .data file
def shuffleData(fileName):
    
    '''
    input: fileName is a string that represents an absolute or relative path to a .data file 
    output: a file called shuffledData.data 
    '''
    
    rows = []
  
    with open(fileName, newline='') as csvfile:
        for row in csvfile:
            row = row.rstrip()
            if(len(row) > 0):
                row = row.split(',')
                rows.append(row)    
            #
        #
    #
    
    random.shuffle(rows)
    file = open('shuffledData.csv', 'w')
    obj = csv.writer(file)
    obj.writerows(rows)
    
    os.system('mv shuffledData.csv shuffledData.data')
    
#
