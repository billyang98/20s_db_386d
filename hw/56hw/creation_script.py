import pyodbc
server = 'localhost'
database = 'hw5'
username = 'sa'
password = 'Password1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Insert Query
def insert_example():
    tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
    with cursor.execute(tsql,'Jake','United States'):
        print ('Successfully Inserted!')

import string
import choices 
import random
import time
from datetime import timedelta

def insert_n_random_rows(n, batch_size, sequential=True):
    assert n % batch_size == 0
    keys = [i for i in range(1, n+1)]
    if not sequential:
        print("Doing Random Insert")
        random.shuffle(keys)
    else:
        print("Doing Sequential Insert")

    a_s = []
    b_s = []
    fillers = []
    filler_len = 247
    column_range = 50000
    queries = []
    for batch_num in range(0,int(n / batch_size)):
        query_arr = ['INSERT INTO benchmark (theKey, columnA, columnB, filler)  VALUES ']
        for batch_item in range(0, batch_size):
            key_index = batch_num * batch_size + batch_item
            a = random.randint(1, column_range + 1)
            b = random.randint(1, column_range + 1)
            filler = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k = filler_len))
            query = ' ({}, {}, {}, \'{}\'), '.format(keys[key_index], a, b, filler)
            if batch_item == batch_size - 1:
                query = ' ({}, {}, {}, \'{}\') '.format(keys[key_index], a, b, filler)
            query_arr.append(query)
            if (key_index+1) % 100000 == 0:
                print("Made {} rows".format(key_index+1))
        query = " ".join(query_arr)
        queries.append(query)

#    OLD CODE SINGLE INSERTS
#    for i in range(0,n):
#        a = random.randint(1, column_range + 1)
#        b = random.randint(1, column_range + 1)
#        filler = ''.join(random.choices(string.ascii_uppercase +
#                                 string.digits, k = filler_len))
#        a_s.append(a)
#        b_s.append(b)
#        fillers.append(filler)
#        queries.append("INSERT INTO benchmark (theKey, columnA, columnB,\
#            filler)  VALUES ({},{},{},'{}')".format(keys[i], a, b, filler))
#        if (i+1) % 100000 == 0:
#            print("Made {} rows".format(i+1))
#    start_time = time.time()
#    for i in range(0,n):
#            b = random.randint(1, column_range + 1)
#            key = keys[i]
#            a = a_s[i]
#            b = b_s[i]
#            filler = fillers[i]
#            tsql = queries[i]
#            with cursor.execute(tsql):
#                if (i+1) % 100000 == 0:
#                    print ('Successfully Inserted! {} rows'.format(i+1))

    start_time = time.time()
    for i in range(0,int(n / batch_size)):
            tsql = queries[i]
            with cursor.execute(tsql):
                if ((i+1) * batch_size) % 100000 == 0:
                    print ('Successfully Inserted! {} rows, {} batches of {} \
                        rows'.format((i+1) * batch_size, i + 1, batch_size))
    elapsed_time = time.time() - start_time
    if not sequential:
        print("Random Insert")
    else:
        print("Sequential Insert")
    print(str(timedelta(seconds=elapsed_time)))
        

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--sequential', type=bool, default=False,
                   help='insert rows sequentially or randomly')
parser.add_argument('--num_rows', type=int, default=5,
                   help='number of rows to insert')
parser.add_argument('--batch_size', type=int, default=5,
                   help='how many rows to insert per batch')

if __name__ == "__main__":
    args = parser.parse_args()
    insert_n_random_rows(args.num_rows, args.batch_size, args.sequential);
    


