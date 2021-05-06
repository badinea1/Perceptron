import math

'''
Vihan Patel
Gordon Petry
Amulya Badineni
Yuriy Deyneka
'''

#used to get a perceptron output for a training example
def getPerceptronOutput(percWeights, trainingEx):
    
    '''
    input: percWeights is a list of weights for a perceptron, trainingEx is a training example
    output: perceptron output for training example
    '''
    
    total = 0
    
    for x in range(0, len(trainingEx)):
        product = percWeights[x] * trainingEx[x]
        total = total + product
    #
    
    if(total > 0):
        return 1
    #
    
    return -1

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
    copyOfPercWeights = percWeights.copy()
    
    for x in range(0, len(copyOfPercWeights)):
        deltaWeight = trainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        copyOfPercWeights[x] = copyOfPercWeights[x] + deltaWeight
    #
      
    return copyOfPercWeights
    
#

#performs an epoch of learning
def performOneEpoch(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, trainingSet contains training data
    output: returns [currWeights, numOfErrors], where currWeights is a list that results from updating percWeights during an epoch
    of learning and numOfErrors is the # of training examples the perceptron incorrectly classifies
    '''
    
    numOfErrors = 0
    currWeights = percWeights.copy()
    
    '''
    Format of each element in trainingSet: [x_1, ..., x_n, targetOutput]
    -> targetOutput is a 1 or -1
    -> x_1 to x_n are used by a perceptron to calculate a # that will be compared with targetOutput when updating perceptron weights
    '''
     
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        perceptronOutput = getPerceptronOutput(currWeights, trainingEx)
        if(targetOutput != perceptronOutput):
            currWeights = updatePerceptronWeights(learningRate, currWeights, trainingEx, targetOutput)
            numOfErrors += 1
        #
    #
        
    return [currWeights, numOfErrors]
    
#

#records information about every epoch of learning necessary for a training set
def learnFromDataSet(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron,
    trainingSet contains training data
    output: a list in which the kth element will contain information about the kth
    epoch of learning which takes place
    '''
    
    copyOfPercWeights = percWeights.copy()
    result = performOneEpoch(learningRate, copyOfPercWeights, trainingSet)
    array = [result]
    copyOfPercWeights = result[0]
    numOfErrors = result[1]
   
    while(True):
        newResult = performOneEpoch(learningRate, copyOfPercWeights, trainingSet)
        newWeights = newResult[0]
        newNumOfErrors = newResult[1]
        if((newNumOfErrors > numOfErrors) | (numOfErrors == 0)):
           break
        else:
           copyOfPercWeights = newWeights
           numOfErrors = newNumOfErrors
           array.append(newResult)
        #
    #
   
    return array
   
# 
