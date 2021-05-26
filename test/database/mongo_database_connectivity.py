from pymongo import MongoClient, errors
import ssl

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


# myclient = MongoClient('localhost', 27017)
# mydb = myclient["rasa"]
# mycollection = mydb["users"]

myclient = MongoClient("mongodb+srv://test:test@whoabotcluster.lv9q9.mongodb.net/rasa?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient.get_database('rasa')
mycollection = mydb.users

def mongodataupdate(per_id, fname, lname):
    # name = name.lower()
    if per_id != 'none':
        person_list = {"_id": per_id, "First_Name": fname, "Last_Name": lname}
        try:
            mycollection.insert_one(person_list)
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return

        for x in mycollection.find():
            print(x)


def mongodataverify(per_id):
    count = mycollection.count_documents({"_id": per_id})
    return count


def mongohobbyupdate(per_id, hobby1, hobby2, hobby3):
    hobby1 = hobby1.lower()
    hobby2 = hobby2.lower()
    hobby3 = hobby3.lower()
    if hobby1 != 'none' or hobby2 != 'none' or hobby3 != 'none':
        query = {"_id": per_id}
        values = {"$set": {"hobby1": hobby1, "hobby2": hobby2, "hobby3": hobby3}}
        try:
            mycollection.update_one(query, values)
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return
        for x in mycollection.find():
            print(x)


def mongohobbyretrieve(per_id):
    if per_id != 'none':
        hobby1 = None
        hobby2 = None
        hobby3 = None

        try:
            result = mycollection.find_one({"_id": per_id})
            if "hobby1" in result:
                hobby1 = result["hobby1"]
            if "hobby2" in result:
                hobby2 = result["hobby2"]
            if "hobby3" in result:
                hobby3 = result["hobby3"]
        except errors.DuplicateKeyError as e:
            print("Error: {}".format(e))
            return
        return hobby1, hobby2, hobby3


# if __name__ == "__main__":
#     print(mongodataverify("1"))
