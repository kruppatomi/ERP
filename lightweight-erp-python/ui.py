""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
   
    table.insert(0, title_list)
          # title listet 0.helyre teszi
    # your code

    lenght_list = []                                # tartalmazza az összes szót
    for lines in table:
        for items in lines:
            lenght_list.append(items)

    longest_words_length = len(max(lenght_list, key=len))
    multiplier = len(title_list)*(longest_words_length+1)

    for sublist in table:
        print("|\n|", "-"*multiplier, "|")

        for j in sublist:
            print("|", j, end = " "*(longest_words_length-len(j)))

    print("|\n|","-"*multiplier, "|")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("\n", label)
    print("\n", result)
    # your code



def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print("\n", title)

    print_list = []
    for i in list_options:
        print_list.append(i)
    
    number_list = []
    for i in range(len(print_list)):
        number_list.append(i+1)
    
    to_print = dict(zip(number_list, print_list))

    for k,v in to_print.items():
        print("\t", k,v)
    
    # print("\t","0", exit_message)
    # print(title)
    # print('\n'.join([str(i) for i in enumerate(list_options, 1)]))
    # print("(0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    # your code
    print(title)

    inputs = []
    for i in list_labels:
        inputs.append(input(i))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    # your code
    print(message)
