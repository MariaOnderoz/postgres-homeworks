"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=1002)


cur = conn.cursor()

customers = 'north_data/customers_data.csv'
employees = 'north_data/employees_data.csv'
orders = 'north_data/orders_data.csv'

with open(customers, 'r', encoding='utf-8') as text:
    reader = csv.reader(text)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

with open(employees, 'r', encoding='utf-8') as text:
    reader = csv.reader(text)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)

with open(orders, 'r', encoding='utf-8') as text:
    reader = csv.reader(text)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

conn.commit()

cur.close()
conn.close()