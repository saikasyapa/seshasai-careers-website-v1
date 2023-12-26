
# from sqlalchemy import create_engine

# # Replace 'username', 'password', 'host', 'database_name' with your AWS RDS MySQL credentials
# # Replace 'us-west-2' with your AWS region and 'mydbinstance' with your RDS instance identifier
# engine = create_engine('mysql+pymysql://admin:SNRKumari.1919@database-1.crl8y9bwsxyd.us-east-1.rds.amazonaws.com:3306/mysql')

# connection = engine.connect()

# # Perform operations using this connection
# # For example, executing raw SQL queries:
# result = connection.execute("SELECT * FROM jobs")
# for row in result:
#     print(row)

# # Close the connection when done
# connection.close()


# # Example connection string:
# # engine = create_engine('mysql+pymysql://myusername:mypassword@mydbinstance.abcdefghijkl.us-west-2.rds.amazonaws.com:3306/mydatabase')






# import mysql.connector

# # Establish a connection to the MySQL database
# mydb = mysql.connector.connect(
#     host="database-1.crl8y9bwsxyd.us-east-1.rds.amazonaws.com",
#     user="admin",
#     password="SNRKumari.1919",
#     database="mysql"
# )

# # Create a cursor object to interact with the database
# mycursor = mydb.cursor()

# # Example: Selecting data from a table
# mycursor.execute("SELECT * FROM auroraconsulting.myjobs")


# # Fetch all rows from the query
# rows = mycursor.fetchall()
# print(type(rows))



# # #Function to convert rows to dictionaries
# # def row_to_dict(cursor, row):
# #     columns = [col[0] for col in cursor.description]
# #     return dict(zip(columns, row))

# # # Convert each row to a dictionary
# # result = [row_to_dict(mycursor, row) for row in rows]

# # # Printing the list of dictionaries
# # for row_dict in result:

# #     print(row_dict)
# #     print(type(row_dict))
