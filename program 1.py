import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    # Delete table if it exists
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table
    cur.execute('''CREATE TABLE Entries(
                    ID INTEGER PRIMARY KEY NOT NULL, 
                    NAME TEXT,
                    GRADE TEXT,
                    GRADE_PERCENTAGE FLOAT,
                    CLASS TEXT,
                    MAJOR TEXT,
                    CITY TEXT)''')

    # Data to insert
    data = [
        (1, 'Abraham Anderson', 'B', 87.52, 'COS2005', 'Business', 'St. Paul'),
        (2, 'Sabria Fafach', 'A', 92.37, 'COS2005', 'Art', 'Maple Grove'),
        (3, 'Ainsley Bellamy', 'C', 78.94, 'COS2005', 'Culinary', 'Blaine'),
        (4, 'Violet Haveman', 'A', 98.12, 'COS2005', 'Medical', 'Minneapolis'),
        (5, 'Ben Krehbiel', 'C', 70.94, 'COS2005', 'Finance', 'Coon Rapids'),
        (6, 'Lucia Floan', 'B', 81.85, 'COS2005', 'Economics', 'Champlin')
    ]

    # Insert data
    cur.executemany('''INSERT INTO Entries (ID, Name, Grade, Grade_percentage, Class, Major, City)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''', data)

    # Save and close
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
