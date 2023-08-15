import psycopg2
try:
    conn = psycopg2.connect(database = "pimdreyvami",
                        host = "127.0.0.1",
                        user = "pimdreyvami",
                        password = "",
                        port = "5431",)
    conn.autocommit = True

    cur = conn.cursor()
    cur.execute("INSERT INTO penguin (name,age,color) VALUES ('Vami',3,'pink')")
    conn.commit
    cur.execute("SELECT * FROM penguin")
    penguin_data = cur.fetchall()
    for i in penguin_data :
        print(i)


    cur.close()
except  psycopg2.DatabaseError as error:
    print(error)
finally:
    conn.close

