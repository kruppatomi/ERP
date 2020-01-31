
""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

import main

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    while True:
        table = data_manager.get_table_from_file("inventory/inventory.csv")
        title_list = ["id","name","manufacturer","purchase year","durability"]

        options = ["Show table","Add","Remove","Update","Special_1","Special_2", "Back to Main menu: "]

        ui.print_menu("\nInventory menu:", options, "Back to Main menu: ")
        try:
            inputs = ui.get_inputs(["\nWhich function would you like? "],"")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)                                              #
                data_manager.write_table_to_file("inventory/inventory.csv", new_table)
            elif option == "3":
                id_ = ui.get_inputs(["Id: "], "")
                remove("inventory/inventory.csv", id_)
            elif option == "4":
                id_ = ui.get_inputs(["Id: "], "")
                update("inventory/inventory.csv", id_)
            elif option == "5":
                result = get_available_items(table)
                ui.print_result(result, " Available items: ")
            elif option == "6":
                result = get_average_durability_by_manufacturers(table)
                ui.print_result(result, " Avg durability: ")
            elif option == "7":
                main.main()

            else:
                raise KeyError("There is no such option.")
        
        except KeyError as err:
            ui.print_error_message(str(err))



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ["id","name","manufacturer","purchase year","durability"]

    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    random_id = common.generate_random(table)
    print("\nYour random id is: ",random_id)
    title_list = ["Name: ","Manufacturer: ","Purchase Year: ","Durability: "]
    inputs = ui.get_inputs(title_list, "")

    inputs.insert(0, random_id)
    table.append(inputs)
    
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    dict_ = {}
    for lines in table:
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4]]

    id_ = id_[0]

    if id_ in dict_:
        del dict_[id_]

    key_lista = []
    value_lista = []
    for key, value in dict_.items():
        key_lista.append(key)
        value_lista.append(value)

    for i in range(len(value_lista)):
        value_lista[i].insert(0, key_lista[i])
    

    data_manager.write_table_to_file("inventory/inventory.csv", value_lista)
    return value_lista


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    dict_ = {}
    for lines in table:
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4]]


    id_ = id_[0]

    title_list = ["Name: ","Manufacturer: ","Purchase Year: ","Durability: "]
    inputs = ui.get_inputs(title_list, "")
    
    key_lista = []
    value_lista = []
    for key, value in dict_.items():
        key_lista.append(key)
        value_lista.append(value)

    index = key_lista.index(id_)
    value_lista[index] = inputs


    
    for i in range(len(value_lista)):
        value_lista[i].insert(0, key_lista[i])
        

    data_manager.write_table_to_file("inventory/inventory.csv", value_lista)
    return value_lista


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    durability_list = []
    file = data_manager.get_table_from_file("inventory/inventory.csv")
    for line in file:
        if int(line[3]) + int(line[4]) == 2017:
            durability_list.append(line)
            line[3] = int(line[3])
            line[4] = int(line[4])
    return durability_list

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    manuf_dict = {}
    file = data_manager.get_table_from_file("inventory/inventory.csv")
    for line in file:
        manuf_dict[line[2]] = []
    for line in file:
        manuf_dict[line[2]].append(line[4])
    for key, value in manuf_dict.items():
        sum_value = 0
        for i in value:
            sum_value += int(i)
        manuf_dict[key] = sum_value / len(value)
    return manuf_dict