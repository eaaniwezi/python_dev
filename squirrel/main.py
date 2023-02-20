import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

pandas.DataFrame(data_dict).to_csv('squirrel_count.csv')