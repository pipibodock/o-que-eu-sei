# Análise de complexidade

Alguns recursos que demandamos em computação são, processamento, que é superficilamente falando,
a capacidade de realizar calculos, e o segundo a capacidade de armazenamento, a memória do computador.
- complexidade é uma medida de recursos que são demandos por um algorítimo.
- Para calcular complexidade usamos operações que parecem pouco detalhadas(operações elementares),
pois o nosso interesse não é o número exato, mas sim, entender como o algoritimo varia de acordo com o
número de entradas.

Quando falamos em análise de complexidade, queremos inferir a demanda desses recursos,
**complexidade de Tempo** *T(n)* e **complexidade de espaço** *S(n)* sobre os nossos algorítimos.
Importante que fique claro, que sempre aos nos referirmos em complexidade, se não formos específicos
de qual complexidade estamos falando, fica-se subentendido que falamos de complexidade de tempo.

Importante ressaltar que quando falamos em complexidade, não levamos em consideração a linguagem
de programação que esse algorítimo foi escrito e nem a quantidade de recursos que possímos em uma
máquina, isso porque, o que avaliamos em uma análise de complexidade é o comportamento elementar.
Isso quer dizer que, se eu executo um algorítimo de entrada igual a N, em uma máquina esse algorítimo
pode levar 2 segundos e em outra, ja pode levar 4 segundos. Mas se dobrarmos o número de entradas,
os tempos de execução também dobraram para 4 e 8. Então o que avaliamos é o comportamento do algorítimo.

Notaçãoes assintóticas:
- big O
- big omega
- Teta
- o pequeno
- omega pequeno

Notação BigO:
A notação BigO é um conjunto de funções, que são dominadas pelo termo de grau N.
A idéia de uma notação bigO é descrever um comportamento geral, quando os nossos dados crescem
e tendem ao infinito(comportamento também chamado de assintótico)
Quanto mais crescer a quantidade de operações necessárias para processar os itens, pior é
o desempenho do algorítimo(pois se executa mais intruções, demora mais, é mais complexo).


# Melhor Caso e Pior Caso

Melhor caso e Pior caso são análises com pontos de vistas diferentes. Fazemos uma análise
levando em consideração melhor e pior caso, quando queremos avaliar a **qualidade** de nossas entradas.
Essa análise de qualidade, nos remete a como os dados se pré-dispõe, diferente de uma análise de quantidade.

Podemos ter como exemplo, um banco de dados e seu processo pg-stat, que constantemente faz uma busca por melhor
ou pior caso, quando necessário fazer suas consultas em discos.
