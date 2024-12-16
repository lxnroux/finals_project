print("Fahrenheit to Celsius Converter Program")

fahrenheit = eval(input("Enter temperature in Fahrenheit --> : "))

celsius = ((fahrenheit - 32) * 5) / 9

print(f"{fahrenheit} degrees Fahrenheit converted to Celsius is {round(celsius, 2)} degrees")
