import sqlite3

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('mydata.db')

### crates an inmemoery db for Unit Tests
# conn = sqlite3.connect(':memory:')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert data
cursor.execute('''
    INSERT INTO users (name, email) VALUES (?, ?)
''', ("Alice", "alice@example.com"))

# Commit the changes
conn.commit()

# Query the data
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

# Close the connection
conn.close()


### supported features

# * Foreign keys -- cursor.execute("PRAGMA foreign_keys = ON;")
# * Transactional DDL
# * Full Text Search using FTS5 extensions
# * JSON support  with json1 extension -- built in in many distributions
# * Write Ahead Logging (WAL) mode for improved concurrency

### Limitations

# * Concurrency -- SQLite locks the entire database during writes -- not ideal for high-traffic web apps
# * Size constraints -- not suitable for massive datasets or high throughput analytics
# * Non built in use authentication

### Strengths
# * Good integration use with Pandas -- df = pd.read_sql_query("SELECT * FROM users", conn)
# * Tools -- DB Browser for SQLite -- allows no-code db operations
