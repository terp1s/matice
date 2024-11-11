Write a Python class that represents a matrix of numbers.

Your class should support the following operations. (Below, m and n represent Matrix objects. ll represents a list of lists. s represents a scalar, i.e. a number.)

Matrix(ll) - create a Matrix object from a list of lists of numbers

m.vals() - return a list of lists of numbers containing the values in this Matrix

m.dims() - return a pair (i.e. tuple) of integers (r, c) with the matrix's dimensions

m + n - add two matrices

m - n - subtract two matrices

m * s - multiply a matrix by a scalar s

m * n - multiply two matrices

m.is_symmetric() - return True if the matrix is symmetric

A matrix's string representation should look like this:

"3 5 2
5 2 8
8 7 4"
Notice that there is no newline at the end of the last row in the string above.

Also define these functions:

zero_matrix(r, c) - return a Matrix of zeroes of dimensions r x c

identity_matrix(n) - return an identity Matrix of dimensions n x n

In all the operations above, you may assume that matrices have compatible dimensions.

Do not read any input or write any output; ReCodEx will call your class's methods to test them.

Important: Your class must be in a source file called matrix.py.

Important: You may not use numpy or any other Python library that provides matrix operations.

Sample usage #1:

> m = Matrix([[2, 3, 4], [5, 6, 7]])
>
> m.vals() 
> [[2, 3, 4], [5, 6, 7]]
>
> m
> 
> 2 3 4
> 
> 5 6 7
> 
> n = Matrix([[1, 2, 3], [2, 3, 4]])
> n
> 1 2 3
> 
> 2 3 4
>
> 
> m + n
> 
> 3 5 7
> 
> 7 9 11
>
> 
> m - n
> 
> 1 1 1
> 
> 3 3 3


Sample usage #2:

>>> m = Matrix([[2, 3], [4, 5]])
>>> m
>>>
>>> 
>>> 2 3
>>> 
>>> 4 5
>>> 
>>> n = Matrix([[1, 2], [3, 4]])
>>> 
>>> n
>>>
>>> 
>>> 1 2
>>> 
>>> 3 4
>>> 
>>> m * 2
>>>
>>> 4 6
>>> 
>>> 8 10
>>> 
>>> m * n
>>> 
>>> 11 16
>>> 
>>> 19 28
>>>
>>> 
>>> n * m
>>> 
>>> 10 13
>>> 
>>> 22 29
>>> 
>>> p = Matrix([[0, 2, 4], [1, 3, 5]])
>>> 
>>> p
>>> 
>>> 0 2 4
>>> 
>>> 1 3 5
>>>
>>> 
>>> p * 2
>>> 
>>> 0 4 8
>>> 
>>> 2 6 10
>>>
>>> 
>>> n * p
>>> 
>>> 2 8 14
>>> 
>>> 4 18 32


Sample usage #3:

>>> m = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
>>>
>>> 
>>> 1 2 3
>>> 
>>>2 3 4
>>> 
>>>3 4 5
>>>
>>> 
>>> m.is_symmetric()
>>> 
>>>True
>>> 
>>> i = identity_matrix(3)
>>> 
>>> i
>>>
>>> 
>>>1 0 0
>>>0 1 0
>>>0 0 1
>>>
>>> 
>>> i.is_symmetric()
>>> 
>>>True
>>> 
>>> m * i
>>> 
>>>1 2 3
>>> 
>>>2 3 4
>>> 
>>>3 4 5
>>> 
>>> zero_matrix(2, 3)
>>> 
>>>0 0 0
>>> 
>>>0 0 0
>>>

Hints:

In your __mul__ method you'll need to test whether the argument is a Matrix or a scalar, to know what kind of multiplication to perform. You can call 'isinstance(x, Matrix)', which returns True if x is a Matrix, otherwise False.

If you multiply matrices with dimensions (a x b) and (b x c), you get a matrix with dimensions (a x c).
