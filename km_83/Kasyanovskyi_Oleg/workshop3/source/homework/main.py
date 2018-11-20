dataset={

"bob":{
            "gender":"M",
            "dirrection":"python",

            "route":{
                       "str1": {
                            "str_name":"str1",
                            "transport":{
                                            "type":"tram",
                                            "price":10
                                         }
                        },
                        "str2":{
                            "str_name": "str2",
                            "transport": {
                                "type": "bus",
                                "price": 8
                            }
                        }
                     }
}

,

"boba":{
            "gender":"F",
            "dirrection":"shopping",

            "route":{
                        "str1":{
                                "str_name": "str2",
                                "transport": {
                                            "type": "car",
                                            "price": 50}
                            }
                        }
            }


}

total=0
for street in dataset["bob"]["route"].keys():
    price = dataset["bob"]["route"][street]["transport"]["price"]
    total+=price
    print(street,price)
print(total)

def listkey(dataset):
    Key=[i for i in dataset.keys()]
    return Key
Key=listkey(dataset)
def print_name(dataset,Key):
    if Key==[]:
        return None
    if dataset[Key[0]]["gender"]=="M":
        print(Key[0])
    return print_name(dataset, Key[1:])
print_name(dataset,Key)
Key=listkey(dataset)
def spend(name,dataset):
    if name not in Key:
        print("Нема такого імені")
        return
    total = 0
    for street in dataset[name]["route"].keys():
        price = dataset[name]["route"][street]["transport"]["price"]
        total += price
        print(street, price)
    print("total =",total)
    return total
spend('boba',dataset)

def get_amount(dataset,str1,i=0):

    Keys=listkey(dataset)

    if i==len(Keys):
        return 0

    x=0
    for j in dataset[Keys[i]]["route"].keys():
        if j == "str1":
            x+=1

    return x+get_amount(dataset,str1,i+1)
print("total in street",get_amount(dataset,"str1"))


