
def celcius_to_fahrenheit(celcius_float):
    """Convert Celcius to Fahrenheit"""
    return celcius_float*1.8+32

print("Convert Celcius to Fahrenheit.")
celcius_float=float(input("Enter a Celcius temp: "))

fahrenheit_float=celcius_to_fahrenheit(celcius_float)

print(celcius_float, "converts to ", fahrenheit_float, "Fahrenheit")
