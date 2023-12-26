import mysql.connector
# import os

# db_connection_string = os.environ['DB_CONNECTION_STRING']

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="database-1.crl8y9bwsxyd.us-east-1.rds.amazonaws.com",
    user="admin",
    password="SNRKumari.1919",
    database="mysql",
    ssl_ca="us-east-1-bundle.pem"  # Specify SSL CA path if needed
)


def load_jobs_from_db():
  # Create a cursor to execute SQL queries
  mycursor = mydb.cursor(dictionary=True)  # Set dictionary mode for cursor

  # Execute SQL query to fetch all jobs
  mycursor.execute("SELECT * FROM auroraconsulting.myjobs")

  # Fetch all rows and convert them into dictionaries
  jobs = mycursor.fetchall()

  # Close the cursor
  mycursor.close()

  return jobs


def load_job_from_db(id):
  # Create a cursor to execute SQL queries
  mycursor = mydb.cursor(dictionary=True)  # Set dictionary mode for cursor

  # Execute SQL query to fetch a specific job by ID
  mycursor.execute("SELECT * FROM auroraconsulting.myjobs WHERE id = %s",
                   (id, ))

  # Fetch the row and convert it into a dictionary
  row = mycursor.fetchone()

  # Close the cursor
  mycursor.close()

  return row
