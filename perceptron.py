import math

#NOTE: THIS FILE MAY HAVE BUGS, I MIGHT NEED TO FIX THEM

#used to get a perceptron output for a training example
def getPerceptronOutput(percWeights, trainingEx):
    
    '''
    input: percWeights is a list of weights for a perceptron, trainingEx is a training example
    output: perceptron output for training example
    '''
    
    copyOfTrainingEx = [1]
    
    for x in trainingEx:
        copyOfTrainingEx.append(x)   
    #

    total = 0
        
    for x in range(0, len(percWeights)):
        product = percWeights[x] * copyOfTrainingEx[x]
        total = total + product
    #
    
    return total

#

#updates weights for a perceptron if it incorrectly classifies a training example
def updatePerceptronWeights(learningRate, percWeights, trainingEx, targetOutput):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, 
    trainingEx is a training example, targetOutput is the expected perceptron output for
    a training example
    output: a list containing updated weights for a perceptron
    '''
            
    perceptronOutput = getPerceptronOutput(percWeights, trainingEx)
    copyOfTrainingEx = [1]
    
    for x in trainingEx:
        copyOfTrainingEx.append(x)   
    #
    
    copyOfPercWeights = []
    
    for x in percWeights:
        copyOfPercWeights.append(x)   
    #
    
    for x in range(0, len(copyOfPercWeights)):
        deltaWeight = copyOfTrainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        copyOfPercWeights[x] = copyOfPercWeights[x] + deltaWeight
    #
  
    return copyOfPercWeights
    
#

#performs an epoch of learning
def performOneEpoch(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, trainingSet contains training data
    output: returns [newWeights, numOfErrors], where newWeights is a list that results from updating percWeights during an epoch
    of learning and numOfErrors is the # of training examples the perceptron incorrectly classifies
    '''
    
    numOfErrors = 0
    
    '''
    Format of each element in trainingSet: [x_1, ..., x_n, targetOutput]
    -> targetOutput is a 1 or -1
    -> x_1 to x_n are used by a perceptron to calculate a # that will be compared with targetOutput when updating perceptron weights
    '''
     
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        weights = updatePerceptronWeights(learningRate, percWeights, trainingEx, targetOutput)
        if(weights != percWeights):
           numOfErrors = numOfErrors + 1
        #
        percWeights = weights
    #
    
    newWeights = percWeights
    
    return [newWeights, numOfErrors]
    
#

#records information about every epoch of learning necessary for a training set
def learnFromDataSet(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron,
    trainingSet contains training data
    output: a list in which the kth element will contain information about the kth
    epoch of learning which takes place
    '''
 
    result = performOneEpoch(learningRate, percWeights, trainingSet)
    array = [result]
    percWeights = result[0]
    numOfErrors = result[1]
   
    while(True):
        newResult = performOneEpoch(learningRate, percWeights, trainingSet)
        newWeights = newResult[0]
        newNumOfErrors = newResult[1]
        if(newNumOfErrors == numOfErrors):
           break
        else:
           percWeights = newWeights
           numOfErrors = newNumOfErrors
           array.append(newResult)
        #
    #
   
    return array
   
#
