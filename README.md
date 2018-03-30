# O que eu sei


### Vim

O Vim é um forte editor de texto. Umas das suas maiores vantagens se encontra na sua composição. 
Vários comandos podem ser somados e dar ao desenvolvedor uma extensa lista de combinações.


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
### while
### for
### Listas
### Dicionarios
### Class

## Git e GitHub

### git init
    
Cria um repositório vazio dentro da pasta que você escolher. 
Uma pasta nomeada como `.git`.
Essa pasta que iniciamos o git, nao precisa estar vazia, ela pode conter arquivos ou não.

### areas do git    
    
O git trabalha com o conceito de 3 áreas diferentes. work área, stage área, repository area.
O work área, nada mais é do que a sua pasta local. ou simplismente a sua partição, em que
você realiza todas as mudanças ou criação de arquivo.

A stage área, também chamada de index, podemos entende-la como um container.
Nessa ficam previamente monitoradas as mudanças que fazemos.

A terceira área é a qual o git armazena as suas informações, cada qual com suas tags.

### git .ignore

O git possui essa forma para que possamos inserir arquivos que queremos ignorar.
Fazemos isso para não commitarmos os nossos arquivos por acidente e também por comodidade,
para que os arquivos não fiquem sendo listados o tempo todo como 'untracked'.

### git status

Git status é o comando que usamos para nos orientar.
Nesse comando que nos atualizamos e sabemos de fato, em qual área do git se encontra o nosso arquivo.

### git add

Git add, comando usado para enviar nossos arquivos que foram criados ou modificados para a stage area.
A partir do momento que fazemos esse comando, o git passa a monitora-lo e já se cria um chamado blob.

### git commit

'Commitar' um arquivo, é envia-lo para a nossa área de repositório.

### git log

O git log é o comando responsavel por mostrar os commit's feitos.
Neste comando, vem a descrição de usuário, data e mensagens usadas para descrição do arquivo.

Temos também uma variação do git log, que é chamado de git log oneline.
Este comando organiza os nossos logs em forma de lista, facilitando a visualização.

### git diff

O comando dif, é usado para nos orientarmos das mudanças feitas em cada arquivo.
Somado com o dif, podemos usar outras combinações para as modificações serem apresentadas
de várias formas diferentes.

### git branch

Fazer um git branch é criar uma nova linha de desenvolvimento.
Criar novas linhas de desenvolvimento é relevante, pois projetos podem avançar em diferentes caminhos
e futuramente serem unidos, evitando assim, que o seu código fique parado por muito tempo em um único ponto.
Usar o comando git branch, nos permite também, ver quantos 'branch' temos ali registrados.

### git checkout

Podemos possuir diferentes linhas de deselvovimento, que chamamos de brach. ``Git checkout`` nos permite
fazer a troca desses branch.

### git merge:

O comando merge provavelmente é uma das funções mais importantes dentro do git.
Fazer um merge é atualizar seus commits, juntar as modificações de cada branch
tornando o arquivo um só. Juntando as suas alterações em apenas uma 'tree'.

