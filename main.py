import plotly.graph_objects as go
import numpy as np
from ipywidgets import interact, fixed, widgets

def f(x, y):
    return x**2 + y**2

def grad(x, y):
    dx = 2*x
    dy = 2*y
    return np.array([dx, dy])

x0 = -4
y0 = -4
alpha = 0.1
n_iter = 100

x = y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

x = x0
y = y0
x_list = [x0]
y_list = [y0]
z_list = [f(x0, y0)]

for i in range(n_iter):
    x, y = x - alpha * grad(x, y)[0], y - alpha * grad(x, y)[1]
    x_list.append(x)
    y_list.append(y)
    z_list.append(f(x, y))

fig = go.Figure(data=[go.Surface(z=f(X, Y), x=X, y=Y), go.Scatter3d(x=x_list, y=y_list, z=z_list, mode='markers', marker=dict(size=3, color='red'))])
fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))

def update_plots(alpha, n_iter, x0, y0, fig):
    x = x0
    y = y0
    x_list = [x0]
    y_list = [y0]
    z_list = [f(x0, y0)]

    for i in range(n_iter):
        x, y = x - alpha * grad(x, y)[0], y - alpha * grad(x, y)[1]
        x_list.append(x)
        y_list.append(y)
        z_list.append(f(x, y))

    fig.data[1].x = x_list
    fig.data[1].y = y_list
    fig.data[1].z = z_list
    fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))
    fig.show()
interact(update_plots, alpha=widgets.FloatSlider(min=0,max=1,step=0.01,value=alpha), n_iter=widgets.IntSlider(min=1, max=1000, step=1, value=n_iter), x0=fixed(x0), y0=fixed(y0), fig=fixed(fig))
"""
This code is using the Plotly library to create a 3D surface plot of a two-dimensional function, and a 3D scatter plot of the optimization path of the gradient descent algorithm.
The function f(x, y) is defined as x^2 + y^2, which is the function to be optimized. The gradient of this function is calculated in the grad(x, y) function and is used to update the parameters x, y in the gradient descent algorithm.
A starting point (x0, y0) is defined and the optimization process is repeated n_iter times with a learning rate of alpha.
The interaction is done by the interact function from the ipywidgets library, which creates sliders that allow the user to adjust the parameters of the algorithm.
The update_plots function updates the path of the optimization in the 3D scatter plot accordingly.
"""
