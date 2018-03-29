# O que eu sei


## Vim

- Editor de texto Vim e sua manipulação
    


## Python

- Str
    
    Uma string é uma sequencia de caracter, e caracter é a menor parcela de um texto. 
    Em python, todo caracter entra em formato de str. Para escrevermos outras
    informações que não seja em formato de string, devemos 'converte-los' ou especificar
    em que formato queremos que aquela informação seja processada. Para isso usamos algumas
    das funções que o python nos fornece para essa interpretação.

- Int

    Int, ou inteiro é uma das funções usadas por string. Essa função faz com que a informação ou caracter
    seja interpretado como um número, e em formato de inteiro. Lembrando que essa função não arredonda numeros,
    faz somente a leitura do primeiro algarismo presente.

- Float

    O float, também conhecido como ponto flutuante, assim como o int, é uma outra função das strings. 
    Float é o que nos permite visualizar algarismos em sua forma decimal ou em sua forma de frações. 

- Variaveis

    O que chamamos de variáveis, são locais de memória usados para armazenar 'valores'.
    Com base nos tipos de dados que estamos trabalhando, esses valores armazenados podem ser números do tipo Inteiro,
    decimais ou caracteres.
    Não é necessário uma complexa ferramenta na hora de fazer essas atribuições, usamos apenas o sinal de  '=',
    que no caso lemos como 'atribuição' ou 'recebe'.

- Func

    Func, é como conhecemos as funções em python. Uma função, possui uma 'syntax' definida como:
            
            def nome_da_função(argumentos):
                .....
    
    Uma função é um bloco de código usado para realizar uma ação. facilitando suas ações e reutilizando códigos.

- if, elif, else
- while
- for
- Listas
- Dicionarios
- Class

## Git e GitHub

- git init
    
    Cria um repositório vazio dentro da pasta que você escolher. 
    Uma pasta de forma oculta nomeada como .git
    Esta pasta que iniciamos o git, nao precisa estar vazia, ela ja pode conter arquivos ou não.

- areas do git    
    
    O git trabalha com o conceito de 3 áreas diferentes. work área, stage área, repository area.
    O work área, nada mais é do que a sua pasta local. ou simplismente a sua partição, em que
    você realiza todas as mudanças ou criação de arquivo.

    A stage área, também chamada de index, podemos entende-la como um container.
    Nessa ficam previamente monitoradas as mudanças que fazemos.

    A terceira área é a qual o git armazena as suas informações, cada qual com suas tags.

- git .ignore

    O git possui essa forma para que possamos inseir arquivos que queremos ignorar.
    Fazemos isso para não commitarmos os nossos arquivos por acidente e também por comodidade,
    para que os arquivos não fiquem sendo listados o tempo todo como 'untracked'.
- git status

    Git status é o comando que usamos para nos orientar.
    Nesse comando que nos atualizamos e sabemos de fato, em qual área do git se encontra o nosso arquivo.

- git add

    git add, comando usado para enviar nossos arquivos que foram criados ou modificados para a stage area.
    A partir do momento que fazemos esse comando, o git passa a monitora-lo e já se cria um chamado blob.

- git commit

    'commitar' um arquivo, é envia-lo para a nossa área de repositório.

- git log <git log oneline>

    O git log é o comando responsavel por mostrar os commit's feitos.
    Neste comando, vem a descrição de usuário, data e mensagens usadas para descrição do arquivo.
    
    Temos também uma variação do git log, que é chamado de git log oneline.
    Este comando organiza os nossos logs em forma de lista, facilitando a visualização.

- git diff

    O comando dif, é usado para nos orientarmos das mudanças feitas em cada arquivo.
    Usado com variações, para nos atualizarmos dessas mudanças em variadas formas de apresentação.
