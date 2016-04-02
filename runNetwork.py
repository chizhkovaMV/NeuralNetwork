# run neural network
import numpy as np
# create training set
X = np.array([  [0,0,1], [0,1,1], [1,0,1], [1,1,1] ])
y = np.array([ [0,0,1,1] ]).T

# set up neural network

from NN_Python import NeuralNetworkBatch

Network = NeuralNetworkBatch()

Network.initializeWeights(3) # this must be the same as input data dimmensions

uuu = Network.updateWeights(X,y,10000,1e-2,1)

import matplotlib.pyplot as plt
plt.plot(uuu)
plt.show()


# now we run network with two layers

from NeuralNetwork_2_Layers import NeuralNetwork_2_Layers

Network_2 = NeuralNetwork_2_Layers()

Network_2.initializeWeights_Layer1(3,4)
Network_2.initializeWeights_Layer2(4)

storeErrorsFinal, storeErrors_1 = Network_2.updateWeights(X,y,10000,1e-2,1)

import matplotlib.pyplot as plt
plt.plot(storeErrorsFinal)
plt.show()

plt.plot(storeErrors_1)
plt.show()


######## THINGS TO DO:

# 1. Implement bold driver algo
# 2. Do that other thing that improves performance
# 3. Implement ROC curve