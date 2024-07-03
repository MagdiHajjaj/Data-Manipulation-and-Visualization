# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Magdi Hajjaj"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101299841"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-002"

#==========================================#
# Place your script for your text_UI after this line
from sort import *
from load_data import *
from histogram import *
from curve_fit import *

data_loaded = []
Active = True
avaliable_command = "The available commands are:\n    L)oad Data\n    S)ort Data\n    C)urve Fit\n    H)istogram\n    E)xit\n"
while Active:
    print(avaliable_command)
    user_input = input("Please type your command: ")

    if user_input.upper() == "L":
        user_file_name = input("Please enter the name of the file: ")
        user_attribute_name = input("Please enter the attribute to use as a filter: ")
        if user_attribute_name != "All":
            user_attribute_value = input("Please enter the value of the attribute: ")

        data_loaded = calculate_health(load_data(user_file_name, (user_attribute_name, user_attribute_value)))
        print("Data loaded")

    elif user_input.upper() == "S":
        user_attribute_sort = input("Please enter the attribute you want to use for sorting:\n'Agility', 'Armor', 'Intelligence', 'Health': ")
        user_order = input("Ascending (A) or Descending (D) order: ")
        sorted_data = sort(data_loaded, user_order, user_attribute_sort)
        if sorted_data == []:
            print("File not loaded. Please, load a file first.")
        else:
            user_display = input("Data Sorted. Do you want to display the data? (Y or N): ")
            if user_display.upper() == "Y":
                print(sorted_data)

    elif user_input.upper() == "C":
        user_attribute_bestfit = input("Please enter the attribute you want to use to find the best fit for Health: ")
        user_order_polynomial = input("Please enter the order of the polynomial to be fitted: ")

    elif user_input.upper() == "H":
        user_attribute_plotting = input("Please enter the attribute you want to use for plotting: ")

    elif user_input.upper() == "E":
        Active = False
    else:
        print("Invalid command.")


