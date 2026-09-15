import numpy as np
array = np.arange(1, 7).reshape(2, 3)
print("Original array (shape={}):\n{}".format(array.shape, array))
reshaped = array.reshape(3, 2)
print("\nReshaped array (shape={}):\n{}".format(reshaped.shape, reshaped))
flattened = array.flatten()
print("\nFlattened array (shape={}):\n{}".format(flattened.shape, flattened))
reshaped[0, 0] = 99
flattened[0] = 88
print("\nOriginal after changing copies:")
print(array)
print("Reshaped copy:\n", reshaped)
print("Flattened copy:\n", flattened)
