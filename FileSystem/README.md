# filesystem - Sistemas de Arquivo

Nossos objetos em algum momento precisam ser guardados. Na hora de guardar, podemos escolher
em simplesmente soltar nosso objeto em algum lugar ou temos a opção de escolher um local
para coloca-lo, separando por tipo de material, ou pela frequencia que usamos, ou colocar junto com outros
materiais ou documentos em forma alfabética.

Os objetivos dessa 'arrumação' podem ser:

- Facilidade de localização.
- Melhor distribuição de espaço.
- Agilidade para movimentação.
- Acesso restrito - segurança.
- Diminuição de risco para perdas ou Danos.

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

#### Ext(Ext2, Ext3, Ext4 - Extended file system)

Os sistemas Ext, e toda a sua linha foram criados especificamente para o SO do Linux.
O Ext foi um melhoramento do sistema minix e foi implatado em 1992.

O Ext2, veio com melhorias em seus atributos na questão de espaço suportado, mas nada além disso.

O Ext3 foi o sistema mais usado por padrão no linux. A sua maior modificação é o suporte ao 'Journaling'.
O Ext3, é basicamente o Ext2 com acesso a esse suporte.

Ext4 desde 2010 é usado como padrão do sistema linux. Além de apresentar o recurso 'Journaling', permite maiores volumes
de arquivos com blocos de 4k, e funções novas como a 'extents', 'Multiblock allocation', 'Delayed allocation' entre outras.
Essas novas funções são inovadoras e mudam a forma como trabalha um sistema de arquivos. A função Extents, é responsável por
diminuir a fragmentação do disco, pois quando se trabalha com arquivos muito grandes, ao inves de colocar tudo em blocos
de 4k, ela consegue separar espaços maiores para essa alocação.
O Multiblock allocation é uma melhoria significativa também. Antes, até mesmo no Ext3, os blocos para serem gravados
eram feitos 1 de cada vez. Em arquivos grandes, quando alocavamos blocos de 4k, o alocador poderia ser chamado várias
vezes até terminr um único arquivo. O Multiblock permite que Vários blocos sejam alocados de uma única vez, ganhando em
desempenho e outras questões.
E por fim entre as várias melhorias, o Delayed allocation, sua tradução seria atraso de alocação.
Ao contrário de outros sistemas de arquivo que alocam rapidamente os arquivos em blocos

#### Btrfs (B-tree file System)

O Btrs começou a ser desenvolvido em 2007 e foi dado como estável no ano de 2014, inicialmente desenvolvido pela
Oracle. Foi projetado para ser capaz de lidar não só com armazenamento mas principalmente para conseguir administra-lo
de forma eficiente.
O btr se baseia na função de 'copy-on-write'(cow) e além disso pode suportar os chamados 'snapshots', clonagem de arquivos,
compactação transparente, desfragmentação online e suporte para raid0, 1, 5, 6 e 10.

A chamada função de cópia em gravação (cow) é onde ele mantém a cópia de um bit de dados antes que ele tenha sido escrito,
quando esses dados forem escritos, uma cópia dele será feita. Quando um arquivo é copiado e não modificado eles compartilham
recursos, reduzindo o consumo para cópias não modificadas.
O snapshots é como uma 'restauração do sistema' usado no Linux. Porém existem algumas diferenças porque não é feito um
backup, onde esse guarda em um espaço secundário suas pastas do sistema. No snap são criados em pontos específicos do tempo
um estado de como está o seu sistema e guardado no mesmo dispositivo de armazenamento. A grande vantagem é na economia
do disco e na agilidade pra executar uma reversão, porém passam a ficar vuneráveis a falhas.

#### ZFS (Zettabyte File System)

O zfs é um sistema de arquivo projetado pela Sun Microsystem hoje registrada pela marca Oracle.
O zfs é um sistema de arquivo que está a frente do seu tempo, possui várias funções como o copy-on-write.
Porém, com técnicas inovadoras o principal foco do Zfs é a integridade dos dados, 
onde cada dado tem o valor do seu bloco somado  e gravado no ponteiro do bloco e não no bloco propriamente.

### iOS
#### APFS (Apple File System)

O mais novo sistema de arquivo da Apple. Foi criado para ser trabalhado e compartilhado em diferentes
plataformas (iOS, macOS, tvOS e watchOS). O ultimo sistema de arquivo usado pela Apple era o HFS+ criado em
1998, claro que modificado durante todo esse tempo, mas não preparado para o futuro.

O Apfs nasce suportado por todas as suas plataformas, com foco na segurança, com criptografia e aposta muito na velocidade 
do seu sistema de arquivos, algo inovador do seu sistema é a possibilidade de criação automática de containers quando
o seu disco se encontra cheio. Em comparação com outros sistemas já disponíveis para outros sistemas operacionais
ela se encontra dentro dos padrões e não carrega nada muito inovador.
