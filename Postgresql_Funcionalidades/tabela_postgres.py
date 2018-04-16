import psycopg2


def teste_de_banco():
    conn = psycopg2.connect(host = 'localhost', user = 'pipibdk', database = 'basepipi', password = 'pipizito')
    cur = conn.cursor()
    cur.execute('INSERT INTO nomes (nomes, idade) VALUES (%s, %s)', ('luiz', 20))
    cur.execute('SELECT * FROM nomes')
    cur.fetchall()

    conn.commit()


if __name__ == '__main__':
    teste_de_banco()
