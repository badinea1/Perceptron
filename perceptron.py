import math

#TODO: test the code

def updatePerceptronWeights(learningRate, weights, trainingEx, targetOutput):
            
    perceptronOutput = calcPredictedVal(weights, trainingEx)
            
    for x in range(0, len(weights)):
        deltaWeight = trainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        weights[x] = weights[x] + deltaWeight
    #
  
    return weights
    
#

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

def learnFromDataSet(trainingSet):

    pass

#
