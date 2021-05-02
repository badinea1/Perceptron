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

def learnFromDataSet(trainingSet, learningRate, weights):
            
    for item in trainingSet:
        trainingEx = item[0: len(item) - 1]
        targetOutput = item[len(item) - 1]
        weights = updatePerceptronWeights(learningRate, weights, trainingEx, targetOutput)
    #
            
    return weights

#

def getWeightsFromDataSet(trainingSet, learningRate):

    weights = []
    
    for x in range(0, len(trainingSet[0])):
        weights.append(0)             
    #
            
    while(True):
        newWeights = learnFromDataSet(trainingSet, learningRate, weights)
        if(newWeights == weights):
           return weights               
        #
        weights = newWeights               
    #

#
