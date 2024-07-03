# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Harveen Kaur, Magdi Hajjaj, Khoi Ha, Sohaila Haroun"

# Update "" with your team (e.g. T102)
__team__ = "T002"

#==========================================#
# Place your sort_characters_agility_bubble function after this line


def sort_characters_agility_bubble(agility: list[dict], order: str) -> list[dict]:
    """Return agility in ascending order if order="A" or in descending order if order="D" using bubble sort. Return 'Agility key is not present' if Agility is not present.

    Precondition: order is either 'A' or 'D'

    Examples:
    >>>sort_characters_agility_bubble([{'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'H','Agility': 20}], "D")
    [{'Occupation': 'H', 'Agility': 20}, {'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}] 

    >>>sort_characters_agility_bubble([{'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]

    >>>sort_characters_agility_bubble([{'Occupation':'EB'},{'Occupation': 'M'}], "A")
    "Agility" key is not present. 
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    """
    if agility == []:
        return []
    if "Agility" not in agility[0].keys():
        print('Agility key is not present')
        return agility
    num = len(agility)
    if order != "A" and order != "D":
        return agility
    for i in range(num - 1):
        swapped = False
        if order == "A":
            for j in range(num - i - 1):
                first_index = agility[j]['Agility']
                second_index = agility[j + 1]['Agility']

                if first_index > second_index:
                    swapped = True
                    agility[j], agility[j + 1] = agility[j + 1], agility[j]
        if order == "D":
            for j in range(num - i - 1):
                first_index = agility[j]['Agility']
                second_index = agility[j + 1]['Agility']
                if agility[j]['Agility'] < agility[j + 1]['Agility']:
                    swapped = True
                    agility[j], agility[j + 1] = agility[j + 1], agility[j]
    return agility


#==========================================#
# Place your sort_characters_intelligence_selection function after this line


def sort_characters_intelligence_selection(list1: list[dict], order: str) -> list[dict]:
    """Return a sorted list based on ascending or descending order by the "Intelligence" attribute.

    Precondition: Order has to  the str A or B

    >>>sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 9}, {'Occupation': 'H','Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB','Intelligence': 9}]

    >>>sort_characters_intelligence_selection([{'Occupation':'EB'}, {'Occupation': 'M'}], "D")

    "Intelligence" key is not present
    [{'Occupation': 'EB'},{'Occupation': 'M'}]

    """

    for i in range(len(list1)):
        try:
            if order == "A":  # Ascending low to high
                min_idx = i
                for j in range(i + 1, len(list1)):
                    if list1[j]["Intelligence"] < list1[min_idx]["Intelligence"]:
                        min_idx = j
                list1[i], list1[min_idx] = list1[min_idx], list1[i]
            elif order == "D":  # Descending high to low
                max_idx = i
                for j in range(i + 1, len(list1)):
                    if list1[j]["Intelligence"] > list1[max_idx]["Intelligence"]:
                        max_idx = j
                list1[i], list1[max_idx] = list1[max_idx], list1[i]
        except:
            print("'Intelligence' key is not present")
            return list1

    return list1

#==========================================#
# Place your sort_characters_health_insertion function after this line


def sort_characters_health_insertion(pok_list: list[dict], string: str) -> list[dict]:
    """Return the new list sorting the characters health using insertion sorting
    method. If health is a key in the dictionary, the function return the sorted
    list. Else, return the original value.
    Precondition: the input string can only "A" or "D"
    Ex:
    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "D")
    [{'Occupation': 'EB', 'Health': 62.71}, {'Occupation': 'H', 'Health': 62.37}]

    >>>sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Health" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    >>>sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]
    """

    if not pok_list:
        return []

    for i in range(len(pok_list)):
        if 'Health' not in pok_list[i]:
            print('\"Health\" key is not present')
            return pok_list
    for j in range(1, len(pok_list)):
        key = pok_list[j]
        k = j - 1
        while (k >= 0 and pok_list[k]['Health'] > key['Health'] and string == 'A') or (k >= 0 and pok_list[k]['Health'] < key['Health'] and string == 'D'):
            pok_list[k + 1] = pok_list[k]
            k -= 1
        pok_list[k + 1] = key
    return pok_list

#==========================================#
# Place your sort_characters_armor_bubble function after this line


def sort_characters_armor_bubble(unsorted_characters: list[dict], order: str) -> list[dict]:
    """Return a sorted list of dictionaries by ascending or desending order based on the 'Armor' value using bubble sort.

    Precondition: order is either 'A' or 'D'

    Examples:
    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "D")
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB'}, {'Occupation': 'M'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "A")
    [{'Occupation': 'H', 'Armor': 10}, {'Occupation': 'EB', 'Armor': 11}]

    """
    characters = unsorted_characters
    if len(unsorted_characters) == 0:
        return unsorted_characters
    else:
        num_characters = len(characters)
        for i in range(num_characters - 1):
            swapped = False

            for j in range(num_characters - i - 1):
                if 'Armor' in characters[j]:
                    if order == 'A':
                        if characters[j]['Armor'] > characters[j + 1]['Armor']:
                            swapped = True
                            characters[j], characters[j
                                                      + 1] = characters[j + 1], characters[j]

                    elif order == 'D':
                        if characters[j]['Armor'] < characters[j + 1]['Armor']:
                            swapped = True
                            characters[j], characters[j
                                                      + 1] = characters[j + 1], characters[j]

                else:
                    print('"Armor\" key is not present')
                    return unsorted_characters

            if not swapped:
                return characters

#==========================================#
# Place your sort function after this line


def sort(characters: list[dict], order: str, attribute: str) -> list[dict]:
    """Return sorted list of dictionaries based on ascending or descending attribute.

     Precondition: order is either 'A' or 'D'

     Examples:
     >>>sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D", "Agility")
     [{'Occupation': 'EB', 'Agility': 13},{'Occupation': 'H', 'Agility': 11}]

     >>>sort([{'Occupation': 'EB', 'Agility': 13},{'Occupation': 'H', 'Agility': 11}], "A", "Stamina")
     Cannot be sorted by " Stamina "
     [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]

     >>>sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A", "Agility")
     [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]

    """
    if attribute == 'Armor':
        return sort_characters_armor_bubble(characters, order)
    elif attribute == 'Intelligence':
        return sort_characters_intelligence_selection(characters, order)
    elif attribute == 'Health':
        return sort_characters_health_insertion(characters, order)
    elif attribute == 'Agility':
        return sort_characters_agility_bubble(characters, order)
    else:
        print('Cannot be sorted by "', attribute, '"')
        return characters


# Do NOT include a main script in your submission

