# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Magdi Hajjaj"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101299841"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-002"

#==========================================#
# Place your curve_fit function after this line
import numpy as np
import matplotlib.pyplot as plt


def curve_fit(pok_list: list[dict], attribute: str, degree: int):
    """Return the function in string of the curve given the pok_list with health 
    and the compared attribute inside, and the degree that the user want to use 
    for the function.

    Precondition: Each dictionary inside the list must have "Health". The 
    compared attribute must also be in the dictionary, and be a number. 
    The input of degree must be between 1 and 5 inclusively.

    Ex:
    >>>curve_fit([{"Health": 10, "Strength":2}, {"Health": 15, "Strength": 3}, {"Health": 13, "Strength": 2}], "Strength", 4)
    'y = 3.50x^1 + 4.50'
    >>>curve_fit([{"Health": 10, "Strength":2}, {"Health": 15, "Strength": 3}, {"Health": 13, "Strength": 2}, {"Health": 20, "Strength": 4}], "Strength", 4)
    'y = 0.75x^2 + -0.25x^1 + 9.00'
    >>>curve_fit([{"Health": 18, "Strength":5} ,{"Health": 10, "Strength":2}, {"Health": 15, "Strength": 3}, {"Health": 13, "Strength": 2}, {"Health": 20, "Strength": 4}], "Strength", 5)
    'y = -1.42x^3 + 13.50x^2 + -37.08x^1 + 43.00'
    """
    average_health = {}  # empty dictionary
    count_health = {}  # empty dictionary

    for entry in pok_list:  # for entry (which are dictionary) in the list
        attribute_value = entry[attribute]  # assign the value to attribute value (number)
        health_value = entry["Health"]  # assign the value to health value (number)

        if attribute_value not in average_health:  # if the attribute value is not in the dictionary, add it. Else, skip
            average_health[attribute_value] = 0  # add the attribute value into the new dictionary as key and assign the value of it to 0
            count_health[attribute_value] = 0  # add the attribute value into the new dictionary as key and assign the value of it to 0

        average_health[attribute_value] += health_value  # add the health_value to the value of attribute_value key
        count_health[attribute_value] += 1  # add count with one
    for key in average_health:
        average_health[key] /= count_health[key]  # find the average_health now
    x_values = np.array(list(average_health.keys()))  # put it to array type
    y_values = np.array(list(average_health.values()))  # put it to array type

    if degree >= len(x_values):  # fitting the polynomial regression
        degree = len(x_values) - 1
    coefficients = np.polyfit(x_values, y_values, degree)  # using polyfit
    equation_str = "y = "  # construct string
    for i in range(degree + 1):
        coef = coefficients[i]
        power = degree - i
        if i < degree:
            equation_str += f"{coef:.2f}x^{power} + "
        else:
            equation_str += f"{coef:.2f}"

    return equation_str

# Do NOT include a main script in your submission



