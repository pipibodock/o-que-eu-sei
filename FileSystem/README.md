# filesystem - Sistemas de Arquivo

Nossos objetos em algum momento precisam ser guardados. Na hora de guardar, podemos escolher
em simplesmente soltar nosso objeto em algum lugar ou temos a opção de escolher um local
para coloca-lo, separando por tipo de material, ou pela frequencia que usamos, ou colocar junto com outros
materiais ou documentos em forma alfabética.

Os objetivos dessa 'arrumação' podem ser:

. Facilidade de localização.
. Melhor distribuição de espaço.
. Agilidade para movimentação.
. Acesso restrito - segurança.
. Diminuição de risco para perdas ou Danos.

Além de outros, que variam de caso para caso.

Portanto, assim como precisamos nos manter organizados fora dos computadores, como esses ja fazem parte do nosso
dia a dia, Dentro deles não podia ser diferente.

## O que é um sistema de arquivo?

Um sistema de arquivo(FileSystem ou File System) é um software usado pelo sistema operacional
para gerenciar nossos dados, guarda-los e recupera-los da forma mais eficiente possível.
Sem o sistema de arquivo nossos dados, chamados de arquivos seriam uma coisa só. Não saberiamos
onde esses arquivos começam ou terminam.

Falamos em filesystem, e talvez pensamos só em computadores, mas os objetos mais simples usados
para armazenar dados, possuem sistema de arquivo, como é o caso do cd por exemplo, que usa o sistema 
ISO 9660.

Existem vários sistemas diferentes, cada um possui os seus pontos fortes e fracos.
Para cada tipo de trabalho se usa ou se aconselha um sistema diferente.
Para cada sistema operacional, suas opções serão diferentes.

## Estrutura

O file system basicamente possui uma estrutura lógica, que é usada com a 'interface' usada pelo
sistema operacional, que nos permite abrir, alterar, fechar, mover e entre outras coisas.

Existe tambem, a camada chamada como sistema de arquivo físico, é a parte de interação com a memória em sí.
Usada para o processamento dos blocos para alocação dos dados, o canal que será usado para o armazenamento e entre outros.

## Principais sistemas:
### Windows:

#### Fat16(file alocation table)

A 'família' Fat é um dos poucos sistemas de arquivos que podem reconhecidos por vários sistemas operacionais.
Por esse motivo e outros que ainda pode ser visto em dispositivos mais simples, como cartões de memória e outros.
É o sistema de arquivos mais antigo do windows, usado pelo DOS e pelo win95.

A menor parte física de um HD, chamamos de setor. Um conjunto de setores chamamos de Cluster.
O sistema Fat usa os cluster, para 'endereçar' seus arquivos, como forma de encontra-los.
Mas, como seu próprio nome sugere, ele trabalha com 16 bits, que podem ser no máximo 65536 clusters,
que não podem ser maiores que 32KB. Dando a esse sistema uma limitação de 2GB por partição.

ex. Em uma partição de 2GB, cada cluster possui 32KB. Imagine 10 mil arquivos com apenas 300 bytes.
Como cada cluster so pode ser ocupado por um arquivo, ocupariamos aí, 32KB para cada arquivo, um total de 320MB.

#### Fat32

O fat32 foi uma evolução do fat16. Seu endereçamento agora passa a ser feita com 32 bits, possiblitando
ter partições de até 2 terabytes. A sua principal evolução está no tamanho dos seus clusters, que passaram
a ter tamanhos de 4KB.

Ou seja, no fat32 temos cluster menores, que diminuem o desperdício de espaço, mas como temos que particionar
o arquivo em vários cluster diferentes(dependendo do tamanho do arquivo), acaba se perdendendo em desempenho.
Além da queda de desempenho, a fat32 vem com outro problema que é a incapacidade de armazenar arquivos com mais de 4GB.

Outro ponto para se levar em consideração, é a questão da segurança, qualquer um poderia ler, mover e apagar
seus arquivos, pois o sistema aqui em questão não trata desse ponto.

#### NTFS(New Type File System)

Em comparação com a 'família' fat, o sistema de arquivo NTFS veio com grandes avanços.
O sistema NTFS inclui agora a preocupação com a segurança.

Permite o controle de acesso aos dados. Permite a criação de usuários, que com suas senhas
podem proteger seus dados que não aparecem e não ficam disponíveis para outros perfis. Inclui também a criptografia
dos arquivos.

O sistema ja vem incluído a compactação dos arquivos, que não são compatíveis com formato zip,
uma compactação que na hora da abertura do arquivo é desfeita, e que não impacta tanto no desempenho.

Mas o principal avanço do sistema NTFS pode se dizer que foi o recurso 'Journaling'. Esse recurso funciona como um registro,
como um log de todas as alterações feitas, antes de serem propriamente modificadas. Isso resulta em uma recuperação caso
haja um erro de gravação ou um problema de conexão.

#### ReFS(Resilient File System)

Novo sistema de arquivo criado para o windows, com a chegada do Win8.
O Refs, vem carregando algumas melhorias, mas muito criticadas, pois devido ao tempo sem melhorias, comparado
com o sistema NTFS o Refs ainda fica atras com comparação de sistema de arquivos como o da oracle, criado em 2004 o ZFS.

Mas as principais mudanças e as que mais chamam a atenção é a grande compatibilidade com o NTFS, verificação de 
correção automática de erros, foco em aplicação em alta escala, melhor suporte a criptografia e outros.

### unix:
