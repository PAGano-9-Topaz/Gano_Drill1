# This how you find the area of a Trapezoid
from pyscript import display, document

def adding_numbers(e):
    document.getElementById('output').innerHTML = " "
    Value1 = float(document.getElementById('num1').value)
     # getting value from an input field
    Value2 = float(document.getElementById('num2').value)
     
    Value3 = float(document.getElementById('num2').value)
    area = 0.5 * (Value1 + Value2) * Value3

    display(f'The area of this trapezoid is {area}', target = 'output')

