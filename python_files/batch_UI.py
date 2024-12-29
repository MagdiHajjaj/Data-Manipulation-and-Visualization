#==========================================#
__author__ = "Sohaila Haroun"
__team__ = "T-002"
#==========================================#

from sort import sort
from load_data import load_data
from load_data import calculate_health
from histogram import histogram
from curve_fit import curve_fit


file_name = input(
    "Please enter the name of the file where your commands are stored:")
print("Data loaded")
infile = open(file_name, 'r')
data = []
for line in infile:
    command = line.strip().split(';')
    try:
        if command[0].lower() == "l":
            if command[2].lower() == "strength":
                command[3] = command[3].strip('( )').replace(" ", "")
                try:
                    values = (
                        command[2], (int(command[3][0]), int(command[3][2])))
                    data = load_data(command[1], values)
                except:
                    print("Invalid command.")
            elif command[2].lower() == "luck":
                try:
                    values = (command[2], float(command[3]))
                    data = load_data(command[1], values)
                except:
                    print("Invalid command.")
            elif command[2].lower() == "occupation" or command[2].lower() == "weapon" or command[2].lower() == "all":
                values = (command[2], command[3])
                data = load_data(command[1], values)
            else:
                print("Invalid command.")
            try:
                if len(data) > 0:
                    data = calculate_health(data)
                    print("Data loaded")
            except:
                print(
                    "Health cannot be calculated, note this means Curve Fit cannot be used")
                print("Data loaded")
        elif command[0].lower() == "s" and len(data) > 0:
            try:
                data = sort(data, command[2], command[1])
                if command[3].strip('\n').lower() == "y":
                    print(data)
                    print("Data sorted")
            except:
                print("Invalid command.")
        elif command[0].lower() == "h" and len(data) > 0:
            try:
                histogram(data, command[1])
            except:
                print("Invalid command.")
        elif command[0].lower() == "c" and len(data) > 0:
            try:
                print(curve_fit(data, command[1], command[2]))
            except:
                print("Invalid command.")
        elif (command[0].strip('\n')).lower() == 'e':
            infile.close()
            print('File closed.')
            break
        else:
            print("Invalid command.")
    except:
        print("Invalid command.")
