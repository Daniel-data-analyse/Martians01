while True:
    player = float(input("enter a temperature: "))
    player1 = input("enter a temperature unit: ").capitalize()
    tries = 1
    def Celsius_calculator():
        if player1 == "Fahrenheit":
            print(f"{player} {player1} temperature in Celsius is {(player - 32) *(5/9)}C")
        if player1 == "Kelvin":
           print(f"{player} {player1} temperature in Celsius is {player - 273.15}C")
        if player1 == "Reaumur":
           print(f"{player} {player1} temperature in Celsius is {player *(5/4)}C")
        if player1 == "Celsius":
           print("Your input is already in Celsius!")
           tries = tries + 1
           if tries == 3:
            print("Are you a stupid guy?")
        if player1 != "Kelvin" and player1 != "Reaumur" and player != "Fahrenheit" and player1 != "Celsius":
            print("Invalid input")
            print("Please, try again!")

    Celsius_calculator()