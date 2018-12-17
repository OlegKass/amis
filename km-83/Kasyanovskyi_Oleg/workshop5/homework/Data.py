import plotly
import plotly.graph_objs as go

with open("data/orders.csv") as file:

    header = file.readline()
    header_list = header.strip(" ").rstrip().split(",")

    dataset = dict()

    print(header_list)

    line = file.readline()
    LIST = []
    while line:

        line_list = line.rstrip().strip().split(",")

        row_dict = dict(zip(header_list,line_list))
        LIST.append( line_list )



        if row_dict["client"] in dataset.keys():


            if row_dict["date"] in dataset[row_dict["client"]].keys():


                if row_dict["product"] in dataset[row_dict["client"]][row_dict["date"]].keys():


                    if row_dict["quantity"] in dataset[row_dict["client"]][row_dict["date"]][row_dict["product"]]["quantity"] :
                        quantity_list = [ dataset["client"]["date"]["product"]["quantity"] ]
                        quantity_list.append(row_dict["quantity"])

                    else:
                        dataset[row_dict["client"]][row_dict["date"]][row_dict["product"]]["quantity"] = row_dict["quantity"]


                    if row_dict["price"] in dataset["client"]["date"]["product"]["price"]:
                        price_list = [dataset["client"]["date"]["product"]["price"]]
                        price_list.append(row_dict["price"])
                    else:
                        dataset[row_dict["client"]][row_dict["date"]][row_dict["product"]]["price"] = row_dict["price"]


                else:
                    dataset[row_dict["client"]][row_dict["date"]][row_dict["product"]] = {
                        "quantity":

                                row_dict["quantity"]

                        ,
                        "price":

                                row_dict["price"]

                    }

            else:
                dataset[row_dict["client"]][row_dict["date"]] = {
                    row_dict["product"]:
                        {
                            "quantity":

                                    row_dict["quantity"]

                            ,
                            "price":

                                    row_dict["price"]

                        }
                }



        else:
            dataset[row_dict["client"]] = {
                row_dict["date"]:
                    {
                        row_dict["product"]:
                            {
                                "quantity":

                                        row_dict["quantity"]

                                ,
                                "price":

                                        row_dict["price"]

                            }
                    }

            }








        line = file.readline()




print(dataset)
Product_list = []

for client in dataset.keys():
    Product_list_client = []
    for date in dataset[client].keys():

        for product in dataset[client][date].keys():

            Product_list_client.append(product)

    Product_list.append(Product_list_client)

print(Product_list)
SET = {}
list_of_sets = []
for list_product in Product_list:
    Set_of_products = set(list_product)
    list_of_sets.append(Set_of_products)

for i in range(len(list_of_sets)):
    SET = list_of_sets[i-1] & list_of_sets[i]

print(SET)
data_scatter = dict()
q = 0
for client in dataset.keys():

    for date in dataset[client].keys():

        for product in dataset[client][date].keys():


            if product == "apple":

                data_scatter[date] = dataset[client][date][product]["price"]


print(data_scatter)

data = go.Scatter(
     x=list(data_scatter.keys()),
     y=list(data_scatter.values())
)
plotly.offline.plot([data], filename='prices_of_apple.html')

data_scatter = dict()

for client in dataset.keys():
    money = 0
    for date in dataset[client].keys():

        for product in dataset[client][date].keys():

            money += (float(dataset[client][date][product]["quantity"]) * float(dataset[client][date][product]["price"]))

    data_scatter[client] = money

data = go.Scatter(
     x=list(data_scatter.keys()),
     y=list(data_scatter.values())
)
plotly.offline.plot([data], filename='amount_of_money_spent.html')

Buy_list = []
Buy_dict = {}
for client in dataset.keys():

    for date in dataset[client].keys():

        for product in dataset[client][date].keys():
            Buy_list.append(product)

            if product in Buy_dict.keys():
                list_of_products = Buy_dict[product]
                list_of_products.append(product)
            else:
                Buy_dict[product] = [product]
print(11111)
print(Buy_list)

print(Buy_dict)
Buy_dict_count = dict()
for i,j in Buy_dict.items():
    if len(j) in Buy_dict_count.keys():

        Buy_dict_count[len(j)].append(i)

    else:
        Buy_dict_count[len(j)] = [i]


print(Buy_dict_count)

Max = Buy_dict_count[max(list(Buy_dict_count.keys()))]
print("Max -",Max)
Min = Buy_dict_count[min(list(Buy_dict_count.keys()))]
print("Min -",Min)

Price_dict = dict()

for client in dataset.keys():

    for date in dataset[client].keys():

        for product in dataset[client][date].keys():

            Price = float(dataset[client][date][product]["price"])

            if product in Price_dict.keys():

                Price_dict[str(Price)].append(product)

            else:

                Price_dict[str(Price)] = [product]


print(Price_dict)

The_expensive = max(list(Price_dict.keys()))

print("The_expensive - ",Price_dict[The_expensive][0])

Counter_of_clients = dict()

for client in dataset.keys():

    for date in dataset[client].keys():

        for product in dataset[client][date].keys():

            if product in Counter_of_clients.keys():

                Counter_of_clients[product].add(client)

            else:
                Counter_of_clients[product] = {client}

print(Counter_of_clients)


for product in Counter_of_clients:
    Counter_of_clients[product] = len(Counter_of_clients[product])

print(Counter_of_clients)

DATA = go.Scatter(

    x = list(Counter_of_clients.keys())
    ,
    y = list(Counter_of_clients.values())
)

plotly.offline.plot([DATA], filename='amount_of_cliens_and_producs.html')





def addNewData(client,date,product,quantity,price):
    if client in dataset.keys():

        if date in dataset[client].keys():

            if product in dataset[client][date].keys():

                if quantity in dataset[client][date][product]["quantity"]:
                    quantity_list = [dataset["client"]["date"]["product"]["quantity"]]
                    quantity_list.append(row_dict["quantity"])

                else:
                    dataset[client][date][product]["quantity"] = quantity

                if price in dataset["client"]["date"]["product"]["price"]:
                    price_list = [dataset["client"]["date"]["product"]["price"]]
                    price_list.append(row_dict["price"])
                else:
                    dataset[client][date][product]["price"] = price


            else:
                dataset[client][date][product] = {
                    "quantity":

                        quantity

                    ,
                    "price":

                        price

                }

        else:
            dataset[client][date] = {
                product:
                    {
                        "quantity":

                            quantity

                        ,
                        "price":

                            price

                    }
            }



    else:
        dataset[client] = {
            date:
                {
                    product:
                        {
                            "quantity":

                                quantity

                            ,
                            "price":

                                price

                        }
                }

        }

