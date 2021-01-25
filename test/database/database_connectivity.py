import mysql.connector


def dataupdate(name):
    name = name.lower()
    if name != 'none':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saumitra",
            database="rasa",
            auth_plugin="mysql_native_password"
        )
        mycursor = mydb.cursor()
        # sql = "CREATE TABLE users (name VARCHAR(50) PRIMARY KEY);"
        sql = 'INSERT INTO users (name) VALUES ("{0}");'.format(name)

        try:
            mycursor.execute(sql)
        except mysql.connector.IntegrityError as e:
            print("Error: {}".format(e))
            return

        mydb.commit()
        print(mycursor.rowcount, " record(s) inserted")


def dataverify(name):
    name = name.lower()
    if name != 'none':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saumitra",
            database="rasa",
            auth_plugin="mysql_native_password"
        )
        mycursor = mydb.cursor()
        verifysql = 'SELECT name FROM users WHERE name= "{}";'.format(name)

        mycursor.execute(verifysql)
        resultant = mycursor.fetchall()
        mydb.commit()
        # gets the number of rows affected by the command executed
        row_count = mycursor.rowcount
        return row_count
    else:
        return 1


def hobbyupdate(hobby, number, name):
    hobby = hobby.lower()
    name = name.lower()
    if hobby != 'none':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saumitra",
            database="rasa",
            auth_plugin="mysql_native_password"
        )
        mycursor = mydb.cursor()
        # sql = "CREATE TABLE users (name VARCHAR(50) PRIMARY KEY);"
        if number == 1:
            sql = 'UPDATE users SET hobby1 = "{}" WHERE name = "{}";'.format(hobby, name)
        elif number == 2:
            sql = 'UPDATE users SET hobby2 = "{}" WHERE name = "{}";'.format(hobby, name)
        elif number == 3:
            sql = 'UPDATE users SET hobby3 = "{}" WHERE name = "{}";'.format(hobby, name)

        try:
            mycursor.execute(sql)
        except mysql.connector.IntegrityError as e:
            print("Error: {}".format(e))
            return

        mydb.commit()
        print(mycursor.rowcount, " record(s) updated")


def hobbyretrieve(name):
    name = name.lower()
    if name != 'none':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saumitra",
            database="rasa",
            auth_plugin="mysql_native_password"
        )
        mycursor = mydb.cursor()
        # sql = "CREATE TABLE users (name VARCHAR(50) PRIMARY KEY);"

        sql = 'SELECT hobby1, hobby2, hobby3 FROM users WHERE name = "{}";'.format(name)

        try:
            mycursor.execute(sql)
            result = mycursor.fetchall()
            hobby1 = result[0][0]
            hobby2 = result[0][1]
            hobby3 = result[0][2]
        except mysql.connector.IntegrityError as e:
            print("Error: {}".format(e))
            return
        mydb.commit()
        return hobby1, hobby2, hobby3


# if __name__ == "__main__":
#     hobbyretrieve("mihir")
    # hobbyupdate("Painting", 1, "saumitra")
    # dataupdate("saumitra")
    # rows = dataverify("adam")
    # if rows == 0:
    #     print("It Does Not Exist")
    # else:
    #     print("number of rows: {}".format(rows))
