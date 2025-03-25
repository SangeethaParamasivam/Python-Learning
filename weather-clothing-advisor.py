#Clothing advisor based on weather condition

temp = int(input("Enter Temperature in celcius: "))


if temp < 10:

    print("It's cold outside wear a sweater!")

elif temp >= 10 and temp <= 25:

    print("It's a mild weather wear a light jacket!")

elif temp > 25:

    print("It's hot outside wear something light!")

else:

    print("Enter proper temperature!")
