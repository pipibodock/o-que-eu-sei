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

### Estruturas de Repetição

#### while

O while é uma estrutura de repetição, o que chamamos de loop, equivalente a "enquanto".
O while é a estrutura que usamos quando buscamos algo para interar sobre uma estrutura de seleção`(if, elif, else)`.
Isso significa que vamos usar o while e o seu laço irá se repetir até que o estado seja alterado ou seja, enquanto
uma afirmação seja equivalente a um `True` teremos uma repetição até que esse estado se altere para um `False`.

#### for

O for é mais uma condição de repetição do python, que chamamos de loop, assim como o while.
Porém, o for é usado em casos de interações, tudo que possui uma range como `strings`, `listas`, `tuplas`,
e outras estruturas que possam  fornecer a sua extensão como "contador" para a repetição.

ex:

    palavra = 'coisa'
    lista = [1, 2, 3, 4, 5]

    for letra in palavra:
        print(letra)


    for numero in lista:
        print(numero)

---

### Estruturas de Dados

### Listas

Uma lista ou list como é conhecida, e um conjunto de dados colocados entre colchetes.
A classe lista do python possui vários métodos para ser usado, que nos permite alterar a lista,
por isso dizemos que é mutável.

ex:

    lista_de_metodos_da_lista = [append(), extend(), insert(), remove(), pop(), clear(), count(), sort(), reverse(), copy()]

Quando definimos uma lista, estamos indexando os seus valores, isso significa que podemos acessar seus elementos
através da sua posição `lista_de_metodos_da_lista[0]` isso seria o mesmo que acessar o método `append()`.

### *Args

### Dicionarios

Os dicionários em python é um tipo de sequência que associa objeto. Dfinida por chaves {} e associada por dois pontos.

    {1 : 'cachorro', 2 : 'gato'}

### *Kwargs

### Tuplas

### Set

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

### Class

Criar uma class, ou objeto classe é compor esse objeto com atributos e métodos. atributos é como são conhecidos as variáveis dentro de uma classee métodos é como são chamadas as funções quando estão dentro de uma classe.

Por convenção, usamos o parâmetro 'self' como obrigatório dentro dos metodos de uma classe.
