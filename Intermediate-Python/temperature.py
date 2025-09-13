#Question: Create a custom module called temperature.py with functions to convert between Celsius 
#and Fahrenheit. Then import and use it in another file.

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def get_temperature_info(temp, unit):
    """Get formatted temperature information"""
    if unit.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(temp)
        return f"{temp}°C = {fahrenheit:.1f}°F"
    elif unit.lower() == 'f':
        celsius = fahrenheit_to_celsius(temp)
        return f"{temp}°F = {celsius:.1f}°C"
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit"

