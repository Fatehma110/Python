from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, get_temperature_info

# Test conversions
temp_c = 25
temp_f = 77

print(f"Converting {temp_c}°C to Fahrenheit: {celsius_to_fahrenheit(temp_c):.1f}°F")
print(f"Converting {temp_f}°F to Celsius: {fahrenheit_to_celsius(temp_f):.1f}°C")

# Using the info function
print(get_temperature_info(100, 'c'))
print(get_temperature_info(32, 'f'))