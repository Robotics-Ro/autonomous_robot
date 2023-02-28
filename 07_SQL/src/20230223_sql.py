import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "1234",
# )

local = mysql.connector.connect(
    host = "database-1.cystwsvet7ac.us-east-1.rds.amazonaws.com",
    port = 3306,
    user = "admin",
    password = "vandred87"
    database = "amrbase"
)
