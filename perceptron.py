import math

def updatePerceptronWeights(learningRate, weights, trainingEx, perceptronOutput, targetOutput):
        
    for x in range(1, len(weights)):
        deltaWeight = trainingEx[x - 1] * (targetOutput - perceptronOutput) * learningRate
        weights[x] = weights[x] + deltaWeight
    #
  
    return weights
    
#

