import numpy as np

training_target = np.zeros((1,2))
formatted_target = np.zeros((1,2))
formatted_target[0][1] = 1.
training_target = np.concatenate((training_target, formatted_target), axis=0)

print(training_target)