import math

#TODO: test the code

def calcPredictedVal(weights, trainingEx):
    
    copyOfTrainingEx = [1]
    
    for x in trainingEx:
        copyOfTrainingEx.append(x)   
    #

    sum = 0
        
    for x in range(0, len(weights)):
        product = weights[x] * copyOfTrainingEx[x]
        sum += product
    #
    
    return sum

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

def calcMeanSquareError(trainingSet, weights):
    
    totalError = 0
    
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        predictedOutput = calcPredictedVal(weights, trainingEx)
        errorSquared = (targetOutput - predictedOutput) * (targetOutput - predictedOutput)
        totalError = totalError + errorSquared
    #
    
    return totalError / len(trainingSet)
       
#

def performOneEpoch(learningRate, weights, trainingSet):
    
    errors = 0
     
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        newWeights = updatePerceptronWeights(learningRate, weights, trainingEx, targetOutput)
        if(newWeights != weights):
           errors = errors + 1
        #
        weights = newWeights
    #
    
    return [weights, errors]
    
#
