def Convert(deg, output_type):
    deg_num = float(deg[0 : len(deg)-1])
    print(output_type)
    if deg[len(deg)-1] == "F":
        if output_type.lower() == "fahrenheit":
            return deg_num
        if output_type.lower() == "celcius":
            return (deg_num - 32) * (5/9)
        if output_type.lower() == "kelvin":
            return ((deg_num * (5/9) + 273.15))
    elif deg[len(deg)-1] == "C":
        if output_type.lower() == "fahrenheit":
            return (deg_num * 1.8) + 32
        if output_type.lower() == "celcius":
            return deg_num
        if output_type.lower() == "kelvin":
            return (deg_num + 273.15)
    elif deg[len(deg)-1] == "K":
        if output_type.lower() == "fahrenheit":
            return (((deg_num - 273.15) * 1.8) + 32)
        if output_type.lower() == "celcius":
            return (deg_num - 273.15)
        if output_type.lower() == "kelvin":
            return deg_num


continuing = True

while continuing == True:
    input_temp = input("Hello User, Please input your tempurature, followed by the letter of the tempurature you are using, for example 32 degrees celcius would be 32C, fahrenheit would be 32F, and kelvin would be 32K. ")
    convert_type = input("Which type of tempurature would you like to convert to? Fahrenheit, Celcius, or Kelvin? ")
    result = Convert(input_temp, convert_type)
    print(f"{input_temp} is {result} degrees in {convert_type}")
    keep_going = input("Would you like to convert another value(yes/no) ")
    if keep_going.lower == "no":
        break

print("Goodbye")