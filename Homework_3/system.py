# Copyright 2017 Michael Graziano mjgrazia@bu.edu

import numpy as np

x_str = input()
h_str = input()

x_list = [float(item) for item in x_str.split(" ")]
h_list = [float(item) for item in h_str.split(" ")]

x_array = np.array(x_list)
h_array = np.array(h_list)

y_array = np.convolve(x_array, h_array)

for i in range(y_array.size):
    if i != y_array.size - 1:
        print("{:f} ".format(y_array[i]), end="")
    else:
        print("{:f}".format(y_array[i]))
