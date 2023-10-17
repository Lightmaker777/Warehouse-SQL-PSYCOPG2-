import psycopg2


# connect to postgres and print its version
def read_database_version():
    conn = psycopg2.connect(dbname='postgres',
                            user='postgres',
                            password='postgres',
                            host='localhost',
                            port=5432)
    # Create a cursor object
    cur = conn.cursor()
    # Execute the SQL query to get the database server version
    cur.execute("SELECT version()")
    # Get the results
    version = cur.fetchone()[0]
    # Print the database server version
    print(version)
    # Close the cursor and connection objects
    cur.close()
    conn.close()


read_database_version()
