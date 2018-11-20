dataset={
    "Reader_Bob":{
        "name":"Bob",
        "group ":"KM_83",
        "age":18,
        "books":{
            "namebook":["book1","book2"],
            "genre":{"genre1","genre2"}
        }

    },
    "Reader_Boba":{
        "name":"Boba",
        "group ":"KM_82",
        "age":17,
        "books":{
            "namebook":["book2","book3"],
            "genre":{"genre2","genre3"}
        }
    }
}

Key=[i for i in dataset.keys()]
def listkey(dataset):
    Key=[i for i in dataset.keys()]
    return Key

def print_readers(dataset,Key):
    if Key==[]:
        return None
    name=Key[0]
    print(name)
    return print_readers(dataset,Key[1:])
print_readers(dataset,Key)

def numbers_of_genres(dataset,genre,i=0):
    Keys = listkey(dataset)

    if i == len(Keys):
        return 0

    x = 0
    for j in dataset[Keys[i]]["books"]["genre"]:
        if j == genre:
            x += 1

    return x + numbers_of_genres(dataset, genre, i + 1)
print(numbers_of_genres(dataset,"genre1"))
print(numbers_of_genres(dataset,"genre2"))
print(numbers_of_genres(dataset,"genre3"))
