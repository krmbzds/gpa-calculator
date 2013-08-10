

def initialize_db(db_name="grades.db"):
    conn = sqlite3.connect(db_name)
    conn.close()
    print("\nDatabase initialized.")


def create_tables(db_name='grades.db', table='grades'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('CREATE TABLE %s (className text, semesterHours int, letterGrade text)' % table)
    conn.commit()
    conn.close()
    print("\nCreated '%s' table on '%s' database." % (table, db_name))


def insert_into_table(className, semesterHours, letterGrade, db_name='grades.db', table='grades'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    values = [className, semesterHours, letterGrade]
    statement = "INSERT INTO %s VALUES (?,?,?)" % table
    c.execute(statement, values)
    conn.commit()
    conn.close()


def fetch_results(db_name='grades.db', table='grades'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM %s" % table)
    rows = c.fetchall()
    conn.close()

    t = prettytable.PrettyTable(["Class Name", "Credit", "Grade"])
    for row in rows:
        t.add_row([row[0], row[1], row[2]])

    g = prettytable.PrettyTable(["Quality Points", "Total Credit", "Cumulative GPA"])
    g.add_row(cumulative_gpa())

    print(t.get_string(hrules=prettytable.ALL))
    print(g.get_string(hrules=prettytable.ALL))


def cumulative_gpa(db_name='grades.db', table='grades'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM %s" % table)
    rows = c.fetchall()
    conn.close()

    total_hours, quality_points = 0, 0

    catalog = {"A+": 4.3, "A": 4.0, "A-": 3.7,
               "B+": 3.3, "B": 3.0, "B-": 2.7,
               "C+": 2.3, "C": 2.0, "C-": 1.7,
               "D+": 1.3, "D": 1.0, "D-": 0.7,
               "F": 0, "U": 0, "IA": 0}

    for row in rows:
        total_hours += int(row[1])
        quality_points += int(row[1]) * catalog[row[2]]

    gpa = math.ceil((quality_points / total_hours) * 100) / 100

    return [quality_points, total_hours, gpa]


def collect_input():
    while True:
        print("")
        insert_into_table(input("Class Name: "), input("Semester Hours: "), input("Letter Grade: "))
        response = input("\nAdd another line? (Y/n) ").lower()
        if response:
            if response[0] == "n":
                break
            elif response[0] == "y":
                pass
            else:
                raise Exception("Wrong Input")
                break


def collect_input_add():
    response = input("\nAdd more grades? (y/N) ").lower()
    if response:
        if response[0] == "n":
            pass
        elif response[0] == "y":
            collect_input()
        else:
            raise Exception("Wrong Input")


def db_exists(db_name="grades.db"):
    return os.path.isfile(db_name)


def main():
    if db_exists():
        print("\nFound an existing database...")
        collect_input_add()
        fetch_results()
    else:
        print("\nNo grades database found...")
        input("\nPress any key to intialize the database and start adding grades.")
        initialize_db()
        create_tables()
        collect_input()
        fetch_results()


if __name__ == "__main__":
    import os
    import math
    import sqlite3
    import prettytable

    main()
