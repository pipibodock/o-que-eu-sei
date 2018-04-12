# Banco de Dados (Postgresql)

### Tipo de dados (Data Type) Sql server.

#### As categorias dos tipos de dados podem ser:

. número exato                             .  cadeias de caracteres unicode

. númerico aproximado                      . cadeias de caractere binária

. data e hora                              . Outros tipos de dados

. cadeias de caracteres

Assim como em  outras linguagens, precisamos definir que tipo de dado estamos prestes a receber ou guardar naquele campo, no caso do sql, precisamos informar o tipo de dado que vamos receber para formar aquela coluna.

Para cada tipo de dado, podemos ter varias preparações diferentes. Essas preparações vão mudar de acordo com o numero de caracteres que ela possui e consequentemente, o número de espaço que ela  ocupa.

ex(s):

. INT OU INTERGER – Preparação usada para receber números inteiros.

. REAL – Usado para definir e receber número do tipo float. Que não é inteiro.

. DATA – Preparação usada para receber data. Existem outros tipos de datas.

. VACHAR – Preparação para o uso de caracter.

. BOOLEAN – Usada para a informação de verdadeiro ou Falso.

### NOT NULL E AUTO_INCREMENT

Além da preparação dos tipos de informação que vamos receber, podemos usar mais aguns ‘comandos’ para a preparação das nossas informações para melhor organiza-las. Os exemplos mais comuns que temos, são:

. NOT NULL – Especificamos que uma informação é not null, quando dizemos que ela não pode ser ignorada, o que significa que não podemos deixar de preencher essa informação.

. AUTO_INCREMENT(SERIAL) – Nesse comando em sql definimos que um campo vai ser auto incrementado, isso significa que todas as vezes que fizermos uma adição de novo item em nossa tabela ele receberá um numero gerado automaticamente e associado para aquela linha.

### PRIMARY KEY (PK)

Assim que criamos uma tabela em nosso banco de dados, podemos definir uma de suas colunas como a nossa primary key. Isso significa que para cada linha que adicionarmos, um dos seus dados serão únicos, o que impede a sua reincidencia.

###  FOREIGN KEY (FK)

Foreign key, ou chave estrangeira é uma chave que usamos para nos referirmos a primary key de um objeto. Usado em caso de termos duas ou mais tabelas que precisamos relaciona-las de alguma forma.

 Ex. Quando temos uma tabela de clientes, e uma tabelas de produtos, precisamos infomar para qual cliente que o produto foi vendido. Podemos criar uma chave estrangeira na tabela produtos que se relaciona a chave primária da tabela de clientes. Assim, essas informações estarão associadas.

### Principais comandos postgre no terminal

Como o próprio título já nos deixa claro, aqui estão listados os principais comandos usados para acessr o banco de dados, criar o banco, criar tabelas e manusea-las. Todos esses comandos são usados via terminal e estão na sua forma genérica. Isso significa que podem ser combinados de formas diferentes para se ganhar em agilidade e funcionalidade.

. SUDO SU – Usado para acessar o postgres. Assim que instalado, para acessar o banco de dados  via terminal, use esse comando junto com o nome ‘postgres’, e então acesse o ‘psql’.

.CREATE DATABASE – Comando usado para criar o sua base de dados. Normalmente esses comando são usados em letras maiúsculas e acompanhados nesse caso, com o nome do banco em letras minusculas.

. \l – Comando usado para listar quais bancos estão disponíveis para acesso.

. CREATE TABLE – Usamos o ‘create table’ para criarmos as nossas novas tabelas. Juntos desse comando devemos colocar o nome da nossa tabela e todas as informações para montarmos as nossas colunas, o que inclui nesse momento definirmos o ‘data type’ de cada campo.

    	CREATE TABLE nome_tabela ( coluna1 datatype, coluna2 datatype… PRIMARY KEY(coluna1) );

. \d – Comando usado para listar as tabelas existentes.

. INSERT INTO – Usado para manusear tabelas, o insert, como sugere o nome, adiciona novos dados em nossas tabelas já criadas.

    	INSERT INTO nome_tabela (coluna1, coluna2..) VALUES (‘dado1’, ‘dado2’..);

. DELETE FROM – Usado para deletarmos linhas ou valores inseridos em nossas tabelas.

. DROPE TABLE – Comando que usamos para apagarmos as tabelas por inteiro.

. ALTER TABLE – Usado para manusear e modificar os dados de nossas tabelas. Podemos por exemplo, adicionar colunas, mudar o datatype  entre outras modificações.

. SELECT – Usamos o ‘select’ para buscarmos os dados do nosso banco e retorna-las em forma de tabelas construídas.
