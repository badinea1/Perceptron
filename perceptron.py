import math

#NOTE: if there are bugs, which I don't believe there might be, just let me know

def calcPredictedVal(weights, trainingEx):
    
    copyOfTrainingEx = [1]
    
    for x in trainingEx:
        copyOfTrainingEx.append(x)   
    #

    total = 0
        
    for x in range(0, len(weights)):
        product = weights[x] * copyOfTrainingEx[x]
        total += product
    #
    
    return total

#

def updatePerceptronWeights(learningRate, weights, trainingEx, targetOutput):
            
    perceptronOutput = calcPredictedVal(weights, trainingEx)
    copyOfTrainingEx = [1]
    
    for x in trainingEx:
        copyOfTrainingEx.append(x)   
    #
            
    for x in range(0, len(weights)):
        deltaWeight = copyOfTrainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        weights[x] = weights[x] + deltaWeight
    #
  
    return weights
    
#

def performOneEpoch(learningRate, weights, trainingSet):
    
    numOfErrors = 0
     
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        newWeights = updatePerceptronWeights(learningRate, weights, trainingEx, targetOutput)
        if(newWeights != weights):
           numOfErrors = numOfErrors + 1
        #
        weights = newWeights
    #
    
    return [weights, numOfErrors]
    
#
