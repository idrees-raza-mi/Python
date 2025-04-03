# covert celcius to fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit')