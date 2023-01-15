# Gradient Descent Visualization
This repository contains a Python script that uses the Plotly library to create a 3D surface plot of a two-dimensional function, f(x, y), and a 3D scatter plot of the optimization path of the gradient descent algorithm. The function being optimized is defined as x^2 + y^2, and the gradient of this function is calculated in the grad(x, y) function. The gradient descent algorithm starts at a specified point (x0, y0) and iterates n_iter times with a learning rate of alpha. The interact function from the ipywidgets library is used to create sliders that allow the user to adjust the parameters of the algorithm and update the path of the optimization in the 3D scatter plot accordingly.

## Dependencies
* Dependencies
* plotly
* numpy
* ipywidgets
* Usage

## To run the script
_open the terminal and navigate to the repository's directory. Then use the command below:_

```python3 main.py```

The script will open a window with the 3D surface plot and the 3D scatter plot, and the sliders to adjust the parameters of the algorithm.

## Conclusion
This code is a great way to visualize the optimization path of the gradient descent algorithm in 3D and understand the impact of different parameters like learning rate and iteration on the optimization process.

## Note
This code is developed and tested on Google Colab, some modification may be required to run on other platforms.

_This README was written by Chat-GPT_
