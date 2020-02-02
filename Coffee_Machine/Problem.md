# Problem Description

*Design a **coffee machine** which makes different beverages based on set ingredients. The initialization of the recipes for each drink should be hard-coded, although it should be relatively easy to add new drinks. The machine should display the ingredient stock (+cost) and menu upon startup, and after every piece of valid user input. Drink cost is determined by the combination of ingredients. For example, Coffee is 3 units of coffee (75 cents per), 1 unit of sugar (25 cents per), 1 unit of cream (25 cents per). Ingredients and Menu items should be printed in alphabetical order. If the drink is out of stock, it should print accordingly. If the drink is in stock, it should print "Dispensing: ". To select a drink, the user should input a relevant number. If they submit "r" or "R" the ingredients should restock, and "q" or "Q" should quit. Blank lines should be ignored, and invalid input should print an invalid input message.*

## Class Recepie
    - ingredients needed [] with their units
    - prices of each from Price class
    - total price

    1. object Coffee
        - ingredients needed Unique
        - prices of each from Price class
        - total price

    2. object Tea
        - ingredients needed Unique
        - prices of each from Price class
        - total price

    3. object milk
        - ingredients needed Unique
        - prices of each from Price class
        - total price

## Class Price
    - ingredient List/Array 
    - getter and setter of prices of each ingredients

## Class Machine (Alphabetical order) (extends Recepie)
    - Display Ingredient Stock (method)
        1. Coffee 40 units - 75 CpU
        2. Suger 100 units - 25 CpU
        3. Water 500 units - 
        4. Cream 30 units - 25 CpU

    - Switch options:()
        1. Coffee
        2. Tea
        .
        .
        r/R ReStock
        q/Q Quit

    - On selecting switch option
        - if out of stock - print out of stock
        - if instock - print dispensing
        - invalid ip - print invalid
