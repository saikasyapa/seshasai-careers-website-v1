import mysql.connector
#import os

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


import mysql.connector


def add_applications_to_db(job_id, data):

  cursor = mydb.cursor()

  add_application = (
      "INSERT INTO auroraconsulting.applications "
      "(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
      "VALUES (%s, %s, %s, %s, %s, %s, %s)")

  application_data = (job_id, data['full_name'], data['email'],
                      data['linkedin_url'], data['education'],
                      data['work_experience'], data['resume_url'])

  cursor.execute(add_application, application_data)

  mydb.commit()

  cursor.close()
  mydb.close()


# mycursor = mydb.cursor(dictionary=True)
# def add_applications_to_db(job_id,full_name):

# # Assuming you have a table named 'your_table' with columns 'column1', 'column2', and 'column3'
# # You will receive the data from the user and then insert it into the table

# # SQL query to insert data into the table
#  insert_query = "INSERT INTO auroraconsulting.applications (job_id, full_name) VALUES (%s, %s)"

# # Data to be inserted into the table
#  values = (job_id, full_name)

# # Execute the query
#  mycursor.execute(insert_query, values)

# # Commit changes to the database
#  mydb.commit()

# # Close the cursor and database connection
#  mycursor.close()
#  mydb.close()

# def add_applications_to_db(job_id, application):
#     mycursor = mydb.cursor(dictionary=True)
#     add_application = ("INSERT INTO auroraconsulting.applications "
#                        "(job_id, full_name, email, linkedin_url, education, experience, resume_url) "
#                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")

#     application_data = (
#         application['job_id'],
#         application['full_name'],
#         application['email'],
#         application['linkedin_url'],
#         application['education'],
#         application['experience'],
#         application['resume_url']
#     )

#     mycursor.execute(add_application, application_data)
#     mydb.commit()
#     mycursor.close()
#     mydb.close()
