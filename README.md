# Calculator_with_UI
A combination of my calculator with parantheses and a user interface.

A functioning calculator with functionality for parantheses. Input is entered exactly as it would be on a real calculator. Decimal numbers can also be inputted.

For exponents, a^b, for multiplication a*b, for division a/b, for addition a+b, for subtraction a-b, Example of a valid equation would be without quotes "((4-3-2)^2+3-6)-(7+8)^0.5". 

Nested brackets are supported eg (4(3-6))

Seperated brackets are supported eg (4+3)(4+6)^2

The buttons provided are used to enter an equation, inlcluding all numbers, (decimals, negative), every arithhnetic operator.

The equals button will then process the equation and display the answer. It will give error for invalid equations.eg square root of negative numbers, division by zero, incoherent bracket placement.

Tkinter library is used for UI

An exe is provided which has some minor adjustments to the source code namely the addition of icons and resizing of buttons in the UI. Otherwise the code for processing the equations is identical
