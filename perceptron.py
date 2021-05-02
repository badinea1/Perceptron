import math

def updatePerceptronWeights(learningRate, weights, trainingEx, perceptronOutput, targetOutput):
        
    if(targetOutput == perceptronOutput):
       return weights 
    #
        
    for x in range(0, len(weights)):
        deltaWeight = trainingEx[x] * (targetOutput - perceptronOutput) * learningRate
        weights[x] = weights[x] + deltaWeight
    #
  
    return weights
    
#
