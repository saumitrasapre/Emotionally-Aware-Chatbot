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


if __name__ == "__main__":
    # dataupdate("saumitra")
    rows = dataverify("adam")
    if rows == 0:
        print("It Does Not Exist")
    else:
        print("number of rows: {}".format(rows))
