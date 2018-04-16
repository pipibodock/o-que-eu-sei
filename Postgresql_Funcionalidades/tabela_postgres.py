import psycopg2


def conecta_database():
    return psycopg2.connect(
        host='localhost',
        user='pipibdk',
        database='basepipi',
        password='pipizito'
    )


def cria_tabela_database():
    conn = conecta_database()
    conn.cursor()
    cria_tabela = 'CREATE TABLE alunos(matricula SERIAL PRIMARY KEY, nome VARCHAR(80), idade INTEGER)' 
    cur.execute(cria_tabela) 
    conn.commit()


def teste_de_banco():
    conn = conecta_database()
    cur = conn.cursor()
    cur.execute('INSERT INTO nomes (nomes, idade) VALUES (%s, %s)', (_insere_dados()))
    cur.execute('SELECT * FROM nomes')
    cur.fetchall()
    conn.commit()

def _insere_dados():
    nome = input('insira nome: ')
    idade = int(input('insira idade: '))
    return nome, idade


if __name__ == '__main__':
    teste_de_banco()
