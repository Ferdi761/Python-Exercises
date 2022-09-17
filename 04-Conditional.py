from re import X


x = input("how's the weather today: ")
temp = float(x)

if temp < 24:
    print("it's too cold in here")

elif temp >= 24 and temp <= 34:
    print("Such a nice weather")

else:
    print("the weather is hot as hell")
