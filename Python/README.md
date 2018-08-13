## Python

### Porque python?

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

### Estrutura de Seleção

#### if, elif, else

-  O **if** é é estrutura de seleção bem difundida. Com esse termo podemos fazer verificações equivalentes ao `se`, isso
significa que colocaremos condições para o objeto tomar uma certa ação e caso essas condições não sejam verdadeiras
não teremos o comportamento imposto pelo if.

- O **else** é uma condição contrária ao if, em uma estrutura de seleção, caso nenhuma das condições impostas sejam satisfatórias
para o objeto entrar no if, será no else que ele achará a condição geral de como se comportar.

- Além do if e do else, temos também o **elif** que é um else com um if. Isso significa que podemos ter mais de uma seleção,
e quando temos mais uma seleção com comportamentos diferentes usamos o elif  entre os 'ifs' e o 'else'.

---

### Estrutura de Repetição

#### while

O while é uma estrutura de repetição. Muito parecida com o if, que verifica as condições dos seus argumentos e executa caso seja verdadeiro. A diferença está na quantidade de repetição, pois o if executa a ação uma vez, e o while executará a sua ação enquanto os seus argumentos forem True e so terá a sua repetição interrompida caso sua condição mude.

#### for

O for é mais uma condição de repetição do python, junto com o while. Porém, o for é mais usado em casos de interação com listas ou ranges.

            for<argumento> in <lista>:
                .....

Nesse caso temos a condição de repetição que são os elementos da lista, enquanto houver esses elementos o for será executado e será interrompido caso esses elementos termine.

---

### Tipos de Dados

### Str

Em python, uma entrada pode ser feita de algumas formas diferentes. Falando especificamente de Str,
esse que é uma sequencia de caractere, ou menor parcela de um texto.
Usualmente, fazemos uma entrada em formato de str e caso seja conveniente a convertemos para outra forma.

### Int

O int é uma classe usada para converter uma entrada em inteiro. Usamos o seu construtor para isso `int()`.
Lembrando que essa função não arredonda numeros, faz somente a leitura dos dois primeiros algarismos presente.

### Float

O float, também conhecido como ponto flutuante, assim como o int, é uma classe que usa o construtor `float()`
e converte a sua entrada para uma forma decimal ou fracionada.

### Listas

Uma lista ou list como é conhecida, e um conjunto de caracteres que podem ser de tipos diferentes. Esses elementos sao colocados dentro de colchetes para formar uma lista.

            ['fellipe', 10, 3,5]

Quando definimos uma lista, estamos ordenando esses valores finitos. Quando definimos uma lista, seus elementos são o que chamamos de mutáveis, pois podem ser excluídos, adicionados e até desordenados. Podemos conter até mesmo listas dentro de listas o que chamamos de 'aninhar'.

---

### Variaveis

O que chamamos de variáveis, são locais de memória usados para armazenar 'valores'.
Com base nos tipos de dados que estamos trabalhando, esses valores armazenados podem ser números do tipo
Inteiro, decimais ou caracteres.
Não é necessário uma complexa ferramenta na hora de fazer essas atribuições, usamos apenas o sinal de  '=',
que no caso lemos como 'atribuição' ou 'recebe'.

### Func

Func, é como conhecemos as funções em python. Uma função, possui uma 'syntax' definida como:

            def nome_da_função(argumentos):
                .....

Uma função é um bloco de código usado para realizar uma ação, reutilizando esses códigos de forma reduzida.
excluindo a necessidade de reescrever todo o bloco a cada uso.



### Dicionarios

Os dicionários em python é um tipo de sequência que associa objeto. Dfinida por chaves {} e associada por dois pontos.

            {1 : 'cachorro', 2 : 'gato'}

### Class

Criar uma class, ou objeto classe é compor esse objeto com atributos e métodos. atributos é como são conhecidos as variáveis dentro de uma classee métodos é como são chamadas as funções quando estão dentro de uma classe.

Por convenção, usamos o parâmetro 'self' como obrigatório dentro dos metodos de uma classe.
