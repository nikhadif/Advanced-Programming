
"""Firstly, import the numpy to the program. Then, the formula for the conversion of Celcius to Fahrenheit is celcius*1.8=32."""

from numpy import random

def celcius_to_fahrenheit(celcius_float):
    """Convert Celcius to Fahrenheit"""
    return celcius_float*1.8+32
    
 
print("Convert Celcius to Fahrenheit.")

x=random.rand(5)  #to generate random numbers 1 row 5 columns

celcius_to_fahrenheit(x)

y= celcius_to_fahrenheit(x)

print("THe value of fahrenheit are ", y)
