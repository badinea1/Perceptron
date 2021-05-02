import math

#NOTE: if there are bugs, which I don't believe there might be, just let me know

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
    
    for x in range(0, len(percWeights)):
        deltaWeight = copyOfTrainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        percWeights[x] = percWeights[x] + deltaWeight
    #
  
    return percWeights
    
#

#performs an epoch of learning
def performOneEpoch(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, trainingSet is a list of training examples
    output: returns [newWeights, numOfErrors], where newWeights is a list that results from updating percWeights during an epoch
    of learning and numOfErrors is the # of training examples the perceptron incorrectly classifies
    '''
    
    numOfErrors = 0
     
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
