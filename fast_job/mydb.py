import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1', 
    port = '3306',
    user = 'root',
    passwd = '',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE fast_job")