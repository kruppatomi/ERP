""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


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
        table = data_manager.get_table_from_file("sales.csv")
        title_list = ["id","title","price","month","day","year"]

        options = ["Show table","Add","Remove","Update"]

        ui.print_menu("\nSales menu:", options, "Exit program")
        try:
            inputs = ui.get_inputs(["\nWhich function would you like? "],"")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)                                              #
                data_manager.write_table_to_file("sales.csv", new_table)
            elif option == "3":
                id_ = ui.get_inputs(["Id: "], "")
                remove("sales.csv", id_)
            elif option == "4":
                id_ = ui.get_inputs(["Id: "], "")
                update("sales.csv", id_)

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
    
    title_list = ["id","title","price","month","day","year"]

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
    title_list = ["Title: ","Price: ","Month: ","Day: ","Year: "]
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

    table = data_manager.get_table_from_file("sales.csv")

    dict_ = {}
    for lines in table:
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4],lines[5]]

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
    

    data_manager.write_table_to_file("sales.csv", value_lista)
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

    
    table = data_manager.get_table_from_file("sales.csv")

    dict_ = {}
    for lines in table:
        dict_[lines[0]] = [lines[1],lines[2],lines[3],lines[4],lines[5]]


    id_ = id_[0]

    title_list = ["Title: ","Price: ","Month: ","Day: ","Year: "]
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
        

    data_manager.write_table_to_file("sales.csv", value_lista)
    return value_lista


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
