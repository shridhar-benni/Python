# OR and AND unidentified errors
This folder contains the OR and AND unidentified errors I encountered in Python programming.

## Introduction
When we are programming we depend on the interpreter to identify errors, but sometimes even the interpreter fails to identify this error. for example, if we define a function to compare two conditions using OR or AND, we mistype any variable and use an undeclared variable instead of a declared variable, we expect the interpreter to through the error, but this assumption may not be true every time, let's see in details section.

## details 

### AND
function():<br>
  if True or error:<br>
    #operations<br>
  else:<br>
    #operations<br>

* If the above function is caller there will be no error, inspite of not declaring error variable. 
* This is because when we are comparing two condition with OR if first contion true second condition dosen't matter.
* because of this behaiour operations under the is condition will be executed.



