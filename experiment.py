import math
import random

#initializes a weight vector for tasks 2, 3.1, 3.2, 3.3
def getInitWeightVector(sizeOfWeightVector, taskNum):
  
    '''
    input: sizeOfWeightVector represents the size of weight vector that needs to be initialized, taskNum represents a task number
    output: a list of weights
    '''
    
    array = []
    
    #for task 2, create a weight vector that has 0s ONLY
    if(taskNum == 2):
       array = [0] * sizeOfWeightVector
        
    #for task 3.1, create a weight vector that has 1s ONLY
    elif(taskNum == 3.1):
       array = [1] * sizeOfWeightVector
        
    #for tasks 3.2 and 3.3, create a weight vector that has decimals greater than 0 and less than 1
    elif(taskNum == 3.2 | taskNum == 3.3):
       for x in range(0, sizeOfWeightVector):
           number = random.random()
           array.append(number)
       #
    #
    
    return array
    
#

def shuffleData(fileName):
  
    pass

#
