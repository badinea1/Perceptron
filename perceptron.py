import math

'''
Vihan Patel
Gordon Petry
Amulya Badineni
Yuriy Deyneka
'''

#computes perceptron output for an unlabeled training example 
def getPerceptronOutput(percWeights, trainingEx):
    
    '''
    input: percWeights is a list of weights for a perceptron, 
    trainingEx is a list representing an unlabeled training example 
    output: perceptron output for an unlabeled training example 
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

#updates perceptron weights if a perceptron incorrectly classifies an unlabeled training example 
def updatePerceptronWeights(learningRate, percWeights, trainingEx, targetOutput):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, 
    trainingEx is a list representing an unlabeled training example, targetOutput is the expected 
    perceptron output for trainingEx 
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

#makes one pass through a training set in order to learn perceptron weights 
def performOneEpoch(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron, trainingSet is a two dimensional list where
    each element represents an instance of training 
    output: returns [currWeights, numOfErrors], where currWeights is a list that represents perceptron weights that are learned after performing
    an epoch of learning and numOfErrors is the # of training examples the perceptron incorrectly classifies while performing an epoch of 
    learning 
    '''
    
    numOfErrors = 0
    currWeights = percWeights.copy()
    
    '''
    Format of each element in trainingSet: [x_1, ..., x_n, targetOutput]
    -> targetOutput is a 1 or -1
    -> x_1 to x_n are used by a perceptron to calculate a number that will be compared with targetOutput
    when updating perceptron weights 
    '''
     
    for item in trainingSet:
        
        '''
        Each instance of training is partitioned into two parts:
        trainingEx (first part) -> instance of training without the label
        targetOutput (second part) -> label for the instance of training
        '''
        
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

#records information about every epoch of learning done by a perceptron on a training set 
def learnFromDataSet(learningRate, percWeights, trainingSet):
    
    '''
    input: learningRate is a float, percWeights is a list of weights for a perceptron,
    trainingSet is a two dimensional list where each element represents an instance of 
    training 
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
           
           '''
           Suppose we perform an epoch of learning and the # of times
           a perceptron incorrectly classifies a training example is H.
           If H is 0, then the perceptron is done learning. If H > 0, the
           perceptron stops learning when it will incorrectly classify at
           least H + 1 training examples on the next epoch of learning. 
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
