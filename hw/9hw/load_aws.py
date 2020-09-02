server = 'localhost'
database = 'hw5'
username = 'sa'
password = 'Password1'
from sqlalchemy import create_engine
import psycopg2

engine = []
connection = []
cur = []
conn = []

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


def insert_n_rows(n, batch_size, sequential=True):
#    assert n % batch_size == 0
    low  = 2300000
    high = 5000000
    time_increment_count = 100000

    a_s = []
    b_s = []
    fillers = []
    filler_len = 233
    queries = []
    tables = ['A', 'B', 'C', 'Aprime', 'Bprime', 'Cprime']
    start_time = time.time()
    prev_time = start_time
    for batch_num in range(low + 1, high, batch_size):
        query_arr = []
        for batch_item in range(batch_num, batch_num + batch_size):
            ht = random.randint(0, 100000)
            tt = random.randint(0, 10000)
            ot = random.randint(0, 1000)
            hund = random.randint(0, 100)
            ten = random.randint(0, 10)
            filler = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k = filler_len))
            query = ' ({}, {}, {}, {}, {}, {}, \'{}\'), '.format(
                        batch_item, ht, tt, ot, hund, ten, filler)
            if batch_item == batch_num + batch_size - 1:
                query = ' ({}, {}, {}, {}, {}, {}, \'{}\') '.format(
                    batch_item, ht, tt, ot, hund, ten, filler)
            query_arr.append(query)
        query_rows = " ".join(query_arr)
        for table_name in tables:
            query_base = 'INSERT INTO {} (pk, ht, tt, ot, hund, ten, filler) \
                            VALUES '.format(table_name)
            query = query_base + ' ' + query_rows 
            cur.execute(query)
        conn.commit()
        if (batch_num + batch_size - 1) % time_increment_count == 0:
            get_times(start_time, prev_time, batch_num + batch_size - 1,
                        time_increment_count)
            prev_time = time.time()
        
def get_times(start_time, prev_time, total, inc):
    total_time = time.time() - start_time
    time_since = time.time() - prev_time
    print('{} total rows : {} '.format(total, str(timedelta(seconds=total_time))))
    print('{} rows : {} '.format(inc, str(timedelta(seconds=time_since))))
    print('{} per row'.format(str(timedelta(seconds=time_since/inc))))


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--sequential', type=bool, default=False,
                   help='insert rows sequentially or randomly')
parser.add_argument('--num_rows', type=int, default=5,
                   help='number of rows to insert')
parser.add_argument('--batch_size', type=int, default=5,
                   help='how many rows to insert per batch')
parser.add_argument('--remote', type=bool, default=False,
                   help='connect to remote or local database')

def connect_db(remote):
    global cur
    global conn
    conn = psycopg2.connect(host="db-hw.c4cqvq8fwlnk.us-east-1.rds.amazonaws.com",database="db_hw", user="postgres", password="!Aa32159753postgres")
    cur = conn.cursor()
#    engine = create_engine(
#        "postgresql+psycopg2://postgres:!Aa32159753postgres@db-hw.c4cqvq8fwlnk.us-east-1.rds.amazonaws.com:5432/db_hw"
#    )
#    connection = engine.connect()

if __name__ == "__main__":
    args = parser.parse_args()
    connect_db(args.remote)
    insert_n_rows(args.num_rows, args.batch_size, args.sequential);
    


