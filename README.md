# python-challenge-1
python-challenge-1

## Solution provided in
  menu-Aromando.py

## Background
You'll be designing an interactive ordering system from a food truck menu, using the skills you've learned in Python so far.

## Files
Download the following files to help you get started:

Module 2 Challenge files
<br>M2_Starter_Code
<br>      menu.py

## Before You Begin
> [!Note]
> Before starting the assignment, be sure to complete the following steps:
>
>Create a new repository for this project called python-challenge-1. Do not add this homework assignment to an existing repository.
>
>Clone the new repository to your computer.
>
>Inside your local Git repository, add the starter file menu.py from your file downloads.
>
>Push these changes to GitHub or GitLab.

## Challenge Instructions
The starter code provided includes the code for printing the menu for the customer, which was part of one of your Day 3 activities. You will be adapting this menu to allow customers to place an order, which includes storing the customer's order and printing the receipt with the total price of all items ordered. The starter code includes comments, which you may use as a guide for the steps you need to add.

## Order System
> [!Note]
>Create an empty list. This list will later store a customer's order in dictionary format, as follows:
>
> [
><br>{
><br>    "Item name": "string",
><br>    "Price": float,
><br>    "Quantity": int
><br>  },
><br>  {
><br>    "Item name": "string",
><br>    "Price": float,
><br>    "Quantity": int
><br>  },
><br>]
>After the sub-menu is printed, prompt the customer to enter their selection from the menu, saving it as a variable menu_selection.
>
>Use input validation to check if the customer input menu_selection is a number. If it isn't, print an error message. If it is a number, convert the input to an integer and use it to check if it is in the keys of menu_items.
>
>If the user input is not in the menu_items keys, print an error. Otherwise, perform the following actions:
>
>Get the item name from the menu_items dictionary and store it as a variable.
>
>Ask the customer for the quantity of the menu item, using the item name variable in the question, and let them know that the quantity will default to 1 if their input is invalid. Save their answer as a variable called quantity.
>
>Check that the customer input is a number. If it isn't, set the quantity to the value 1. If it is a number, convert the variable to an integer.
>
>Append the customer's order to the order list in dictionary format with the following keys: "Item name", "Price", and "Quantity. You will need this information to print the receipt at the end of the order. The price should be found in the menu_items dictionary.
>
>Inside the continuous while loop that prompts the customer if they would like to keep ordering, write a match:case statement that checks for y or n (upper or lowercase), and includes a default option if neither letter is entered by the customer. The following actions should be performed for each case:
>
>y: Set the place_order variable to True and break from the continuous while loop.
>
>n: Set the place_order variable to False, print "Thank you for your order", and break from the continuous while loop.
>
>Default: Tell the customer to try again because they didn't type a valid input.
>

## Order Receipt
Create a for loop to loop through the order list.

Inside the loop, save the value of each key as their own variable: item_name, price, and quantity.

Calculate the number of empty spaces that should be added to the display so that the receipt uses the following format:

Item name                 | Price  | Quantity
--------------------------|--------|----------
Apple                     | $0.49  | 1
Tea - Thai iced           | $3.99  | 2
Fried banana              | $4.49  | 3
Create the space strings as their own variables using string multiplication.

Print the line for the receipt using the format in Step 8.

Upon exiting the for loop, use list comprehension and sum() to calculate the total price of the order and display it to the customer. Make sure you multiply the price by the quantity in your list comprehension.

## Hints and Considerations
Consider what you've learned so far. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through data structures, and you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.

If you're struggling with how to start, consider writing out the steps of the process using pseudocode.

Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

# Requirements
## Order System (54 points)
> [!IMPORTANT]
> An order list is initialized. (2 points)
>
>User is prompted for their menu item selection and it's saved as a variable menu_selection. (4 points)
>
>User input menu_selection is checked as a number and an error is printed if it is not. (4 points)
>
>menu_selection is converted to an integer. (2 points)
>
>An if-else statement is used to check if menu_selection is in the menu_items keys, and an error is printed if it isn't. (4 points)
>
>The item name of the customer's selection is extracted from the menu_items dictionary and stored as a variable. (4 points)
>
>The customer is prompted for a quantity of their item selection and the value defaults to 1 if the customer does not input a valid number. (10 points)
>
>The customer's selected item, price, and quantity are appended to the order list in dictionary format. (10 points)
>
>A match-case statement is used to check if the customer would like to keep ordering, and performs the correct actions for y, n, and default cases. (10 points)
>
>The match-case statement converts the use input to lowercase or uppercase before checking the case. (4 points)
>

## Order Receipt (46 points)
> [!IMPORTANT]
> A for loop is used to loop through the order list. (10 points)
>
>The value of each key in each order dictionary is saved as a variable. (6 points)
>
>The number of formatting spaces are correctly calculated. (6 points)
>
>Space strings are created using string multiplication. (4 points)
>
>The customer's order is printed with the item name, price, and quantity. (6 points)
>
>List comprehension is used to calculate the total price of the order. (10 points)
>
>The total price of the order is printed to the screen. (4 points)
>
