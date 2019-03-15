# Nearest-Average-Algorithm
This is a machine learning algorithm I developed on Repl.it
<br>
# How Does It Work?
In this algorithm, the train() function takes in a dictionary of tuples, representing the coordinates and the values. the predict() function takes three arugments, the input coordinate, n, and K. What this algorithm does it that it takes in the input coordinate, find the n number of points that is within K distance away from the input, take those coordinates' values, and finally calculate the average of the values of those points and return it.
<br>
# Input Format
The train() function takes in a dictionary of tuples representing the coordinate and the corresponding value in the form {(x):(y)}. The predict() function takes in arguments in the form predict(input-coordinate, n, K). The input-coordinate should be a tuple within a list, n should be an integer, and K should either be a float or an integer. 
<br>
# Output Format
The output will be a tuple representing the predicted value.
<br>
# Visual Illustration
The below image showed how this algorithm is going to work. In this case, the orange point with represent the input coordinate, the scattered points in the graph will be the coordinates in the input dataset, and the green points will have their value calculated for average. In this example, the n value will be 3
![example-image](https://github.com/JarJuicy/Nearest-Average-Algorithm/blob/master/Untitled2.png)
# Usage Example
Place the src.py file in the code directory
```python
from src import main
learn = main()
learn.train({(1, 1, 1):(4, 6, 9), (5, 6, 7):(3, 4, 5), (6, 6, 5):(2, 4, 5), (6, 5, 6):(2, 3, 5), (5, 6, 6):(2, 7, 5)})
print(learn.predict([(6, 6, 6)], 3, 1.1))
#(2.0, 4.666666666666667, 5.0)
```
<br>
If you have any questions and/or suggestions, feel free to open up an issue or contact me on briansiyuanzheng@gmail.com
<br>
In the near future I will upload this package to PyPI and clean up some messy code and extra comments
<br>
You can visit the live development in [Repl.it](https://repl.it/@BrianZheng1/K-Best-Average-Algorithm)
