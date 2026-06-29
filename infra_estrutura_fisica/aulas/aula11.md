# Infraestrutura Física de Redes


# AULA 11 — Dispositivos de Interconexão

**Objetivo da aula:** Conhecer os principais dispositivos ativos de uma infraestrutura de rede, compreender a função de cada um, entender em qual camada do modelo OSI operam e saber identificar o dispositivo correto para cada situação.

---

## 1. Componentes Passivos vs. Componentes Ativos

Ao longo das últimas aulas estudamos os componentes passivos da infraestrutura de rede — cabos, conectores, patch panels, canaletas e racks. São chamados de passivos porque não processam dados: apenas os transportam ou organizam, sem nenhum processamento eletrônico.

Os **componentes ativos** — também chamados de **dispositivos de interconexão** — são equipamentos eletrônicos que processam, encaminham ou gerenciam o tráfego de dados. Eles precisam de energia elétrica para funcionar e tomam decisões sobre o que fazer com cada dado que recebem.

A infraestrutura física que estudamos até aqui é a fundação — os dispositivos ativos são o que dá vida à rede sobre essa fundação.

---

## 2. Hub

### O que é e Como Funciona

O **hub** foi o primeiro dispositivo usado para conectar múltiplos computadores numa rede local Ethernet. Sua função é simples: receber um sinal elétrico por uma porta e replicá-lo imediatamente para **todas as outras portas** — sem nenhuma inteligência sobre para onde o dado deve ir.

Isso significa que se o computador A envia dados para o computador B, todos os outros computadores conectados ao hub também recebem esses dados — e precisam verificar se são o destinatário correto antes de descartar ou processar o pacote.

### Problemas do Hub

Essa abordagem de replicação total gera dois problemas sérios:

**Colisões:** se dois computadores transmitem simultaneamente, os sinais colidem no cabo — ambos os dados são corrompidos e precisam ser retransmitidos. Em redes com muitos dispositivos, as colisões se tornam frequentes e degradam drasticamente o desempenho.

**Falta de privacidade:** como todos recebem todos os dados, qualquer computador na rede pode capturar o tráfego destinado a outros — um problema grave de segurança.

### Relevância Atual

O hub é um dispositivo obsoleto — substituído completamente pelo switch em qualquer instalação moderna. Não deve ser usado em novas instalações. Seu estudo é relevante para compreender a evolução tecnológica e para entender por que o switch representa uma melhoria tão significativa.

> **Camada OSI:** o hub opera na **camada 1 — Física**. Não interpreta endereços — apenas amplifica e replica o sinal elétrico.

---

## 3. Switch

### O que é e Como Funciona

O **switch** é o dispositivo central de qualquer rede local moderna. Assim como o hub, conecta múltiplos dispositivos — mas com uma diferença fundamental: o switch é inteligente.

Quando um dispositivo se conecta ao switch e transmite dados, o switch lê o **endereço MAC** de origem do quadro e registra em qual porta aquele dispositivo está conectado. Isso forma a **tabela MAC** — um mapa de qual endereço MAC está em qual porta.

A partir desse momento, quando chega um quadro destinado a um endereço MAC já registrado, o switch encaminha o quadro **apenas para a porta correta** — e não para todas as portas como o hub faz.

O resultado é uma rede sem colisões, com privacidade entre os dispositivos e com desempenho muito superior ao hub.

> **Camada OSI:** o switch opera na **camada 2 — Enlace de Dados**. Toma decisões baseadas em endereços MAC.

### Switch Não Gerenciável

O switch não gerenciável (*unmanaged*) funciona imediatamente ao ser conectado — sem nenhuma configuração necessária. Liga, conecta os cabos e a rede funciona.

É a escolha correta para instalações simples onde não há necessidade de controle avançado — pequenas empresas, escritórios domésticos, expansões pontuais de rede.

**Limitações:** sem configuração, sem VLANs, sem monitoramento de tráfego, sem controle de portas.

### Switch Gerenciável

O switch gerenciável (*managed*) oferece controle completo sobre seu funcionamento através de uma interface de configuração — acessada por linha de comando (CLI), interface web ou protocolo SNMP.

Recursos típicos de um switch gerenciável:

- **VLANs:** segmentação lógica da rede — dispositivos em VLANs diferentes não se comunicam diretamente, mesmo estando no mesmo switch físico
- **QoS (*Quality of Service*):** priorização de tráfego — garante que chamadas VoIP e videoconferências tenham prioridade sobre downloads
- **Monitoramento de portas:** visualização do tráfego, erros e status de cada porta
- **Segurança de porta:** limitar quais endereços MAC podem se conectar a cada porta
- **STP/RSTP:** prevenção de loops em redes com caminhos redundantes

É a escolha correta para instalações corporativas, ambientes com múltiplas VLANs e qualquer instalação que exija controle e monitoramento.

### PoE — Power over Ethernet

O **PoE** (*Power over Ethernet*) é uma tecnologia que permite transmitir energia elétrica pelo mesmo cabo de par trançado que transporta os dados — eliminando a necessidade de fonte de alimentação separada para dispositivos como câmeras IP, access points e telefones VoIP.

O switch com suporte a PoE injeta energia elétrica nos pares do cabo. O dispositivo receptor (câmera, AP, telefone) extrai essa energia para se alimentar.

**Padrões PoE:**

| Padrão | Potência por porta | Uso típico |
|---|---|---|
| IEEE 802.3af (PoE) | Até 15,4 W | Telefones VoIP, câmeras IP simples |
| IEEE 802.3at (PoE+) | Até 30 W | APs Wi-Fi, câmeras PTZ |
| IEEE 802.3bt (PoE++) | Até 60 W / 100 W | APs Wi-Fi 6, painéis de acesso, TVs |

> **Importante:** apenas par trançado suporta PoE — fibra óptica não conduz energia elétrica.

### Velocidades e Portas

Switches modernos são fabricados com diferentes combinações de portas:

**Portas de cobre RJ-45:** Fast Ethernet (100 Mbps), Gigabit Ethernet (1 Gbps) ou Multi-Gigabit (2,5/5/10 Gbps). A maioria dos switches atuais para redes locais opera em Gigabit.

**Portas SFP e SFP+:** portas para módulos transceptores removíveis — permitem instalar transceptores de fibra óptica ou cobre de alta velocidade. SFP suporta até 1 Gbps; SFP+ suporta até 10 Gbps. São usadas para uplinks — conexão entre switches ou conexão com o roteador.

---

## 4. Roteador

### O que é e Como Funciona

O **roteador** é o dispositivo responsável por interligar **redes diferentes** e determinar o melhor caminho para que os pacotes cheguem ao destino — mesmo atravessando múltiplas redes intermediárias.

Enquanto o switch trabalha com endereços MAC dentro de uma mesma rede local, o roteador trabalha com **endereços IP** e toma decisões de encaminhamento entre redes distintas.

Quando um pacote chega ao roteador, ele lê o endereço IP de destino, consulta sua **tabela de roteamento** e encaminha o pacote pela interface mais adequada — seja para outro roteador no caminho, seja diretamente para o destino.

> **Camada OSI:** o roteador opera na **camada 3 — Rede**. Toma decisões baseadas em endereços IP.

### Roteador Doméstico vs. Roteador Corporativo

**Roteador doméstico:** equipamento compacto que combina múltiplas funções num único dispositivo — roteador, switch de 4 portas, access point Wi-Fi, servidor DHCP, NAT e firewall básico. É o equipamento que a operadora instala na residência do cliente. Simples de configurar, mas com recursos limitados.

**Roteador corporativo:** equipamento dedicado exclusivamente ao roteamento — sem switch embutido, sem Wi-Fi. Projetado para alto volume de tráfego, múltiplas interfaces WAN, protocolos de roteamento dinâmico (OSPF, BGP) e configuração avançada. Em ambientes corporativos, as funções de switch e Wi-Fi ficam em equipamentos separados e especializados.

### Funções Típicas do Roteador Doméstico/SMB

**NAT:** traduz os endereços IP privados da rede interna para o IP público da operadora — permite que todos os dispositivos da rede acessem a internet compartilhando um único IP público.

**DHCP:** atribui automaticamente endereços IP, máscara, gateway e DNS para cada dispositivo que se conecta à rede — elimina a necessidade de configuração manual em cada dispositivo.

**Firewall básico:** bloqueia conexões não solicitadas vindas da internet, protegendo os dispositivos internos de acessos externos não autorizados.

---

## 5. Access Point

### O que é e Como Funciona

O **access point** (AP) é o dispositivo que cria e gerencia a rede Wi-Fi — permitindo que dispositivos sem fio se conectem à rede local cabeada.

O AP recebe dados da rede cabeada pelo cabo de par trançado e os transmite pelo ar via ondas de rádio para os dispositivos wireless. No sentido inverso, recebe os dados transmitidos pelos dispositivos wireless e os encaminha para a rede cabeada.

> **Camada OSI:** o access point opera nas camadas **1 e 2** — converte entre o meio físico cabeado e o meio sem fio, mantendo o endereçamento MAC.

### AP Standalone vs. AP Gerenciado por Controlador

**AP standalone:** configurado individualmente, de forma independente. Adequado para instalações com um ou poucos APs. Cada AP tem sua própria interface de configuração — o que torna a gestão trabalhosa quando há muitos APs.

**AP gerenciado por controlador (*controller-based*):** múltiplos APs são gerenciados centralmente por um controlador — físico (um equipamento dedicado no rack) ou virtual (software num servidor). O controlador configura todos os APs simultaneamente, monitora o tráfego wireless de toda a instalação e permite funcionalidades avançadas como roaming transparente entre APs e balanceamento de carga.

É a escolha correta para instalações com muitos APs — escolas, hospitais, hotéis, empresas com múltiplos andares.

### PoE como Forma de Alimentação

A grande maioria dos access points corporativos é alimentada por **PoE** — recebem energia pelo mesmo cabo Cat6 que transporta os dados. Isso elimina a necessidade de tomada elétrica próxima ao ponto de instalação do AP, que frequentemente fica no teto ou em locais de difícil acesso.

### Posicionamento e Cobertura

O posicionamento correto dos APs é fundamental para garantir cobertura adequada sem interferência entre eles. Fatores que afetam a cobertura:

- **Paredes e obstáculos:** paredes de concreto, vidro metalizado e estruturas metálicas reduzem significativamente o alcance do sinal Wi-Fi
- **Frequência:** 2,4 GHz penetra melhor em obstáculos; 5 GHz oferece mais velocidade mas menor alcance
- **Interferência entre APs:** APs próximos devem operar em canais diferentes para evitar interferência mútua

> O projeto de cobertura Wi-Fi — *site survey*, cálculo de APs necessários e posicionamento — será abordado em disciplinas específicas de redes sem fio.

---

## 6. Firewall

### O que é e Qual sua Função

O **firewall** é o dispositivo de segurança responsável por controlar e filtrar o tráfego entre redes — geralmente entre a rede interna (confiável) e a internet (não confiável).

O firewall analisa cada pacote que tenta atravessar a barreira entre as redes e decide, com base em regras configuradas, se permite ou bloqueia a passagem. Essas regras podem ser baseadas em endereços IP, portas, protocolos, horários e outros critérios.

> **Camada OSI:** firewalls básicos operam nas **camadas 3 e 4**. Firewalls de próxima geração (*NGFW*) inspecionam até a **camada 7**, analisando o conteúdo das aplicações.

### Firewall de Hardware vs. Software

**Firewall de hardware:** appliance dedicado — um equipamento físico instalado no rack, projetado exclusivamente para função de firewall. Oferece alto desempenho, recursos avançados e não compete por recursos com outros sistemas. É a solução para ambientes corporativos.

**Firewall de software:** programa instalado num servidor ou computador. Mais flexível e de menor custo, mas consome recursos do servidor onde está instalado. Exemplos: pfSense, OPNsense (soluções open source amplamente usadas em pequenas e médias empresas).

### Quando é Necessário um Firewall Dedicado

O roteador doméstico inclui um firewall básico — suficiente para uso residencial e pequenas empresas com baixo nível de risco. Para ambientes que exigem:

- Regras de segurança detalhadas e auditáveis
- Inspeção profunda de pacotes (DPI)
- VPN corporativa
- Controle de aplicações e filtragem de conteúdo
- Relatórios de segurança

— um firewall dedicado é necessário.

---

## 7. Modem

### O que é e Qual seu Papel

O **modem** é o dispositivo que conecta a rede local do cliente à infraestrutura da operadora de internet. Faz a conversão entre o sinal da rede local (digital Ethernet) e o sinal usado pela tecnologia de acesso da operadora.

O nome vem de **Mo**dulador/**Dem**odulador — como estudado na aula 02, converte sinais digitais em analógicos e vice-versa. Embora os modems modernos de fibra não façam mais modulação analógica no sentido original, o nome permanece por tradição.

### Tipos de Modem por Tecnologia de Acesso

**Modem DSL (xDSL):** conecta à linha telefônica de cobre da operadora. Tecnologia em declínio, substituída progressivamente pela fibra. Velocidades limitadas pela distância até a central da operadora.

**Modem a cabo (DOCSIS):** conecta ao cabo coaxial da operadora de TV a cabo. Usado por operadoras como Claro/NET. Oferece velocidades altas, mas o meio é compartilhado entre vizinhos.

**ONT/ONU — Optical Network Terminal:** o "modem" de fibra óptica. Converte o sinal óptico da fibra em sinal elétrico Ethernet para a rede do cliente. É o CPE padrão nas instalações FTTH. Tecnicamente não é um modem no sentido original — é um conversor óptico/elétrico — mas cumpre o mesmo papel de interface com a operadora.

### Diferença entre Modem e Roteador

Esta é uma das confusões mais comuns em instalações domésticas e de pequenas empresas:

| | Modem / ONT | Roteador |
|---|---|---|
| Função | Conecta à operadora | Gerencia a rede interna |
| Camada OSI | 1 e 2 | 3 |
| NAT | Não (geralmente) | Sim |
| DHCP interno | Não | Sim |
| Wi-Fi | Não | Sim (em modelos combinados) |

Muitas operadoras fornecem um equipamento combinado — modem + roteador + Wi-Fi num único dispositivo, chamado de **gateway residencial** ou **roteador da operadora**. Em instalações corporativas, o correto é separar as funções: o modem/ONT faz a interface com a operadora, e um roteador dedicado gerencia a rede interna.

---

## 8. Comparativo entre os Dispositivos

| Dispositivo | Camada OSI | Função Principal | Uso Típico |
|---|---|---|---|
| Hub | Camada 1 | Replica sinal para todas as portas | Obsoleto — não usar |
| Switch | Camada 2 | Encaminha quadros por endereço MAC | Rede local — conexão de dispositivos |
| Roteador | Camada 3 | Encaminha pacotes por endereço IP entre redes | Conexão entre redes e internet |
| Access Point | Camadas 1 e 2 | Conecta dispositivos wireless à rede cabeada | Cobertura Wi-Fi |
| Firewall | Camadas 3 a 7 | Filtra e controla tráfego entre redes | Segurança de perímetro |
| Modem / ONT | Camadas 1 e 2 | Interface com a operadora de internet | Ponto de entrada da internet |

---

## Síntese do Bloco 5

Com esta aula, o Bloco 5 — Dispositivos de Interconexão — está concluído. O aluno agora conhece todos os dispositivos ativos que compõem uma infraestrutura de rede local:

- **Hub:** dispositivo obsoleto, substituído pelo switch
- **Switch:** coração da rede local, opera na camada 2, suporta PoE e VLANs nos modelos gerenciáveis
- **Roteador:** interliga redes diferentes, opera na camada 3, inclui NAT e DHCP nos modelos domésticos
- **Access Point:** cria a rede Wi-Fi, alimentado por PoE, gerenciado individualmente ou por controlador
- **Firewall:** controla e filtra o tráfego entre redes, essencial para segurança corporativa
- **Modem / ONT:** interface com a operadora de internet, converte o sinal da tecnologia de acesso para Ethernet
