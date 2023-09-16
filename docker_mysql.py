import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    password="dlgydlf",
    host="localhost",
    port="13306"
)
cursor = cnx.cursor()

while True:
    print("User管理データベース (1: select, 2: insert, 3: update, 4: delete, 0: exit)")
    menu = int(input())

    if menu == 1: # select
        cursor.execute("SELECT * FROM supu_db.users")
        for id, name in cursor:
                print(f"{id}: {name}")
    elif menu == 2: # insert
        query = "INSERT INTO supu_db.users(name) values(%s)"
        name = input("please input user name-> ")
        data = (name,)
        cursor.execute(query, data) 
        cnx.commit()
    elif menu == 3: # update
        id = input("please input user id-> ")
        name = input("please input user name-> ")
        query = "UPDATE supu_db.users SET name = %s WHERE id = %s"
        data = (name, id)
        cursor.execute(query, data) 
        cnx.commit()
    elif menu == 4: # delete
        id = input("please input user id-> ")
        query = "DELETE FROM supu_db.users WHERE id = %s"
        data = (id,)
        cursor.execute(query, data) 
        cnx.commit()
    else: # exit
        cursor.close()
        cnx.close()
        break

