
""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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
        table = data_manager.get_table_from_file("sales/sales.csv")
        title_list = ["id","title","price","month","day","year"]

        options = ["Show table","Add","Remove","Update","Special_1","Special_2", "Back to Main menu: "]

        ui.print_menu("\nSales menu:", options, "Back to Main menu: ")
        try:
            inputs = ui.get_inputs(["\nWhich function would you like? "],"")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                new_table = add(table)                                              #
                data_manager.write_table_to_file("sales/sales.csv", new_table)
            elif option == "3":
                id_ = ui.get_inputs(["Id: "], "")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(["Id: "], "")
                update(table, id_)
            elif option == "5":
                result = get_lowest_price_item_id(table)
                ui.print_result(result, " Cheapest game is id: ")
            elif option == "6":
                result = get_items_sold_between(table)
                ui.print_result(result, " Game titles between the dates: ")
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
    

    data_manager.write_table_to_file("sales/sales.csv", value_lista)
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
        
    data_manager.write_table_to_file("sales/sales.csv", value_lista)
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
    prices = []
    names = []

    for i in table:
        prices.append(i[2])
    
    for passnum in range(len(prices)-1,0,-1):
        for i in range(passnum):
            if prices[i]>prices[i+1]:
                temp = prices[i]
                prices[i] = prices[i+1]
                prices[i+1] = temp

    for i in table: 
        if prices[0] in i[2]:
            names.append(i[0])

    return names
            


def get_items_sold_between(table):
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
    result = []
    title_list = ["Month: ","Day: ","Year: "]
    smaller = ui.get_inputs(title_list, "From date: ")
    smaller.insert(0, 0)
    smaller.insert(0, 0)
    smaller.insert(0, 0)
    biger = ui.get_inputs(title_list, "To date: ")
    biger.insert(0, 0)
    biger.insert(0, 0)
    biger.insert(0, 0)
    table.append(smaller)
    table.append(biger)

    for passnum in range(len(table)-1, 0, -1):
        for i in range(passnum):
            if int(table[i][5]) > int(table[i+1][5]):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
            elif int(table[i][5]) == int(table[i+1][5]) and int(table[i][3]) > int(table[i+1][3]):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
            elif int(table[i][5]) == int(table[i+1][5]) and int(table[i][3]) == int(table[i+1][3]) and int(table[i][4]) > int(table[i+1][4]):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp

    index_s = table.index(smaller)
    index_b = table.index(biger)
    for i in table[index_s+1:index_b]:
        result.append(i[1])
    return result


# functions supports data abalyser
# --------------------------------

#enyem
def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
#eddig az enyem

def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
