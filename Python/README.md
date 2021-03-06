## Python

### Porque Python?

Escolhi python como minha primeira linguagem de programação, porque é simples de escrever como PHP, porém mais versátil, e
também nos da acesso a questões complexas que estão presentes em outras linguagens como C++, de uma forma mais acessível.
Python é uma linguagem de alto nível, o que significa estar mais próximo de uma linguagem humana, facilitando o aprendizado,
e me permitiria o contato com a programação mais rápido, contato esse necessário, para dicidir se eu teria gosto pela
programação; E sim, gosto muito disso.

---

### O que é Python?

Python é uma linguagem de programação multi paradigma, significa que ela suporta os paradigmas de **orientação a objeto**,
**imperativo**, **funcional** e **procedural**. Além disso, uma das suas principais características é permitir o fácil acesso
a leitura do código, por isso também falamos que python é uma linguagem de alto nível.

É uma linguagem que pode ser usada para aplicações Desktop, Web e mobile. As contruções do python incluem estruturas de seleções,
estruturas de repetições e contruções de classes.

---

### Estruturas de Seleção

#### if, elif, else

-  O **if** é é estrutura de seleção bem difundida. Com esse termo podemos fazer verificações equivalentes ao `se`, isso
significa que colocaremos condições para o objeto tomar uma certa ação e caso essas condições não sejam verdadeiras
não teremos o comportamento imposto pelo if.

- O **else** é uma condição contrária ao if, em uma estrutura de seleção, caso nenhuma das condições impostas sejam satisfatórias
para o objeto entrar no if, será no else que ele achará a condição geral de como se comportar.

- Além do if e do else, temos também o **elif** que é um else com um if. Isso significa que podemos ter mais de uma seleção,
e quando temos mais uma seleção com comportamentos diferentes usamos o elif  entre os 'ifs' e o 'else'.

---

### With

O `with` é um tratamento que pode ser usado para fechar uma execução, assim quando fazemos:

    with open("arquivo.txt", "w") as arquivo:
        ...

não precisamos dizer a execução para que ele abra o arquivo e depois de toda a execução do bloco ele se feche,
porque isto já se encontra implicito no tratamento `with`.


Porém, ainda mais importante do que garantir esse fechamento com o método `close()` 'encapsulado' dentro do método
há uma outra grande relevancia para se usar o `with`, que se assim podemos dizer, é *garantir a execução do bloco de código*.

Quando dizemos "garantir a execução de código" estamos falando que de alguma forma, o nosso bloco de execução começara
a ser executado, e caso encontre algum erro ou algum motivo para que a execução não seja efetuada do início ao fim, teremos
a interrupção do bloco, de forma completa, sem prejuízo aos objetos do início. Essa 'alguma forma' que garante essa
execução que estamos falando, na verdade são os métodos `__enter__()` e `__exit__()`.

Em uma operação usando banco de dados por exemplo, ou citando uma transação bancária como exemplo, a nossa execução deve
ser bem sucedida do início ao fim, caso isso não aconteça, devemos ter uma interrupção sem nenhum prejuízo ou efeito colateral.
O método `__enter__()` garante que possamos começar toda essa execução e o método `__exit__(self, exc_type, exc_value, traceback)`
recebe 2 parámetros que capturam qualquer tipo de `exception`, se esses parâmetros forem diferente de **None** interrompem
o bloco de execução.

---

### Estruturas de Repetição

#### while

O while é uma estrutura de repetição, o que chamamos de loop, equivalente a "enquanto".
O while é a estrutura que usamos quando buscamos algo para interar sobre uma estrutura de seleção`(if, elif, else)`.
Isso significa que vamos usar o while e o seu laço irá se repetir até que o estado seja alterado ou seja, enquanto
uma afirmação seja equivalente a um `True` teremos uma repetição até que esse estado se altere para um `False`.

#### for

O for é mais uma condição de repetição do python, que chamamos de loop,
assim como o while.
Porém, o for é usado em casos de interações, tudo que possui uma range,
ou que possua o elemento `iterável`, como `strings`, `listas`, `tuplas`,
e outras estruturas que possam  fornecer a sua extensão como "contador" para a
repetição.

ex:

    palavra = 'coisa'
    lista = [1, 2, 3, 4, 5]

    for letra in palavra:
        print(letra)


    for numero in lista:
        print(numero)

---

### Estruturas de Dados

### Tuplas

Tuplas em python são sequências de valores separados por vírgula. Podendo ser
definida entre parênteses ou não. As tuplas podem ser aninhadas:

    tupla = ((1, 2, 3), (3, 2, 1))

O maior ponto a se destacar em uma tupla é que ela é imutável. Não conseguimos usar
métodos para adicionar ou remover itens no nosso objeto.

### Listas

Uma lista ou list como é conhecida, e um conjunto de dados colocados entre colchetes.
A classe lista do python possui vários métodos para ser usado, que nos permite alterar a lista,
por isso dizemos que é mutável.

ex:

    lista_de_metodos_da_lista = [append(), extend(), insert(), remove(), pop(), clear(), count(), sort(), reverse(), copy()]

Quando definimos uma lista, estamos indexando os seus valores, isso significa que podemos acessar seus elementos
através da sua posição `lista_de_metodos_da_lista[0]` isso seria o mesmo que acessar o método `append()`.

### Dicionarios

O dicionário do python é outra estrutura de dado diferente na forma como é
indexado. O dict, é uma estrutura indexada com `keys(chaves)`, que podem ser
do tipo `int` ou `string`, o que nos deixa livres para escolhermos como acessar
os nossos videos.
No dic, temos o que chamamos de **key: value** definido entre **{}**.

    {'nome': 'fellipe', 'idade': 29}
    {1 : 'cachorro', 2 : 'gato'}

### *Args

Em python podemos usar uma estrutura chamada `*args`, que para início de tudo,
não precisa se chamar args. Mas como assim? Significa que essa estrutura poderia
se chamar `*coisa` ou `*aquilo` o importante é não faltar o `*`.
Porque usamos args? O Args é útil quando precisamos passar argumentos,
para uma função por exemplo, mas não sabemos quantos são ou quais são.

ex:

    def soma_coisas(*args):
        bolso = 0
        for arg in args:
            bolso += arg
        return bolso

Essa função é um exemplo onde poderiamos passar vários argumentos que ela ainda
aceitará.

### **Kwargs

Em python também possuímos a estrutura conhecida como `kwargs`, mas assim como
o nome **args**, **kwargs** não passa de uma convenção. Poderíamos chama-lo de
qualquer nome, desde que não falte os `**` para defini-lo.

Usamos o kwargs em situações em que desconhecemos a quantidade de
**argumentos nomeados** que teremos de interagir.

---

## Tipos de Dados

### String(str)

Em python, uma entrada pode ser feita de algumas formas diferentes. Falando especificamente de uma string,
esse que é uma sequência de caractere, ou menor parcela de um texto.
Usualmente, fazemos uma entrada em formato de str e caso seja conveniente a convertemos para outra forma.

### Inteiro(int)

O int é uma classe usada para converter uma entrada em inteiro. Usamos o seu construtor para isso `int()`.
Lembrando que essa função não arredonda numeros, faz somente a leitura dos dois primeiros algarismos presente.

### Float

O float, também conhecido como ponto flutuante, assim como o int, é uma classe que usa o construtor `float()`
e converte a sua entrada para uma forma decimal ou fracionada.

### Variaveis

O que chamamos de variáveis, são locais de memória usados para armazenar 'valores'.
Com base nos tipos de dados que estamos trabalhando, esses valores armazenados podem ser números do tipo
Inteiro, decimais ou caracteres.
Não é necessário uma complexa ferramenta na hora de fazer essas atribuições, usamos apenas o sinal de  '=',
que no caso lemos como 'atribuição' ou 'recebe'.

---

### Func

Func, é como conhecemos as funções em python. Uma função, possui uma 'syntax' definida como:

            def nome_da_função(argumentos):
                .....

Uma função é um bloco de código usado para realizar uma ação, reutilizando esses códigos de forma reduzida.
excluindo a necessidade de reescrever todo o bloco a cada uso.

---

### Class

Criar uma class, ou objeto classe é compor esse objeto com atributos e métodos. atributos é como são conhecidos as variáveis dentro de uma classee métodos é como são chamadas as funções quando estão dentro de uma classe.

Por convenção, usamos o parâmetro 'self' como obrigatório dentro dos metodos de uma classe.

---

### Módulo de requests do Python

Como evidenciamos no título, o python possui um módulo que importamos com `import requests` que usamos
para fazer requisições e instanciar o objeto response. Esse módulo presente no python é de fácil acesso,
descomplicado na hora de fazermos as nossas requisições, e aceita parâmetros de diferentes maneiras para
atingirmos o nosso objetivo.

Alguns métodos usados pelo HTTP, são eles o `put`, `delete`, `head`, `options` e os mais comuns `GET` e `POST`.
As requisições feitas pelo módulo requests, são simples, deixando claro como queremos fazer a nossa requisição:

    response =  resquests.get('http://urlsquequeremos.com')

Geralmente queremos mandar informações nas query strings de nossas url's, dessa forma, podemos usar um *dicionário*
e passa-lo para o argumento `params`:

    dicionario = {'agr1': 'coisa', 'arg2': 'boa'}
    response = requests.get('http://urlquequeremos.com', params=dicionario)

Além do argumento `params` outos argumentos são usados pelo módulo requests, que facilitam o nosso trabalho,
alguns deles são:

**data:**

Passamos um dicionário para o parâmetro data quando queremos criar algum dado em forma de formulário, como fazemos
no HTML. Usando esse parâmetro, os nossos dados colocados no dicionário já tomam a forma necessária para a requisição.

**files:**

Podemos usar o parâmetro `files` quando queremos enviar em nossas requisições algum objeto Multipart, podemos
nomear esses arquivos ou também podemos passar em forma de string para que seja enviada em forma de arquivo.
Tudo isso com grande facilidade.

**cookies:**

Através do parâmetro `cookies`, podemos passar os nossos próprios cookies para os servidores.

Além de passarmos diferentes informações em nossas requisições, muitas vezes precisamos conferir qual tipo de informação
que nos foi retornada. O objeto *Response* possui atributos com fácil acesso:

    response = requests.get('http://algumaurldesejada.com')
    response.url
    response.text
    response.encoding
    response.content

Chegamos a conclusão que o módulo requests é uma biblioteca do python eficiente que atende as nossas demandas.
Fontee e informações completas: [Requests](https://media.readthedocs.org/pdf/requests-docs-pt/latest/requests-docs-pt.pdf)
