## Python

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

### if, elif, else

Os Termos aqui apresentados é o que chamamos de estruturas condicionais. Os comandos verificam as condições dos argumentos, e executa caso seja verdadeira. Podemos entender o if como uma condição principal e o else como a condição contrária ao if. É comum termos mais de duas condições e caso isso aconteça usamos então o elif até chegarmos no else.

### while

O while é uma estrutura de repetição. Muito parecida com o if, que verifica as condições dos seus argumentos e executa caso seja verdadeiro. A diferença está na quantidade de repetição, pois o if executa a ação uma vez, e o while executará a sua ação enquanto os seus argumentos forem True e so terá a sua repetição interrompida caso sua condição mude.

### for

O for é mais uma condição de repetição do python, junto com o while. Porém, o for é mais usado em casos de interação com listas ou ranges.

            for<argumento> in <lista>:
                .....

Nesse caso temos a condição de repetição que são os elementos da lista, enquanto houver esses elementos o for será executado e será interrompido caso esses elementos termine.

### Listas

Uma lista ou list como é conhecida, e um conjunto de caracteres que podem ser de tipos diferentes. Esses elementos sao colocados dentro de colchetes para formar uma lista.

            ['fellipe', 10, 3,5]

Quando definimos uma lista, estamos ordenando esses valores finitos. Quando definimos uma lista, seus elementos são o que chamamos de mutáveis, pois podem ser excluídos, adicionados e até desordenados. Podemos conter até mesmo listas dentro de listas o que chamamos de 'aninhar'.

### Dicionarios

Os dicionários em python é um tipo de sequência que associa objeto. Dfinida por chaves {} e associada por dois pontos.

            {1 : 'cachorro', 2 : 'gato'}

### Class

Criar uma class, ou objeto classe é compor esse objeto com atributos e métodos. atributos é como são conhecidos as variáveis dentro de uma classee métodos é como são chamadas as funções quando estão dentro de uma classe.

Por convenção, usamos o parâmetro 'self' como obrigatório dentro dos metodos de uma classe.
