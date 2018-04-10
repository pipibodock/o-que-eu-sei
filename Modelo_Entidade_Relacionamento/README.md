# DIAGRAMA DE ENTIDADE E RELACIONAMENTO

Diagrama de Entidade e relacionamento e uma forma grafica de representar os relacionamentos entre as entidades.

Esse Diagrama pode ser usado para a construção de um novo banco de dados ou para a depuração de banco já existentes.                             (design, solução de problemas e pesquisa)

A importância de se fazer um diagrama se da na necessidade que temos de construir um relacionamento sólido e descritivo. Criar um diagrama te possibilita pensar todas as possíveis relações que seu banco de dados pode ter. Diminui as chances de ter que refazer algo posteriormente.

## ENTIDADES

Entidades são representadas no diagrama como forma de retângulo e normalmente descrita por um substantivo.

![alt text](https://github.com/pipibodock/o-que-eu-sei/blob/master/Imagens/1f1183cc7f618d80b61bd57ae81e994b.png)

Entidades pode ser uma entidade sozinha ou podemos dizer em conjuntos de entidades. Essas entidades podem ser classificadas como:.

#### FORTES 

São aquelas que não dependem de outra entidade. Ela existe por si só. Pode possuir um ou mais atributo.

##### FRACAS 

São aquelas que dependem de outras entidades para existir. Ela por sí só em um diagrama não faz sentido.

#### ASSOCIATIVAS 

São aquelas criadas para uma se relacionar no produto de uma entidade com um relacionamento. As entidades associativas, podem ser vistas como vias de mão dupla, onde está ligada tanto a entidade quanto ao relacionamento.


## RELACIONAMENTOS

Relacionamentos é a forma como uma entidade se ‘relaciona’ , ou como estão ligadas, ou como atuam uma com a outra. Podemos representar esses     relacionamentos em um diagrama como uma elipse e descreve-la como um verbo.

![alt text](https://github.com/pipibodock/o-que-eu-sei/blob/master/Imagens/imagens-losango-15.gif)

Relacionamentos podem ter tipos, conhecidos como __cardinalidade__:

#### 1..1 

Necessariamente uma entidade se relaciona diretamente com apenas 1 outra entidade. ex.( cada pessoa só coloca apenas 1 curriculum em um banco de dados de registro. Ou seja existe apenas  1 curriculum para 1 pessoa ou 1 pessoa para 1 curriculum)

#### 1..n  

Temos aqui uma relação de 1 para vários. A entidade Alunos e a entidade veículo. Em uma auto escola, a relação entre os alunos para o veículo é  de 1 para vários.  1 carro é para vários alunos. Vários alunos são para 1 carro de aprendizagem.

#### n..n 

Ligação de vários para vários, existem várias entidades de um mesmo tipo que se relaciona para várias entidades de outro tipo. Como uma          entidade ‘produto’ podem ser vendidos para vários clientes e vários clientes podem comprar vários produtos.

## ATRIBUTOS

Atributos são qualidades, que descrevem a entidade ou um relacionamento. Cada elemento pode ter um atributo ou mais. Normalmente usamos          __ADJETIVO__ para a descrição de um atributo de entidade e __ADVÉRBIOS__ para a descrição de um atributo de relacionamento.

Entidades podem possuir vários atributos, cabe a quem constroe um diagrama decidir quais deles são relevantes para o seu tipo de serviço.        

. ex: Uma pessoa possui cor dos olhos, cor do cabelo e etc, porém esses atributos não são relevantes quando se trata, por exemplo, de registros  
para ser usado em um supermercado. 

Assim, os atributos mais relevantes passariam a ser o seu nome, seu endereço ou o seu cpf.

#### Atributos Descritivos ou Nominativos:

##### Descritivos

São aqueles que descrevem a entidade propriamente dita, como nome e cor.

##### Nominativos 

São os atributos construidos, como números de matŕiculas para uma entidade.

#### Composição - Atributos simples ou compostos:

##### Simples 

Quando a descrição por ela só já é suficiente, por exemplo o nome.

##### composta 

Quando um atributo é composto por outros informações. Por exemplo, o endereço, que se compoe por rua, bairro, número e etc.
