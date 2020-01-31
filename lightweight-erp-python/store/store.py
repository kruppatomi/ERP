#nincs benne az utolsó special!
""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
        table = data_manager.get_table_from_file("store/games.csv")
        title_list = ["id","title","manufacturer","price","in stock"]

        options = ["Show table","Add","Remove","Update","Special_1", "Back to Main menu: "]

        ui.print_menu("\nStore menu:", options, "Back to Main menu: ")
        try:
            inputs = ui.get_inputs(["\nWhich function would you like? "],"")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)                                              #
                data_manager.write_table_to_file("store/games.csv", new_table)
            elif option == "3":
                id_ = ui.get_inputs(["Id: "], "")
                remove("store/games.csv", id_)
            elif option == "4":
                id_ = ui.get_inputs(["Id: "], "")
                update("store/games.csv", id_)
            elif option == "5":
                result = get_counts_by_manufacturers(table)
                ui.print_result(result, "Counts by manufacturers: ")
            elif option == "6":
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
    title_list = ["id","title","manufacturer","price","in stock"] 

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
    title_list = ["Title: ","Manufacturer: ","Price: ","In stock: "]
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
    

    data_manager.write_table_to_file("store/games.csv", value_lista)
    return value_lista


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    dict_ = {}
    for lines in table:
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4]]


    id_ = id_[0]

    title_list = ["Title: ","Manufacturer: ","Price: ","In stock: "]
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
        

    data_manager.write_table_to_file("store/games.csv", value_lista)
    return value_lista

# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    lines2_list = []
    for lines in table:
        lines2_list.append(lines[2])
    
    dict_ = {}
    for i in lines2_list:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] = dict_[i] + 1
    return dict_

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code