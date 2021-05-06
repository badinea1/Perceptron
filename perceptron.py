import math

'''
Vihan Patel
Gordon Petry
Amulya Badineni
Yuriy Deyneka
'''

#computes perceptron output using a feature vector and a weight vector -
def getPerceptronOutput(percWeights, featureVector):
    
    '''
    input: percWeights is a list of weights for a perceptron, featureVector is a list of numerical features -
    output: 1 or -1 -
    '''
    
    total = 0
    
    for x in range(0, len(featureVector)):
        product = percWeights[x] * featureVector[x]
        total = total + product
    #
    
    if(total > 0):
        return 1
    #
    
    return -1

#

#updates perceptron weights if a perceptron incorrectly classifies a training example -
def updatePerceptronWeights(learningRate, percWeights, featureVector, targetOutput):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, 
    featureVector is a list of numerical features, targetOutput is the expected 
    perceptron output -
    output: a list containing updated weights for a perceptron -
    '''
            
    perceptronOutput = getPerceptronOutput(percWeights, featureVector)
    copyOfPercWeights = percWeights.copy()
    
    for x in range(0, len(copyOfPercWeights)):
        deltaWeight = featureVector[x] * (targetOutput - perceptronOutput) * learningRate
        copyOfPercWeights[x] = copyOfPercWeights[x] + deltaWeight
    #
      
    return copyOfPercWeights
    
#

#makes one pass through a training set in order to learn perceptron weights -
def performOneEpoch(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, trainingSet is a two dimensional list where
    each element represents a training example -
    output: returns [currWeights, numOfErrors], where currWeights is a list that represents perceptron weights that are learned after performing
    an epoch of learning and numOfErrors is the # of training examples the perceptron incorrectly classifies while performing an epoch of 
    learning -
    '''
    
    numOfErrors = 0
    currWeights = percWeights.copy()
    
    '''
    Format of each element in trainingSet: [x_1, ..., x_n, targetOutput]
    -> targetOutput is a 1 or -1
    -> x_1 to x_n represent numeric features -
    '''
     
    for item in trainingSet:
        
        '''
        Each instance of training is partitioned into two parts:
        featureVector (first part) -> vector of numeric features
        targetOutput (second part) -> label for the instance of training -
        '''
        
        featureVector = item[0: len(item) - 1] 
        targetOutput = item[len(item) - 1]
        perceptronOutput = getPerceptronOutput(currWeights, featureVector)
        if(targetOutput != perceptronOutput):
            currWeights = updatePerceptronWeights(learningRate, currWeights, featureVector, targetOutput)
            numOfErrors += 1
        #
    #
        
    return [currWeights, numOfErrors]
    
#

#records information about every epoch of learning done by a perceptron on a training set -
def learnFromDataSet(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron,
    trainingSet is a two dimensional list where each element represents an instance of 
    training -
    output: a list in which the kth element will contain information about the kth
    epoch of learning which takes place -
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
           
           '''
           Suppose the # of times a perceptron incorrectly classifies a training
           example while performing an epoch of learning is H. If H is 0, then 
           the perceptron will stop learning. If H > 0, the perceptron stops 
           learning when it will incorrectly classify at least H + 1 training 
           examples during the next epoch of learning. -
           '''
           
           break
            
        else:
           copyOfPercWeights = newWeights
           numOfErrors = newNumOfErrors
           array.append(newResult)
        #
    #
   
    return array
   
#
