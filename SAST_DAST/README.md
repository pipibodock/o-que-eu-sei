# Resumo sobre o que é SAST e DAST

**SAST** e **DAST** são processos de validação de segurança para softwares.
SAST e DAST significam Static Application Security Testing e Dynamic Application Security Testing respectivamente.

Podemos dizer que o DAST é uma metodologia de caixa preta. Isso significa que o software estando rodando, ele será testado de fora.
Na prática o testador não conhece a aplicação e tentará "Hackea-lo".
Por outro lado, temos o SAST, que é uma metodologia caixa branca, onde se testa a aplicação de dentro para fora.
Nesse contexto, buscamos vunerabilidades que pode estar direto no código fonte da aplicação.

> Importante ressaltar que o SAST não executa o seu código

Nesse contexto, podemos afirmar que os processos se completam.

#### Principais vantagens do SAST:

- Ajuda a encontrar problemas mais cedo, antes da implantação;
- Garante a conformidade com padrões de codificação, sem realmente executar o código;
- Fornece informações detalhadas para a equipe poder corrigir os problemas.

#### Vantagens do DAST:

- Encontra problemas de tempo de execução que não podem ser identificados pela análise estática;
- Identifica mais rapidamente problemas de autenticação e configuração de servidores;
- Lista as falhas que ficam visíveis apenas quando um usuário de fato efetua um login.

# 10 Principais riscos de segurança para uma aplicação WEB (2021)

### A01:2021-Broken Access Control

---

Controle de acesso quebrado. Subiu 5 posições, desde 2017, estando em 2021 na primeira posição.
Aplicativos de várias categorias foram encontrados com esse tipo de vunerabilidade.

Alguns exemplos de quebra de acesso:

- Violação de permissão
- Bypass de modificação da URL
- Acesso a métodos de API não permitidos - como POST, PUT e DELETE
- Configuração de CORS para origins desconhecidos

Como previnir:

- Exceto para recursos públicos, por default, negue.
- Implement apenas um controle de acesso e se possível re-use. Minizando erros de CORS.
- Desative a lista de diretórios do servidor e garanta que arquivos de BackUp não estejam presentes na raiz do projeto
- Seguir os padrões de OAUTH para autenticações de longa duração. Tokens JWT devem ter sempre vida curta para minimizar
  a janela de ataque e após o logout todos os identificadores de sessão devem ser invalidados

### A02:2021-Cryptographic Failures

---

Falha de criptografia. A falha de criptografia é o foco de um problema que pode causar danos mais pontuais, como por exemplo a exploração de dados sensíveis (A08-2021).

Para dados sensíveis como senhas, números de cartão e outras informações, sempre precisamos tomar alguns cuidados:

- Possui alguma informação sendo transmitida em texto não criptografado? O tráfego externo na internet é perigoso.
- Algum protocolo de criptografia antigo ou fraco?
- Chaves fracas são usadas por longos tempos ou existe rotação das chaves de criptografias geradas?
- Uso de funções obsoletas como MD5 ou SHA1 ou ausência de criptografias em locais necessários?

Como previnir:

- Classifique os dados processados e indentifique os que são sensíveis de acordo com as leis de proteção dos dados
- Não armazene dados sensíveis desnecessariamente. Descarte o mais rápido possível ou use sistema de tokens
- Certifique-se de criptografar todos os dados em repouso
- Desative o armazenamento em cache para respostas que contenham dados confidenciais
- Evite funções criptográficas e esquemas de preenchimento obsoletos, como MD5, SHA1, PKCS número 1 v1.5

### A03:2021-Injection

---

Injeção de dados sem nenhum tipo de validação. Algumas das injeções mais comuns são SQL, NoSQL, comandos do Sistema operacional, Object Relational Mapping (ORM) e entre outros. A revisão do código-fonte é o melhor método para detectar se os aplicativos são vulneráveis ​​a injeções.

O teste automatizado de todos os parâmetros, cabeçalhos, URL, cookies, JSON e outros são extremamente necessários. As organizações podem incluir testes estático (SAST), dinâmico (DAST), ferramentas de teste de segurança de aplicativos no pipeline de CI / CD para identificar algumas falhas de injeção introduzidas antes de colocar em produção. Esses são os principais cuidados para se evitar esse tipo de ataque.

A plicação está vulnerável a um ataque quando:

- Os dados fornecidos pelo usuário não são validados, filtrados ou higienizados pelo aplicativo
- Consultas dinâmicas ou chamadas não parametrizadas sem escape ciente do contexto são usadas diretamente no interpretador.

Como previnir:

- Revisão de Códigos e testes automatizados
- Use validação de entrada positiva ou "whitelist" do lado do servidor. Esta não é uma defesa completa, pois muitos aplicativos requerem caracteres especiais, como áreas de texto ou APIs para aplicativos móveis
- Use LIMIT e outros controles SQL em consultas para evitar a divulgação em massa de registros em caso de injeção de SQL

### A04:2021-Insecure Design

---

Falhas de Design e arquitetura. O design inseguro não é a fonte de todas as outras 10 categorias de risco principais. Há uma diferença entre design inseguro e implementação insegura. Nós diferenciamos entre falhas de design e defeitos de implementação por uma razão, eles têm diferentes causas raiz e remediação. Um design seguro ainda pode ter defeitos de implementação que levam a vulnerabilidades que podem ser exploradas. Um design inseguro não pode ser corrigido por uma implementação perfeita, pois, por definição, os controles de segurança necessários nunca foram criados para a defesa contra ataques específicos.

Exemplo de Ataque:

- Uma rede de cinemas permite descontos para reservas de grupos e tem um máximo de quinze participantes antes de exigir um depósito. Os invasores podem modelar esse fluxo e testar se podem reservar seiscentos lugares e todos os cinemas de uma só vez em algumas solicitações, causando uma enorme perda de receita

### A05:2021-Security Misconfiguration

---

Configuração incorreta de segurança.

Principais causas:

- Falta de proteção de segurança apropriada em qualquer parte da pilha de aplicativos ou permissões configuradas incorretamente
- Recursos desnecessários ativados ou instalados
- As contas padrão e suas senhas ainda estão ativadas e inalteradas
- O tratamento de erros revela rastreamentos de pilha ou outras mensagens de erro excessivamente informativas para os usuários
- O software está desatualizado ou vulnerável (A06: 2021 - Componentes Vulneráveis ​​e Desatualizados)

Como previnir:

- Um processo automatizado para verificar a eficácia das configurações e configurações em todos os ambientes
- Envio de diretivas de segurança para clientes, por exemplo, cabeçalhos de segurança
- Uma plataforma mínima sem recursos, componentes, documentação e amostras desnecessários. Remova ou não instale recursos e estruturas não utilizados
- Os ambientes de desenvolvimento, controle de qualidade e produção devem ser todos configurados de forma idêntica, com credenciais diferentes usadas em cada ambiente. Este processo deve ser automatizado para minimizar o esforço necessário para configurar um novo ambiente seguro

### A06:2021-Vulnerable and Outdated Component

---

Componentes vulneráveis ​​e desatualizados.Componentes vulneráveis ​​são um problema conhecido que nós lutamos para testar e avaliar o risco e é a única categoria que não tem nenhuma enumeração de fraqueza comum.

Estará provavelmente vulnerável quando:

- Se você não souber as versões de todos os componentes que usa (tanto do lado do cliente quanto do lado do servidor). Isso inclui componentes que você usa diretamente, bem como dependências aninhadas
- Se o software for vulnerável, sem suporte ou desatualizado. Isso inclui o sistema operacional, servidor web / aplicativo, sistema de gerenciamento de banco de dados (DBMS), aplicativos, APIs e todos os componentes, ambientes de tempo de execução e bibliotecas
- Se os desenvolvedores de software não testarem a compatibilidade de bibliotecas atualizadas, atualizadas ou com patches

Como se previnir:

- Remova dependências não utilizadas, recursos, componentes, arquivos e documentação desnecessários
- Obtenha componentes apenas de fontes oficiais por meio de links seguros. Prefira pacotes assinados para reduzir a chance de incluir um componente malicioso modificado
- Monitore bibliotecas e componentes sem manutenção ou que não criem patches de segurança para versões anteriores. Se o patch não for possível, considere implantar um patch virtual para monitorar, detectar ou proteger contra o problema descoberto

### A07:2021-Identification and Authentication Failure

---

Falhas de identificação e autenticação. A confirmação da identidade do usuário, autenticação e gerenciamento de sessão é fundamental para proteção contra ataques relacionados à autenticação. Pode haver pontos fracos de autenticação se o aplicativo:

- Permite ataques automatizados, como o enchimento de credenciais, em que o invasor tem uma lista de nomes de usuário e senhas válidos
- Permite força bruta ou outros ataques automatizados
- Permite senhas padrão, fracas ou conhecidas, como "Senha1" ou "admin / admin"
- Possui autenticação multifator em falta ou ineficaz
- Expõe o identificador da sessão no URL

Como se previnir:

- Sempre que possível, implemente a autenticação multifator para evitar o enchimento automatizado de credenciais, força bruta e ataques de reutilização de credenciais roubadas
- Não envie ou implante com nenhuma credencial padrão, especialmente para usuários administradores
- Implementar verificações de senhas fracas, como testar senhas novas ou alteradas na lista das 10.000 piores senhas
- Limite ou atrase cada vez mais as tentativas de login malsucedidas, mas tome cuidado para não criar um cenário de negação de serviço. Registre todas as falhas e alerte os administradores quando o enchimento de credenciais, força bruta ou outros ataques forem detectados

### A08:2021-Software and Data Integrity Failure

---

Falhas de software e integridade de dados. As falhas de software e integridade de dados estão relacionadas ao código e à infraestrutura que não protegem contra violações de integridade. Um exemplo disso é quando um aplicativo depende de plug-ins, bibliotecas ou módulos de fontes não confiáveis. Um pipeline de CI / CD inseguro pode apresentar o potencial de acesso não autorizado, código malicioso ou comprometimento do sistema. Por último, muitos aplicativos agora incluem a funcionalidade de atualização automática, em que as atualizações são baixadas sem verificação de integridade suficiente e aplicadas ao aplicativo anteriormente confiável. Os invasores podem potencialmente carregar suas próprias atualizações para serem distribuídas e executadas em todas as instalações. Outro exemplo é onde objetos ou dados são codificados ou serializados em uma estrutura que um invasor pode ver e modificar é vulnerável à desserialização insegura.

Como se previnir:

- Use assinaturas digitais ou mecanismos semelhantes para verificar se o software ou os dados são da fonte esperada e não foram alterados.
- Certifique-se de que seu pipeline de CI / CD tenha segregação, configuração e controle de acesso adequados para garantir a integridade do código que flui através dos processos de construção e implantação

### A09:2021-Security Logging and Monitoring Failure

---

Falhas de registro e monitoramento de segurança. Esta categoria serve para ajudar a detectar, escalar e responder às violações ativas. Sem registro e monitoramento, as violações não podem ser detectadas. Registro, detecção, monitoramento e resposta ativa insuficientes ocorrem a qualquer momento:

- Eventos auditáveis, como logins, logins com falha e transações de alto valor, não são registrados
- Os registros são armazenados apenas localmente

Como Previnir:

- Certifique-se de que os logs sejam gerados em um formato que as soluções de gerenciamento de log possam consumir facilmente
- Certifique-se de que as transações de alto valor tenham uma trilha de auditoria com controles de integridade para evitar adulteração ou exclusão

### A10:2021-Server-Side Request Forgery

---

Falsificação de solicitação do lado do servidor. Acontece sempre que um aplicativo da web está buscando um recurso remoto sem validar a URL fornecida pelo usuário. O SSRF, como é mais conhecido, é uma vulnerabilidade que permite ao atacante realizar requisições através de um servidor vulnerável.
Cuidados:

Network:

- Estabeleça um ciclo de vida com para os FireWall
- Registrar em Log todos os fluxos de rede aceito e bloqueados
- Aplicar políticas de FireWall para negar por padrão

Application:

- Sanitize e valide todos os dados incluídos pelos usuários
- Não envie "Raw response" para os clientes
- Não reduza o SSR por meio de uma lista de negação ou por regex
- Aplique o esquema de URL, porta e destino com uma lista de permissões positiva

> fontes:

https://www.nova8.com.br/2020/07/17/o-que-e-sast-e-dast/

https://owasp.org/www-project-top-ten/
