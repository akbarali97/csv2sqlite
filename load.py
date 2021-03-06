# import nessessary packages
import sqlite3
import csv
import sys


# to load the values from the csv file into a list of tuples
def loadcsv(filename):
    with open(filename, newline='') as f:
        try:
            return [tuple(row) for row in csv.reader(f)]
        except Exception as e:
            sys.exit(e)


# write data into the sqlite database.
def create_database(db_file, table_headers, table_rows):
    try:
        with sqlite3.connect(db_file) as con:
            table_name = db_file.split('.')[0]
            table_name = ''.join(e for e in table_name if e.isalnum())
            query = f"create table {table_name} {table_headers}"
            print (query)
            con.execute(query)
            for i in table_rows:
                query = f"insert into {table_name} values {i}"
                con.execute(query)
                print(query)
    except Exception as e:
        print(e)
    finally:
        con.close()

# main method
def main():

    #get filename from user
    filename = input()
    db_filename = filename.split('.')[0] + '.sqlite3'

    # load load the values from the csv file
    csv_list = loadcsv(filename)
    if csv_list == []: sys.exit('Null CSV file')

    # write into DB
    table_headers = csv_list[0]
    table_rows = csv_list[1:]
    create_database(db_filename,table_headers,table_rows)


if __name__ == '__main__':
    main()
