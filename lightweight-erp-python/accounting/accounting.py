# benne van minden
""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
    while True:
        table = data_manager.get_table_from_file("accounting/items.csv")

        title_list = ["id","month","day","year","type","amount"]
        
        # id_ = table[0]

        options = ["show table", "add", "remove", "update", "which year max", "avg amount", "go back to menu\n"]

        ui.print_menu("Features:", options, "Exit program")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)
                data_manager.write_table_to_file("accounting/items.csv", new_table)
            elif option == "3":
                title_list = ["id"]
                id_ = ui.get_inputs(title_list, "Remove line")
                remove(table, id_)
            elif option == "4":
                update()
            elif option == "5":
                print(which_year_max(table))
            elif option == "6":
                title_list = ["year: "]
                year = ui.get_inputs(title_list, "Average (per item) profit: ")
                print(avg_amount(table, year))
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

    title_list = ["id","month","day","year","type","amount"]
    
    ui.print_table(table, title_list)



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:EAD
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """


    random_id = common.generate_random(table)
    title_list = ["month","day","year","type","amount"]
    inputs = ui.get_inputs(title_list, "Enter new line")
    inputs.insert(0, random_id)
    table.append(inputs)

    return table



    """#table[-1] = ['12345123', '12', '2', '31', 'in' ,'34']
    add_mar_hozza = ['12345123', '12', '2', '31', 'in' ,'34']
    #12345678 12 2 2019 in 12
    table.append(add_mar_hozza)
    print(table)"""

    """table = data_manager.get_table_from_file("items.csv")


    new_inputs = input("\nAdd id; month, day, year, type (in/out) and amount of transaction:\n")
    key_lista = new_inputs.split()
    input_lista = []
    for i in input_list:
        input_lista.append(i)

    table.append(input_lista)

    print(ui.print_table(table, input_list))"""


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """


    table = data_manager.get_table_from_file("accounting/items.csv")
    
    # title_list = ["id"]
    # id_ = ui.get_inputs(title_list, "Remove line")

    for lines in table:              # line vegig megy a listakon
        if str(lines[0]) == id_[0]:       # a sorok 0. elemei kellenek nekunk, igy hivatkozunk, es az id_[0].elemei(inputba megadod) lesznek a sorok 0.elemei
            table.remove(lines)

    table_remove = data_manager.write_table_to_file("accounting/items.csv", table)
    
    return table_remove


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
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4],lines[5]]


    id_ = id_[0]

    title_list = ["Month: ","Day: ","Year: ","Type: ","Amount: "]
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
        

    data_manager.write_table_to_file("accounting/items.csv", value_lista)
    return value_lista

#update("items.csv", id_)

# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    my_dict = {}


    table = data_manager.get_table_from_file("accounting/items.csv")

    for lines in table:
        if lines[3] in my_dict:
            if lines[4] == "in":    
                my_dict[lines[3]] += int(lines[5])
            elif lines[4] == "out":
                my_dict[lines[3]] -= int(lines[5])        
        elif lines[3] not in my_dict:
            if lines[4] == "in":
                my_dict[lines[3]] = int(lines[5])
            elif lines[4] == "out":

                my_dict[lines[3]] = 0-int(lines[5])     # in nel hozzaadja outnal kivonja
    
    year_max = max(my_dict.values())                   # legnagyobb yeart megkeresi 

    for key, value in my_dict.items():                 # megkeresi a legnagyobb ev key parjat es visszaadja
            if my_dict[key] == year_max:
                    return key