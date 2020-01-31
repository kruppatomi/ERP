
""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
        table = data_manager.get_table_from_file("hr/persons.csv")
        title_list = ["id", "name", "year"]
        options = ["show_table", "Add", "Remove", "Update", "Special_1", "Special_2", "Back to Main menu: "]

        ui.print_menu("Hr menu: ", options, "Back to Main menu: ")
        try:
            inputs = ui.get_inputs([" Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)
                data_manager.write_table_to_file("hr/persons.csv", new_table)   
            elif option == "3":
                id_ = ui.get_inputs(["id_"], "")
                remove("hr/persons.csv",id_)
            elif option == "4":
                start_module()
            elif option == "5":
                result = get_oldest_person(table)
                ui.print_result(result, " Oldest person/people name/names: ")
            elif option == "6":
                result = get_persons_closest_to_average(table)
                ui.print_result(result, " who is the closest to te average age? : ")
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
    title_list = ["id","name","year"]

    ui.print_table(table, title_list)
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ["id","name","year"]
    inputs = ui.get_inputs(title_list, "enter new line: ")
    table.append(inputs)
    return table
    # your code

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
    table = data_manager.get_table_from_file("hr/persons.csv")
    dict_ = {}

    for line in table:
        dict_[line[0]] = [line[1],line[2]]
    
    id_ = id_[0]

    
    if id_ in dict_:
        del dict_[id_]
    
    key_lists = []
    value_lists = []

    for key,value in  dict_.items():
        key_lists.append(key)
        value_lists.append(value)
    for i in range(len(value_lists)):
        value_lists[i].insert(0, key_lists[i])

    data_manager.write_table_to_file("hr/persons.csv", value_lists)
    return value_lists


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
        dict_[lines[0]] = [lines[1],lines[2]]


    id_ = id_[0]

    title_list = ["Name: ","Year: "]
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
        

    data_manager.write_table_to_file("hr/persons.csv", value_lista)
    return value_lista
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    years = []
    names = []

    for i in table:
        years.append(i[2])
    
    for passnum in range(len(years)-1,0,-1):
        for i in range(passnum):
            if years[i]>years[i+1]:
                temp = years[i]
                years[i] = years[i+1]
                years[i+1] = temp

    for i in table: 
        if years[0] in i:
            names.append(i[1])

    return names
            

    
    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code

    years = []
    names = []

    for i in table:
        years.append(int(i[2]))

    for passnum in range(len(years)-1,0,-1):
        for i in range(passnum):
            if years[i]>years[i+1]:
                temp = years[i]
                years[i] = years[i+1]
                years[i+1] = temp

    counter = 0
    for i in years:
        counter += int(i)
    my_number = counter/len(years)
    result = min(years, key=lambda x: abs(x-my_number))

    for i in table: 
            if str(result) in i:
                names.append(i[1])

    return names