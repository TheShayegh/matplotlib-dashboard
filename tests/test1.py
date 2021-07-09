import matplotlib.pyplot as plt
from matplotlib_dashboard import MatplotlibDashboard
import numpy as np
from PIL import Image

plt.figure(figsize=(10,10))

dashboard = MatplotlibDashboard([
    ['red','red','red','red'],
    ['g3D','g3D',None,'blue'],
    ['g3D','g3D','im','blue'],
], wspace=0.5, hspace=0.5)

dashboard['red'].plot(np.random.rand(200), color='red')
dashboard['red'].set_ylabel('y')
dashboard['red'].set_xlabel('x')
dashboard['red'].set_title('red plot')

dashboard['blue'].bar(['A','B','C'], [10,35,17], color='blue')
dashboard['blue'].set_ylabel('freq')
dashboard['blue'].set_xlabel('label')
dashboard['blue'].set_title('blue bar')

dashboard['im'].imshow(Image.open('test1.jpeg'))
dashboard['im'].get_xaxis().set_ticks([])
dashboard['im'].get_yaxis().set_ticks([])
dashboard['im'].set_title('cat image')

z = ((5-np.arange(100)%10)**3).reshape(10,10)
x, y = np.meshgrid(np.arange(z.shape[0]), np.arange(z.shape[1]))
dashboard['g3D'].plot_surface(x, y, z, color='green')
dashboard['g3D'].set_ylabel('x')
dashboard['g3D'].set_xlabel('y')
dashboard['g3D'].set_zlabel('z')
dashboard['g3D'].set_title('green surface')

plt.show()