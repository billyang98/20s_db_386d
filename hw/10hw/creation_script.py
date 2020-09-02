server = 'localhost'
database = 'hw5'
username = 'sa'
password = 'Password1'
from sqlalchemy import create_engine

engine = []
connection = []

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

def insert_n_random_rows(n, batch_size, queue_size, sequential=True):
    assert n % batch_size == 0
    assert n % queue_size == 0
    assert queue_size % batch_size == 0
    total_time = 0
    print("Doing Sequential Insert")
    for row_num in range(0 , n, queue_size):
        keys = [i for i in range(row_num + 1, row_num + 1 +  queue_size)]

        print("Loading rows {} to {}".format(keys[0], keys[-1]))

        a_s = []
        b_s = []
        fillers = []
        filler_len = 247
        column_range = 100000
        queries = []
        for batch_num in range(0,int(queue_size / batch_size)):
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

        start_time = time.time()
        print("Inserting rows {} to {}".format(keys[0], keys[-1]))
        for i in range(0,int(queue_size / batch_size)):
                tsql = queries[i]
                connection.execute(tsql)
                if ((i+1) * batch_size) % 100000 == 0:
                    print ('Successfully Inserted! {} rows, {} batches of {} \
                        rows'.format((i+1) * batch_size + row_num, i + 1, batch_size))
        elapsed_time = time.time() - start_time
        total_time = total_time + elapsed_time
    print("Sequential Insert")
    print(str(timedelta(seconds=total_time)))
        

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--sequential', type=bool, default=False,
                   help='insert rows sequentially or randomly')
parser.add_argument('--num_rows', type=int, default=20,
                   help='number of rows to insert')
parser.add_argument('--batch_size', type=int, default=5,
                   help='how many rows to insert per batch')
parser.add_argument('--queue_size', type=int, default=10,
                   help='how many rows to preload at a time')
parser.add_argument('--remote', type=bool, default=False,
                   help='connect to remote or local database')



def connect_db(remote):
    global engine
    global connection
    engine = create_engine(
        "postgresql+psycopg2://postgres:!Aa32159753postgres@db-hw.c4cqvq8fwlnk.us-east-1.rds.amazonaws.com:5432/db_hw"
    )
#    else:
#        engine = create_engine(
#            "postgresql+psycopg2://postgres:password@localhost:5432/db_hw"
#        )
    connection = engine.connect()

if __name__ == "__main__":
    args = parser.parse_args()
    connect_db(args.remote)
    insert_n_random_rows(args.num_rows, args.batch_size, args.queue_size);
    


