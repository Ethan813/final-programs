import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')
cur = conn.cursor()

def new_entry(ID, Name, Grade, Grade_percentage, Class, Major, City):
    cur.execute('INSERT INTO Entries (ID, Name, Grade, Grade_percentage, Class, Major, City) VALUES (?, ?, ?, ?, ?, ?, ?)',(ID, Name, Grade, Grade_percentage, Class, Major, City))
    print(f'Added: {ID} - {Name} - {Grade} - {Grade_percentage} - {Class} - {Major} - {City}')
def edit_entry(ID, Name, Grade, Grade_percentage, Class, Major, City):
    cur.execute('UPDATE Entries SET Name=? Grade=? Grade_percentage=? Class=? Major=? City=? WHERE ID = ?',(new_name, new_grade, new_grade_percentage, new_class, new_major, new_city, ID))
    print(f"{ID}'s data is now {Name} - {Grade} - {Grade_percentage} - {Class} - {Major} - {City}")
def delete(ID):
    cur.execute('DELETE FROM Entries WHERE ID = ?', (ID,))
    print(f'{ID} has been deleted')
def print_all():
    for row in cur.execute("select * from Entries"):
        print(row)



def main():


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

while True:
    print("\nStudents database options")
    print("1. Add an entry")
    print("2. Edit student data")
    print("3. Delete an entry")
    print("4. Display all entries")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        ID = input("Enter ID: ")
        Name = input("Enter name: ")
        Grade = input("Enter grade: ")
        Grade_percentage = input("Enter grade percentage: ")
        Class = input("Enter class: ")
        Major = input("Enter major: ")
        City = input("Enter city: ")
        new_entry(ID, Name, Grade, Grade_percentage, Class, Major, City)

    elif choice == '2':
        ID = input("Enter ID: ")
        new_name = input("Enter new name: ")
        new_grade = input("Enter new grade: ")
        new_grade_percentage =  input("Enter new grade percentage: ")
        new_class = input("Enter new class: ")
        new_major = input("Enter new major: ")
        new_city = input("Enter new city")
        edit_entry(ID, new_name, new_grade, new_grade_percentage, new_class, new_major, new_city)
    elif choice == '3':
        ID = input("Enter ID: ")
        delete(ID)
    elif choice == '4':
        print_all()
    elif choice == '5':
        conn.commit()
        break
    else:
        print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()
