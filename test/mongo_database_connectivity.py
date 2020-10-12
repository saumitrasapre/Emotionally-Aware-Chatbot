from pymongo import MongoClient, errors


# myclient = MongoClient('localhost', 27017)
# print(myclient.list_database_names())
#
# mydb = myclient["rasa"]
# mycollection = mydb["users"]
#
# record = mycollection.find_one()
# print(record)
#
# for x in mycollection.find():
#     print(x)


def mongodataupdate(name):
    name = name.lower()
    if name != 'none':
        myclient = MongoClient('localhost', 27017)
        mydb = myclient["rasa"]
        mycollection = mydb["users"]

        name_list = {"name": name}
        try:
            mycollection.insert_one(name_list)
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return

        for x in mycollection.find():
            print(x)


def mongodataverify(name):
    name = name.lower()
    if name != 'none':
        myclient = MongoClient('localhost', 27017)
        mydb = myclient["rasa"]
        mycollection = mydb["users"]

        count = mycollection.count_documents({"name": name})
        print(count)
        return count
    else:
        return 1


def mongohobbyupdate(hobby1,hobby2,hobby3, name):
    hobby1 = hobby1.lower()
    hobby2 = hobby2.lower()
    hobby3 = hobby3.lower()
    name = name.lower()
    if hobby1 != 'none' or hobby2!='none' or hobby3!='none':
        myclient = MongoClient('localhost', 27017)
        mydb = myclient["rasa"]
        mycollection = mydb["users"]
        query = {"name": name}
        values = {"$set": {"hobby1": hobby1,"hobby2":hobby2,"hobby3":hobby3}}
        try:
            mycollection.update_one(query, values)
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return
        for x in mycollection.find():
            print(x)


def mongohobbyretrieve(name):
    name = name.lower()
    if name != 'none':
        myclient = MongoClient('localhost', 27017)
        mydb = myclient["rasa"]
        mycollection = mydb["users"]

        try:
            result = mycollection.find_one({"name": name})
            hobby1 = result["hobby1"]
            hobby2 = result["hobby2"]
            hobby3 = result["hobby3"]
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return
        return hobby1, hobby2, hobby3


# if __name__ == "__main__":
#     mongohobbyretrieve("saumitra")
    # mongohobbyupdate("reading", 2, "Saumitra")
    # mongodataupdate("Saumitra")
    # mongodataverify("Saumitra")
