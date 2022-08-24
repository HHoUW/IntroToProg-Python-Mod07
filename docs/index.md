Exception Handling and Pickling
===============================



Introduction
------------
In this report, I will give an overview of Exception Handling and Pickling in Python.  I will go over a Python script I created to demonstrate these two concepts.  The program presents the user with two separate demos, one for each concept that the user can choose to view.



Exception Handling
------------------

<p>In Python, errors that occur during code execution are called exceptions.  When exceptions occur, Python stops the program and displays an error message detailing the exception (Figure 1).  There are a of number exception types.  A few common ones are: 

+ •	TypeError - occurs when an operation is applied to objects of inappropriate types.
+ •	ValueError - occurs when an operation receives an argument that has the right type but an inappropriate value.
+ •	ZeroDivisionError – occurs when the second argument of a division operation is zero.</p>


<img src="A07Fig1.png" alt="alt text" title="Figure 1" />
<p>Figure 1: Example of a Python error message when a TypeError exception occurs.</p>


<p>Exception handling is used to catch and handle the errors so that the program does not end abruptly and allows the program to continue running.  This is accomplished with the try and except block.  Python executes code following the try statement and if any exceptions occur while running this code, instead of stopping the program, Python executes the code following the except statement as a response to the exceptions in the preceding try clause. (Figure 2)</p>

<img src="A07Fig2.png" alt="alt text" title="Figure 2" />
<p>Figure 2: Try...Except block for exception handling.  Image from RealPython.com.</p>


<p>
  
</p>

text here






