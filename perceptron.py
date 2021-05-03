import math

def getPerceptronOutput(percWeights, trainingEx):
    
    '''
    Used to get a perceptron output for a training example

    Arguments:
        percWeights : [weight] : List of weights for a perceptron
        trainingEx : [x] : List of examples in a training example

    Returns: 
        Perceptron output for training example
    '''

    total = 0
        
    for x in range(0, len(percWeights)):
        product = percWeights[x] * trainingEx[x]
        total = total + product
    #
    
    return total

#

def updatePerceptronWeights(learningRate, percWeights, trainingEx, targetOutput):
    
    '''
    Updates weights for a perceptron if it incorrectly classifies a training example

    Arguments:
        learningRate : float
        percWeights : [weight] : list of weights for a perceptron, 
        trainingEx : [x] : List of examples in a training example
        targetOutput : float : The expected perceptron output for a training example

    Returns:
        A list containing updated weights for a perceptron
    '''
            
    perceptronOutput = getPerceptronOutput(percWeights, trainingEx)
    
    for x in range(0, len(percWeights)):
        deltaWeight = trainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        percWeights[x] = percWeights[x] + deltaWeight
    #
  
    return percWeights
    
#

def performOneEpoch(learningRate, percWeights, trainingEx, targetOutput):
    
    '''
    Performs an epoch of learning

    Arguments:
        learningRate : float
        percWeights : [weight] : list of weights for a perceptron
        trainingEx : [[item,],] : contains training data
        targetOutput : int

    Returns: [newWeights, numOfErrors] : 
        newWeights : [weight] : a list that results from updating percWeights during an epoch of learning
        numOfErrors : # of training examples the perceptron incorrectly classifies
    '''
    
    numOfErrors = 0
     
    for example in trainingEx:
        weights = updatePerceptronWeights(learningRate, percWeights, example, targetOutput)
        if(weights != percWeights):
           numOfErrors = numOfErrors + 1
        #
        percWeights = weights
    #
    
    newWeights = percWeights
    
    return [newWeights, numOfErrors]
    
#

def learnFromDataSet(learningRate, percWeights, trainingEx, targetOutput):
    
    '''
    Records information about every epoch of learning necessary for a training set

    Arguments:
        learningRate : float
        percWeights : [weights] : a list of weights for a perceptron,
        trainingEx : [[item,],] : contains training data
        targetOutput : int
    Returns:
        a list in which the kth element will contain information about the kth
        epoch of learning which takes place
    '''
 
    result = performOneEpoch(learningRate, percWeights, trainingEx, targetOutput)
    array = [result]
    percWeights = result[0]
    numOfErrors = result[1]
   
    while(True):
        newResult = performOneEpoch(learningRate, percWeights, trainingEx, targetOutput)
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
