# OR and AND unidentified errors
This folder contains the OR and AND unidentified errors I encountered in Python programming.

## Introduction
When we are programming we depend on the interpreter to identify errors, but sometimes even the interpreter fails to identify this error. for example, if we define a function to compare two conditions using OR or AND, we mistype any variable and use an undeclared variable instead of a declared variable, we expect the interpreter to through the error, but this assumption may not be true every time, let's see in the details section. example .ipynb file is uploaded for reference.

## details 

### OR
function():<br>
&nbsp;if True or error:<br>
\t\t#operations<br>
\telse:<br>
\t\t#operations<br>

* If the above function is called there will be no error, despite not declaring the error variable. 
* This is because when we are comparing two conditions with OR if the first condition is true second condition doesn't matter.
* because of this behavior operations under the "if" condition will be executed.


### AND
function():<br>
\tif False and error:<br>
\t\t#operations<br>
\telse:<br>
\t\t#operations<br>

* If the above function is called there will be no error, despite not declaring the error variable. 
* This is because when we are comparing two conditions with AND if the first condition is false second condition doesn't matter.
* because of this behavior operations under the "else" condition will be executed.

  

