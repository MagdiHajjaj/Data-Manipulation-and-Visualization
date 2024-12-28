#==========================================#
__author__ = "Magdi Hajjaj"
__student_number__ = "101299841"
__team__ = "T-002"
#==========================================#

import matplotlib.pyplot as plt
import math
 
 
def histogram(list: list, attribute: str) -> float:
    """Takes two input parameters, a list of dictionaries and a string that indicates which attribute will be plotted on the histogram. Returns -1 if the attribute is categorical or the maximum value if the attribute is numerical.
    Preconditions: The provided string is a key in all dictionaries in the list
    >>>histogram([{'Occupation': 'AT', 'Strength': 20, 'Intelligence': 8, 'Luck': 0.67},{'Occupation': 'AT', 'Strength': 13, 'Intelligence': 7, 'Luck': 0.67},{'Occupation': 'DB', 'Strength': 19, 'Intelligence': 12, 'Luck': 0.44}], 'Luck')
    [Figure displayed]
    0.67
    >>>histogram([{'Occupation': 'AT', 'Strength': 20, 'Intelligence': 8},{'Occupation': 'AT', 'Strength': 13, 'Intelligence': 7},{'Occupation': 'DB', 'Strength': 19, 'Intelligence': 12}], 'Occupation')
    [Figure displayed]
    -1
    >>>histogram([{'Occupation': 'AT', 'Strength': 20, 'Intelligence': 8, 'Luck': 0.67},{'Occupation': 'AT', 'Strength': 13, 'Intelligence': 7, 'Luck': 0.67},{'Occupation': 'DB', 'Strength': 19, 'Intelligence': 12, 'Luck': 0.44}], 'Strength')
    [Figure displayed]
    20
    >>>histogram([{'Occupation': 'AT', 'Strength': 20, 'Intelligence': 8, 'Luck': 0.67},{'Occupation': 'AT', 'Strength': 13, 'Intelligence': 7, 'Luck': 0.67},{'Occupation': 'DB', 'Strength': 19, 'Intelligence': 12, 'Luck': 0.44}], 'Intelligence')
    12
    """
    if isinstance(list[0][attribute], str):
        attribute_count = {}
        for d in list:
            value = d[attribute]
            attribute_count[value] = attribute_count.get(value, 0) + 1
        fig1 = plt.figure()
        plt.bar(attribute_count.keys(), attribute_count.values(), edgecolor="Black")
        plt.title('Histogram of ' + attribute)
        plt.xlabel(attribute + ' value')
        plt.ylabel('Occurrences')
        plt.show()
        return -1
    else:
        bars_x = []
        bars_y = {}
        bar_heights = []
        max_value = 0
        for d in list:
            value = d[attribute]
            if value > max_value:
                max_value = value
            if bars_y.get(value):
                bars_y[value] += 1
            else:
                bars_x.append(value)
                bars_y[value] = 1
        for x in bars_x:
            value = bars_y.get(x)
            bar_heights.append(value)
        plt.figure()
        plt.title('Histogram of ' + attribute)
        plt.xlabel(attribute + ' value')
        plt.ylabel('Occurrences')
        plt.bar(bars_x, bar_heights, width=(max_value / 20), edgecolor="Black")
        x_ticks = []
        for i in range(21):
            x_ticks.append(i * (max_value / 20))
        plt.xticks(x_ticks, rotation=45)
 
        return max_value

# Do NOT include a main script in your submission

