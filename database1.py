
from sqlalchemy import create_engine

# Replace 'username', 'password', 'host', 'database_name' with your AWS RDS MySQL credentials
# Replace 'us-west-2' with your AWS region and 'mydbinstance' with your RDS instance identifier
engine = create_engine('mysql+pymysql://admin:SNRKumari.1919@database-1.crl8y9bwsxyd.us-east-1.rds.amazonaws.com:3306/mysql')

connection = engine.connect()

# Perform operations using this connection
# For example, executing raw SQL queries:
result = connection.execute("SELECT * FROM jobs")
for row in result:
    print(row)

# Close the connection when done
connection.close()


# Example connection string:
# engine = create_engine('mysql+pymysql://myusername:mypassword@mydbinstance.abcdefghijkl.us-west-2.rds.amazonaws.com:3306/mydatabase')
