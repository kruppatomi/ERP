#kész
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
                my_dict[lines[3]] = 0-int(lines[5])    # in nel hozzaadja outnal kivonja
        
    year_maxprofit = max(my_dict.values())            # megmondja melyik evben volt legtobb profit

    return year_maxprofit


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    table = data_manager.get_table_from_file("accounting/items.csv")
    # title_list = ["year"]
    # year = ui.get_inputs(title_list, "Average (per item) profit: ")
    
    my_dict1 = {}                # contains: years : sum of profits 
    my_dict2 = {}                # contains: years : count of items 
    avg_dict = {}                # contains: years : average of profits(per count of items)

    sum_profit = []             # list of profits
    count_item = []             # list of items per year
    avg_profit = []             # division of profit/count of items

    years_list = []             # contains the years

    for lines in table:                                 # returns a dictionary with years and sum of profits in a year
        if lines[3] in my_dict1:
            if lines[4] == "in":    
                my_dict1[lines[3]] += int(lines[5])
            elif lines[4] == "out":
                my_dict1[lines[3]] -= int(lines[5])        
        elif lines[3] not in my_dict1:
            if lines[4] == "in":
                my_dict1[lines[3]] = int(lines[5])
            elif lines[4] == "out":
                my_dict1[lines[3]] = 0-int(lines[5])
    
    for lines in table:                                  # returns dict with year and counf of items
            if lines[3] in my_dict2:
                    my_dict2[lines[3]] += 1
            elif lines[3] not in my_dict2:
                    my_dict2[lines[3]] = 1

    for k, v in my_dict1.items():                          # at basszuk listaba hogy el tudjuk osztani
        sum_profit.append(v)

    for k, v in my_dict2.items():
        count_item.append(v)

    for i in range(len(sum_profit)):
        avg_profit.append(sum_profit[i] / count_item[i])

    for lines in table:
        if lines[3] not in years_list:
            years_list.append(lines[3])

    avg_dict = dict(zip(years_list, avg_profit))            # contains avg profit per years

    if year[0] in avg_dict.keys():
        return round(avg_dict[year[0]])
