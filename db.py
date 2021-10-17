import sqlite3

def create_table():
    db = sqlite3.connect('factstable.db')
    cur = db.cursor()
    statement = 'CREATE TABLE if not exists facts(id integer, fact text, PRIMARY KEY(id))'
    cur.execute(statement)
    db.close()


def insert_to_table():

    fact_file = open('facts.txt')
    fact_string = fact_file.read()
    fact_list = fact_string.split(',')
    return fact_list

def register_fact():
    db = sqlite3.connect('factstable.db')
    cur = db.cursor()

    statement = 'insert into facts (fact) values(?)'
    for i in insert_to_table():
        cur.execute(statement, (i,))
    db.commit()
    db.close()

def get_all_facts():
    db = sqlite3.connect('factstable.db')
    cur = db.cursor()
    statement = 'select fact from facts'
    database_iter = cur.execute(statement)
    facts = [i[0] for i in database_iter]
    return facts
get_all_facts()
#create_table()
#register_fact()
