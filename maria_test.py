import sys
import mariadb

config = {
    'host': '192.168.2.222',
    'user': 'ralf',
    'password': 'Fr@010265',
    'port': 3307
}


try:
    conn = mariadb.connect(**config, database='morannon')
except mariadb.Error as err:
    print(err, file=sys.stderr)
    sys.exit(1)

cur = conn.cursor()

cur.execute("SHOW TABLES")
for (tbl,) in cur.fetchall():  # pre-fetch all data to free up the cursor
    print("\n===", tbl, "===\n")
    cur.execute(f"SELECT * FROM `{tbl}`")
    print([x[0] for x in cur.description])  # print field names (as a list)
    for row in cur:  # using an iterator minimizes the memory used
        print(row)  # print every row in this table (each as a tuple)

# cur.execute("INSERT INTO sample VALUES (?, ?, ?)",
#     (1, "A 'string' with single quotes.", '2020-01-01'))

conn.close()
