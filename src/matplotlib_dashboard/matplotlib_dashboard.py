import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

class MatplotlibDashboard:
    def __init__(self, positions:list, as3D=[], **args):
        positions = np.array(positions)
        if len(positions.shape) == 1:
            positions = positions.reshape(1,-1)
        positions[positions == None] = 'None'
        self.axes = dict()
        gs = gridspec.GridSpec(*positions.shape, **args)
        for i in np.unique(positions):
            if i == 'None':
                continue
            y,x = np.where(positions == i)
            y_min = y.min()
            y_max = y.max()
            x_min = x.min()
            x_max = x.max()
            grid = gs[y_min:y_max+1, x_min:x_max+1]
            if i in as3D:
                self.axes[i] = plt.subplot(grid, projection='3d')
            else:
                self.axes[i] = plt.subplot(grid)

    def __getitem__(self, name):
        return self.axes[name]