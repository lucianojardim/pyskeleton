""" this module is a recommendation of vscode """
import matplotlib.pyplot as plt
import numpy as np


def execute():
    """ This function plots a sinoid """
    # Create a list of evenly-spaced numbers over the range
    x_axis = np.linspace(0, 20, 100)
    plt.plot(x_axis, np.sin(x_axis))  # Plot the sine of each x point
    plt.show()
