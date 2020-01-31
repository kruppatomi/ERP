
""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
        table = data_manager.get_table_from_file("crm/customers.csv")
        title_list = ["id", "name", "email", "suscribed"]

        options = ["Show table", "Add", "Remove", "Update", "Special_1", "Special_2", "Back to Main menu: "]

        ui.print_menu("\nCustomer Relationship Management menu:", options, "Back to Main menu: ")
        try:
            inputs = ui.get_inputs(["\nWhich function would you like? "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)                                              #
                data_manager.write_table_to_file("crm/customers.csv", new_table)
            elif option == "3":
                id_ = ui.get_inputs(["Id: "], "")
                remove("crm/customers.csv", id_)
            elif option == "4":
                id_ = ui.get_inputs(["Id: "], "")
                update("crm/customers.csv", id_)
            elif option == "5":
                result = get_longest_name_id(table)
                ui.print_result(result, " Longest name id: ")
            elif option == "6":
                result = get_subscribed_emails(table)
                ui.print_result(result, "Subscribed e-mails: ")
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
       
    title_list = ["id","name","email","suscribed"]
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
    print("\nYour random id is: ", random_id)
    title_list = ["Name: ", "Email: ", "Suscribed: "]
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
        dict_[lines[0]] = [lines[1],lines[2],lines[3]]

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
    

    data_manager.write_table_to_file("crm/customers.csv", value_lista)
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
        dict_[lines[0]] = [lines[1],lines[2],lines[3]]


    id_ = id_[0]

    title_list = ["Name: ","Email: ","Suscribed: "]
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
        

    data_manager.write_table_to_file("crm/customers.csv", value_lista)
    return value_lista


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    char = []
    
    counter = 0
    file = data_manager.get_table_from_file("crm/customers.csv")
    for line in file:
        if len(line[1]) > counter:
            counter = 0
            counter += len(line[1])
    for check in file:
        if len(check[1]) == counter:
            char.append(check[1])
    
    for i in range(len(char)):
        for j in range(len(char) - 1):
            if char[j] > char[j + 1]:
                char[j], char[j + 1] = char[j + 1], char[j]
    for ID_of_name in file:
        if char[-1] in ID_of_name:
            ui.print_result(ID_of_name[0], "ID: ") 
            return ID_of_name[0]

def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
    subscribers = []
    file = data_manager.get_table_from_file("crm/customers.csv")
    for line in file:
        if line[3] == "1":
            subscribers.append(line[2] +";"+ line[1])
    return subscribers


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
