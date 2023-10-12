def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1/2/3/4/5/6): "))

if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == 3:
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius_to_kelvin(celsius)
    print("Temperature in Kelvin:", kelvin)

elif choice == 4:
    kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = kelvin_to_celsius(kelvin)
    print("Temperature in Celsius:", celsius)

elif choice == 5:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    kelvin = fahrenheit_to_kelvin(fahrenheit)
    print("Temperature in Kelvin:", kelvin)

elif choice == 6:
    kelvin = float(input("Enter temperature in Kelvin: "))
    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print("Temperature in Fahrenheit:", fahrenheit)

else:
    print("Invalid choice")
