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
Os comandos básicos aqui são `git stash` para colocar seus arquivos nessa área  e `git stash list` para 
listar aqueles arquivos que já estão presentes ali. 

Para remover o que colocamos no stash podemos usar o `git stash apply` ou `git stash pop`.
Entretanto, usando o apply uma cópia do nosso arquivo ainda ficará presente dentro do 'esconderijo',
sendo assim, se quisermos apagar completamente de dentro da área do stash devemos então usar o
`git stash drop` para apagar suas modificações da lista do stash.


### Repositórios do Git

Sendo assim, existem duas formas de começarmos a trabalhar com o git, criando nosso repostirório local,
ou clonando um repositório de um local remoto ou até mesmo criar um repositório remoto.
Então ja podemos falar de três comandos do git..

- `git init`

Esse comando cria um repositório local, normalmente usamos esse comando dentro do diretório do
nosso projeto, isso fará com que uma pasta oculta seja criada(`.git`). Ainda não estamos monitorando
nossos arquivos, mas já temos tudo que precisamos para isso.

- `git clone`

Esse é o nosso comando caso a gente queira clonar um repositório.
Clonar um repositório significa que em algum local remoto(locais na internet onde ficam hospedados nossos arquivos)
já existe um projeto criado e guardado, e que você consegue fazer uma cópia desse projeto para também fazer as suas contribuições,
por padrão possuem o nome origin, mas podem ser modificados.

- `git remote`

Esse é o comando que usamos para criar o nosso repositório remoto.
Usamos então o `git remote add (nome) (url)`.
Em nome, por padrão se usa o origin, porém pode ser mudado, mas nada muito longo, para facilitar quando formos fazer
referencia a esse repositório. Em url, colocamos o endereço de hospedagem.

---

Bom, temos um local de trabalho. Por questão de organização, queremos nossa aplicação sempre funcionando
e para podermos fazer nossas alterações com segurança, é comum criarmos um ramo de trabalho, chamado de branch.

### Novos caminhos de trabalho

Temos uma aplicação funcionando, se fizermos nossas alterações na mesma linha de produção podemos bagunçar tudo.
Por isso, o git possui uma solução simples e leve para isso, o `git branch`.
Criar um branch, é criar um novo ponteiro para os nossos commits. Por padrão, temos no git, o branch master, que normalmente
usamos como linha principal de produção, mas isso pode ser desfeito, podemos até mesmo apaga-lo se quisermos, adotando
novos padrões para nosso projeto.

Sendo assim, podemos criar novos branchs, com o comando `git branch (nome do seu branch)` e também podemos apaga-los com
o comando `git branch (nome do branch) -d`.

### Git checkout

Git checkout é um comando complexo no git. Além de possuir vários parâmetros que se adaptam a ele, posui também várias funcionalidades
no contexto do git. Vamos então falar da mais simples de suas ações, podemos usar o git chekout para trocarmos de um branch para outro.
Podemos fazer então `git checkout (nome do branch)` para mudarmos ou podemos simplesmente fazer um `git chekcout (nome do branch) -b`
para criarmos um novo branch e ao mesmo termpo, já mudarmos para ele.

Um exemplo das várias funcionalidades do checkout, é que podemos estar fazendo alguma alteração em nossos arquivos, e se simplesmente
desistirmos dessas mudanças, não precisamos sair apagando linha por linha, podemos fazer um `git checkout (nome do arquivo)` e ele
irá desfazer as nossas últimas modificações, de arquivos que ainda estejam em nossa work área.

### Revisando alterações

O git além de versionar seus projetos, é capaz de lhe apresentar quais foram as mudanças feitas em
cada arquivo. Existem algumas formas de apresentação dessas mudanças, mas a mais comum é o
`git diff`. O git diff mostra as linhas que foram adicionadas e as linhas que foram removidas, porém,
um simples git diff só funciona se seu arquivo ainda estiver na work área. Após passar um arquivo
para a sua index área, só é possivel ver essas mudanças usando o comando `git diff --cached`.


### Arquivos feitos e modificados

Normalmente ao terminarmos nossas alterações feitas em conjunto ou não, enviamos para algum repositório remoto,
onde queremos guardar a última versão do nosso arquivo para não correr o risco de perde-lo.
Sendo assim, podemos usar o nosso `git push` para levarmos essas alterações. Porém devemos especificar para aonde vamos enviar
essas mudanças, então usamos `git push (nome do repositório) (branch)`

---

Após todas as modificações feitas e enviadas a um repositório, é comum atualizarmos o nosso repositório local,
que vai conter todas as novas modificações que nós mesmos fazemos, mas também a que outras pessoas fizeram.
Vamos trazer as alterações e juntar com o nosso local de trabalho.

### Atualizando nosso repositório local

Existem algumas formas diferentes de atualizarmos o nosso repositório, algumas delas são...

- `git fetch`

Assim que enviamos as nossas alterações e as enviamos para um local remoto, queremos as modificações que outras pessoas fizeram
também funcionando na nossa aplicação local.

Portanto, podemos fazer um `git fetch`. Git fetch literalmente traz o que há de diferente entre o repositório
remoto e o local e aplica essas diferenças. Caso estejamos em uma equipe grande, é interessante fazermos algo mais completo,
como o `git fetch --all` que busca as atualizações de todos os branch remotos que estão trabalhando no mesmo projeto que nós.

Mas o git fetch tem uma particularidade, ele puxa tudo o que há de novo, porém, não faz o merge(junta).

- `git merge`

Quando abrimos um branch, diferente da nossa linha principal de produção, ao concluirmos e testarmos, queremos 'juntar' o que há de
novo com a linha principal, para isso usamos o `git merge`.
O merge, é o comando usado para atrelar as mudanças feitas com o nosso projeto principal, gerando assim,
uma nova versão do nosso arquivo, o antigo implementado com as novas alterações.

Ao usarmos o git fetch e trazermos o que há de novo do remoto, precisamos 'juntar' com o que já temos em nosso repositório local,
então, também nesses casos fazemos um git merge.

- `git pull`

O git pull, é um comando mais completo. Ele é um `git fetch` + `git merge`. Ou seja, ele traz todas as atualizações do nosso origin, e
já faz também o merge.

---

### git log

### git ignore

### git reset

### git rebase

### git reflog

### git cherry-pick
