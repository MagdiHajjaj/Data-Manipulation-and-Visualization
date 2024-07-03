# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Magdi Hajjaj, Harveen Kaur, Khoi Ha, Sohaila Haroun"

# Update "" with your team (e.g. T102)
__team__ = "T002"


#==========================================#
# Place your character_occupation_list function after this line

def character_occupation_list(file_name: str, occupation_name: str) -> list[dict]:
    """Return a list of characters (stored as a dictionary) whose occupation
    is provided as the input parameter.

    Preconditions: 
        1. Text file must contain data in CSV format.
        2. file_name, and occupation_name must be strings
        3. The file_name must exist in the same directory as the code file


    >>> character_occupation_list('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
    {another element},
    …
    ]

    >>> character_occupation_list('characters-mat.csv', 'XXXXX')
    []
    """
    header_found = False
    header = None
    data = []
    in_file = open(file_name, "r")
    for line in in_file:
        line = line.strip('\n').split(",")
        if not header_found:
            header = line
            header_found = True
        elif line[0] == occupation_name:
            datadic = {}
            for i in range(1, 9):
                if i == 6:
                    datadic[header[i]] = float(line[i])
                elif i == 8:
                    datadic[header[i]] = (line[i])
                else:
                    datadic[header[i]] = int(line[i])

            data.append(datadic)

    in_file.close()

    return data

#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, strength_range: tuple[int, int]) -> list[dict]:
    """Return a list of characters whose strength falls between the input range 
    determined by tuple with maximum and minimum value, and strength is not included in that list.

    Precondition:
        1. Text file must contain data in CSV format.
        2. file_name must be a string and occupation_name is a tuple.
        3. The file_name must exist in the same directory as the code file

    Ex:

    >>>character_strength_list("characters-mat.csv", (8,10))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15,
    'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, ...]
    """
    in_file = open(file_name, 'r')
    character = []
    first_line = True
    for line in in_file:
        line = line.strip().split(",")
        if first_line:
            first_line = False
            table_header = line
        else:
            if int(line[1]) >= strength_range[0] and int(line[1]) <= strength_range[1]:
                strength_list = {}
                strength_list[table_header[0]] = line[0]
                strength_list[table_header[2]] = int(line[2])
                strength_list[table_header[3]] = int(line[3])
                strength_list[table_header[4]] = int(line[4])
                strength_list[table_header[5]] = int(line[5])
                strength_list[table_header[6]] = float(line[6])
                strength_list[table_header[7]] = int(line[7])
                strength_list[table_header[8]] = line[8]
                character += [strength_list]
    in_file.close()
    return character

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck: float) -> list[dict]:
    """Return a list of charcters, stored as a dictionary, whose luck is less 
    than the value provided in the input paramater.

    Pre-conditions: 
        1. Text file must contain data in CSV format.
        2. file_name must be a string.
        3. The file_name must exist in the same directory as the code file

    Examples:
    >>> character_luck_list('characters-mat.csv', 0.2)
    [{'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14,
    'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]

    >>> character_luck_list('characters-mat.csv', 0.1)
    []

    >>> character_luck_list ('characters-mat.csv', 0.19)
    [{'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14,
    'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    """
    luck_list = []
    table_header = ""
    file = open(file_name, "r")
    first_line = True
    for line in file:
        line = line.strip('\n').split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            character = {}
            for i in range(9):
                if i == 6:
                    if float(line[6]) < luck:
                        luck_list += [character]
                elif i == 0 or i == 8:
                    character[table_header[i]] = line[i]
                else:
                    character[table_header[i]] = int(line[i])

    file.close()
    return luck_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file: str, weapon_name: str) -> list[dict]:
    """Return the list of characters (stored as dictionaries) with the weapon 
    from the file. Returns an empty list if weapon is not in the file.

    Preconditions: 
        1. Text file must contain data in CSV format.
        2. file_name must be a string.
        3. The file_name must exist in the same directory as the code file


    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]
    >>> character_weapon_list ('characters-mat.csv', 'aaa')
    []
    """
    file = open(file, "r")
    first_line = True
    weapon_list = []
    for line in file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if line[8] == weapon_name:
                weapon = {}
                weapon[table_header[0]] = line[0]
                weapon[table_header[1]] = int(line[1])
                weapon[table_header[2]] = int(line[2])
                weapon[table_header[3]] = int(line[3])
                weapon[table_header[4]] = int(line[4])
                weapon[table_header[5]] = int(line[5])
                weapon[table_header[6]] = float(line[6])
                weapon[table_header[7]] = int(line[7])
                weapon_list.append(weapon)
    file.close()
    return weapon_list
#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, tuple_value: tuple[str, (str, int, float)]) -> list[dict]:
    """Return as a list of characters (stored as a dictionary) where the keys of
    the dictionary are the labels for all attributes in the spreadsheet except for the attribute
    in the first item of the tuple. If the first item of the tuple is invalid, the function will
    print the error message “Invalid Value” and return an empty list.                                 

    Precondition:
        1. file_name has to have the following columns:
        Occupation,Strength,Agility,Stamina,Personality,Intelligence,Luck,Armor,Weapon
        2. Text file must contain data in CSV format.
        3. The file_name must exist in the same directory as the code file


    >>> load_data('characters-mat.csv', ('Weapon', 'Staff'))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]

    >>> load_data('characters-mat.csv', ('All', -1))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8,
    'Weapon': 'Staff'},
    {another element},
    …
    ]

    >>> load_data('characters-mat.csv', ('Agility', 2))
    Invalid Value 
    [] 
    >>> load_data('characters-mat.csv', ('Stamina', -1))
    Invalid Value 
    [] 
    """
    if tuple_value[0] == 'All':
        header_found = False
        header = ""
        data = []
        in_file = open(file_name, "r")
        for line in in_file:
            line = line.strip('\n').split(",")
            if not header_found:
                header = line
                header_found = True
            else:
                datadic = {}
                for i in range(0, 9):
                    if i == 6:
                        datadic[header[i]] = float(line[i])
                    elif i == 8 or i == 0:
                        datadic[header[i]] = (line[i])
                    else:
                        datadic[header[i]] = int(line[i])
                data.append(datadic)

        in_file.close()

        return data
    elif tuple_value[0] == 'Occupation':
        return character_occupation_list(file_name, tuple_value[1])
    elif tuple_value[0] == 'Strength':
        return character_strength_list(file_name, tuple_value[1])
    elif tuple_value[0] == 'Luck':
        return character_luck_list(file_name, tuple_value[1])
    elif tuple_value[0] == 'Weapon':
        return character_weapon_list(file_name, tuple_value[1])
    else:
        print("Invalid Value")
        return []


#==========================================#
# Place your calculate_health function after this line
def calculate_health(characters: list[dict]) -> list[dict]:
    """Return the calculated helath of the character and store it as an additional attribute in the dictionary.

    Precondition:
        1. Each dictionary in the input list contains all required keys: 'Strength', 'Agility',
           'Stamina', 'Personality', 'Intelligence','Armor',and 'Luck'.
        2. Values associated with each key are numeric (integers or floats).


    >>> calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.7,
    'Armor': 8, 'Weapon': 'Staff'}])

    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff',
    'Health': 80.8}]
    """
    health_list = characters
    for i in range(len(characters)):
        health = characters[i]['Strength'] + characters[i]['Agility'] + characters[i]['Stamina'] + \
            characters[i]['Personality'] + characters[i]['Intelligence'] + \
            (characters[i]['Armor']**2 * characters[i]['Luck'])
        health_list[i]["Health"] = health
    return health_list

# Do NOT include a main script in your submission

