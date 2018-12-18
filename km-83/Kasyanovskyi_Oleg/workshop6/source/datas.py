
import plotly as pl
import plotly.graph_objs as go
from plotly import tools

import re
def get_address(line):
    if line[0] == '"':
        Res = line[1:].split(",")
        return Res[0], Res[1:]
    else:
        y = line.split(",")
        return y[0], y[1:]
def get_city(line):

    result = re.split(r",",line,maxsplit=1)
    return result[0], result[1:]


def get_country(line):
    result = re.split(r",", line, maxsplit=1)
    return result[0], result[1:]

try:

    with open("data/FastFoodRestaurants.csv","r",encoding = "utf8") as file:
        limit = 100

        dataset = dict()
        current_line = 0
        header = file.readline().rstrip()
        header_list = [colums.strip() for colums in header.split(",")]

        product_index = header_list.index("address")
        z= 0
        for line in file:

            if z >= limit:
                break
            if not line.rstrip():
                continue

            rows = line.strip().split(",")


            z+=1

            line_list = line.rstrip().strip().split(",")

            row_dict = dict(zip(header_list, line_list))



            if row_dict["country"] in dataset.keys():

                if row_dict["city"] in dataset[row_dict["country"]].keys():

                    if row_dict["address"] in dataset[row_dict["country"]][row_dict["city"]].keys():

                        if row_dict["name"] in dataset[row_dict["country"]][row_dict["city"]][row_dict["address"]]:
                            dataset[row_dict["country"]][row_dict["city"]][row_dict["address"]] = {row_dict["name"]}

                        else:
                            dataset[row_dict["country"]][row_dict["city"]][row_dict["address"]].add(row_dict["name"])

                    else:
                        dataset[row_dict["country"]][row_dict["city"]][row_dict["address"]] = {
                            row_dict["name"]
                        }

                else:
                    dataset[row_dict["country"]][row_dict["city"]] = {
                        row_dict["address"]:
                            {
                                row_dict["name"]
                            }
                    }

            else:
                dataset[row_dict["country"]] = {
                    row_dict["city"]:
                        {
                            row_dict["address"]:
                                {
                                    row_dict["name"]
                                }
                        }
                }



        data_1 = dict()
        list_of_magaz = []
        for country in dataset.keys():
            for city in dataset[country].keys():
                for address in dataset[country][city].keys():
                    for name in dataset[country][city][address]:

                        list_of_magaz.append(name)
                data_1[country] = len(list_of_magaz)




        DATA_1 = go.Bar(
            x = list(data_1.keys()),
            y = list(data_1.values()),
            name = "amount_of_fast_food"
        )
        Set_of_mag = set(list_of_magaz)
        data_2 = dict()


        for country in dataset.keys():
            for city in dataset[country].keys():
                for address in dataset[country][city].keys():
                    for name in dataset[country][city][address]:



                        data_2[name] = list_of_magaz.count(name)

        DATA_2 = go.Pie(

            labels = list(data_2.keys()),
            values = list(data_2.values()),

        )
        data_3 = dict()
        list_of_cities = []
        for country in dataset.keys():
            for city in dataset[country].keys():
                list_of_cities.append(city)

            data_3[country] = len(list_of_cities)

        DATA_3 = go.Bar(

            x = list(data_3.keys()),
            y = list(data_3.values()),
            name="cities"
        )

        fig = tools.make_subplots(rows=1, cols=2)

        fig.append_trace(DATA_1, 1, 1)

        fig.append_trace(DATA_3, 1, 2)

        pl.offline.plot(fig, filename='Bars.html')
        pl.offline.plot([DATA_2], filename='Pie.html')

except IOError:
    print(1)