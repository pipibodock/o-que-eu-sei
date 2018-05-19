# Git

O git é um sistema de controle de versão. É uma ferramenta essencial para quem quer
trabalhar em um projeto junto com outras pessoas, várias pessoas alterando os mesmos
dados e sem nenhum tipo de conflito, sendo capaz de recuperar tudo e qualquer coisa a 
qualquer momento. Isso é o Git.

Normalmente quando estudamos o git, é comum apenas pensarmos em 'decorar' os seus principais
comando e o que eles fazem. Não que isso seja errado, mas com certeza em algum momento
teremos que voltar para entender como funciona de fato e o que está por trás de cada comando.
Sendo assim, talvez a melhor forma de fazer para entender o git, seja o caminho inverso, 
antes de mais nada deveriamos entender o que é o git, como ele trabalha, e tentar entender o seu 
'workflow', para então como consequência entendermos os seus principais comandos.

### Repositórios do Git

Sendo assim, existem duas formas de começarmos a trabalhar com o git, criando nosso repostirório local,
ou clonando um repositório de um local remoto. Então ja podemos falar de dois comandos do git..

- `git init`

Esse comando cria um repositório local, normalmente usamos esse comando dentro do diretório do
nosso projeto, isso fará com que uma pasta oculta seja criada(`.git`). Ainda não estamos monitorando
nossos arquivos, mas já temos tudo que precisamos para isso.

- `git clone`

Esse é o nosso comando caso a gente queira clonar um repositório.
Clonar um repositório significa que em algum local remoto(github, gitlab..) já existe um projeto
criado e guardado, e que você consegue fazer uma cópia desse projeto para também fazer as suas contribuições.

### As 'áreas' do Git

Para começarmos a entender o git, algo que é indispensável, é entender o seu fluxo de trabalho.
Esse fluxo passa por diferentes espaços, até chegarmos ao ponto de estar com as últimas alterações salvas.
Acompanhar em que área o nosso arquivo está é simples, usamos apenas mais um comando, o `git status`.
Quando não estamos trabalhando em nada, as áreas do nosso git estão limpas e alinhadas, sem nenhuma alteração.

- Work área

Essa área, conhecida como área de trabalho, é o espaço das nossas máquinas. Após termos criado ou clonado
um repositório do git, qualquer alteração que fizermos já vai estar aparecendo na nossa work área. 
Aqui estamos monitorando essas mudanças, porém nada além disso.
Após alterarmos algo, se usarmos o nosso `git status`, poderemos ver uma mensagem dizendo que uma alteração foi feita,
mas que elas não estão preparadas.

- Index área

A nossa index área é aonde praparamos para salvar uma nova versão daquilo que consta aqui nesse espaço.
Se nossos arquivos estão presentes nesse local, é porque usamos o comando `git add`, e temos a intenção
de levar esse arquivo para um local seguro.

- Repositório local - HEAD

O nosso repositório local, que pode ser apontado como HEAD, é aonde colocamos em segurança os arquivos
que queremos como uma nova versão. Se algo funciona bem e não temos a intenção de perder os nossos trabalhos,
usamos o comando `git commit`, que temos uma nova versão do nosso produto ou código. Assim, podemos continuar
a trabalhar, sem correr o risco de alterar algo que já funciona.

- Git stash

O git stash é mais uma das áreas do git, podendo ser traduzida ao pé da letra como esconderijo.
Esse espaço do git, não entra no fluxo 'normal' do trabalho, mas também pode ser usado, caso estejamos trabalhando
em algum arquivo e apareça a necessidade de mudar o foco do trabalho, não é necessário fazer um commit de algo
que esteja incompleto, podemos levar um arquivo que já esteja na index área e retornarmos a ele depois.
Os comandos básicos aqui são `git stash` e `git stash list`.

### Revisando alterações

O git além de versionar seus projetos, é capaz de lhe apresentar quais foram as mudanças feitas em
cada arquivo. Existem algumas formas de apresentação dessas mudanças, mas a mais comum é o
`git diff`. O git diff mostra as linhas que foram adicionadas e as linhas que foram removidas, porém,
um simples git diff só funciona se seu arquivo ainda estiver na work área. Após passar um arquivo
para a sua index área, só é possivel ver essas mudanças usando o comando `git diff --cached`.

### git branch

### git checkout

### git push

### git pull

### git fetch

### git merge

### git log

### git ignore

### git reset

### git rebase
