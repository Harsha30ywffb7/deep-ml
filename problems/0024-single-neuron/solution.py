import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    features = np.array(features)
    weights = np.array(weights)
    labels = np.array(labels)
    probabilities=[]

    for i in range(len(features)):
        z = np.dot(features[i], weights) + bias
        probabilities.append(1/(1+math.exp(-z)))
    
    probabilities = [round(p, 4) for p in probabilities]
    predicted = np.array(probabilities)
    diff = predicted - labels
    mse = np.sum(np.dot(diff, diff))/len(labels)

    return probabilities, round(mse, 4)