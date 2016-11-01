#Funny calculator script

An attempt to make a Polish notation calculator.

The whole script is located in the file `calculator.py`.

The function `calulate` takes one argument which is then interpreted.

The calculator interprets input from right to left. This means that the precedence of operators go from right to left. E.g input `+ 1 2 * 3 4` gives answer `15.0` and input `* 1 2 + 3 4` gives answer `14.0`. Minus operator (`-`) can be used as a unary operator. Factorial (`!`) is naturally unary.
