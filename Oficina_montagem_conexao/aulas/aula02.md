# 📘 **AULA 02 — FONTE DE ALIMENTAÇÃO (PSU) E QUALIDADE DE ENERGIA**

---

## 🔹 **1. Definição de Fonte de Alimentação**

A fonte de alimentação, também chamada de **PSU (Power Supply Unit)**, é o componente responsável por fornecer energia elétrica ao computador.

> **Definição:** dispositivo que converte e distribui energia elétrica adequada para o funcionamento dos componentes.

Sem a fonte:

* O computador não liga
* Os componentes não recebem energia
* O sistema não funciona

---

## 🔹 **2. Funções Principais da Fonte**

A fonte desempenha três funções essenciais:

### 🔌 **1. Conversão de energia**

* Converte corrente alternada (**AC**) da rede elétrica
* Em corrente contínua (**DC**) utilizada pelo computador

---

### 🔻 **2. Redução de tensão**

* Entrada: 127V ou 220V
* Saídas:

  * 12V
  * 5V
  * 3,3V

---

### 🔀 **3. Distribuição de energia**

* Fornece energia para:

  * Placa-mãe
  * Processador
  * Armazenamento
  * Placa de vídeo

---

## 🔹 **3. Tensões Padrão da Fonte**

### ⚡ **12V**

* Componentes de maior consumo
* Ex: CPU e GPU

### ⚡ **5V**

* Dispositivos intermediários
* Ex: USB

### ⚡ **3,3V**

* Circuitos sensíveis
* Ex: chipsets

---

## 🔹 **4. Estrutura Geral da Fonte (Visão Simplificada)**

A fonte é composta por três partes:

### 🔌 Entrada

* Recebe energia da rede (AC)

### ⚙️ Circuito interno

* Converte AC → DC
* Regula tensões

### 🔗 Saídas

* Cabos que alimentam os componentes

---

## 🔹 **5. Tipos de Fontes de Alimentação**

### 🖥️ **a) Quanto ao padrão físico**

* **ATX** → padrão mais comum
* **SFX** → formato compacto

---

### 🔧 **b) Quanto à modularidade**

* **Não modular** → cabos fixos
* **Semi-modular** → parcialmente removíveis
* **Modular** → cabos totalmente removíveis

---

## 🔹 **6. Conectores da Fonte**

### 🔌 **ATX 24 pinos**

* Alimenta a placa-mãe

### 🔌 **CPU (4/8 pinos)**

* Alimenta o processador

### 🔌 **SATA**

* Alimenta HDs e SSDs

### 🔌 **PCIe**

* Alimenta placas de vídeo

---

## 🔹 **7. Potência da Fonte**

A potência indica a capacidade máxima de fornecimento de energia.

> **Unidade:** Watt (W)

### 🔧 Exemplos:

* 400W
* 500W
* 600W

### 💡 Interpretação:

* Sistemas simples → menor potência
* Sistemas mais exigentes → maior potência

> A fonte não deve operar no limite máximo constantemente, sendo recomendada uma margem de segurança.

---

## 🔹 **8. Eficiência Energética**

A eficiência indica o quanto da energia é aproveitada.

* Parte da energia é perdida em forma de calor
* Quanto maior a eficiência, menor o desperdício

### 🏷️ **Selo 80 Plus**

Classificações:

* Bronze
* Silver
* Gold

👉 Maior nível = maior eficiência

> A eficiência não aumenta a potência da fonte, mas reduz o desperdício de energia.

---

## 🔹 **9. Qualidade da Fonte**

### ⚠️ **Fontes genéricas**

* Potência não confiável
* Maior risco de falhas
* Podem danificar componentes

---

### ✅ **Fontes de qualidade**

* Potência real
* Estabilidade elétrica
* Sistemas de proteção

---

## 🔹 **10. Fator de Correção de Potência (PFC)**

O PFC melhora o aproveitamento da energia elétrica.

### 🔧 Tipos:

#### 🔹 **PFC Passivo**

* Mais simples
* Menor eficiência

#### 🔹 **PFC Ativo**

* Mais eficiente
* Ajuste automático de tensão (100V–240V)
* Presente em fontes modernas e associado a melhor aproveitamento da energia.

---

### 📌 Importância:

* Melhor desempenho
* Menor desperdício
* Maior estabilidade

---

## 🔹 **11. Aterramento Elétrico**

> Ligação do sistema elétrico ao solo para segurança e estabilidade.

### ⚡ Funções:

* Proteção contra choques
* Redução de interferências
* Estabilidade elétrica

---

### ⚠️ Relação com PFC ativo:

* Funciona sem aterramento
* Porém, o aterramento melhora:

  * Segurança
  * Eficiência
  * Redução de ruídos

---

## 🔹 **12. Estabilizadores**

Equipamento antigo, atualmente **não recomendado**.

### ⚠️ Problemas:

* Atraso na resposta elétrica
* Pode causar instabilidade
* Prejudica fontes com PFC ativo

> Fontes modernas já possuem circuitos internos de regulação, tornando o estabilizador desnecessário e, em alguns casos, prejudicial.

---

## 🔹 **13. Nobreak (UPS)**

Dispositivo que mantém o sistema ligado em quedas de energia.

### 🔋 Função:

* Fornecer energia temporária
* Permitir desligamento seguro

---

### 🔧 Tipos:

* Offline (mais simples)
* Online (mais estável)

---

### ⚠️ Importante:

* Para fontes com PFC ativo:

  > Preferir nobreak com **onda senoidal pura**

---

## 🔹 **14. Módulo Isolador**

Dispositivo de proteção elétrica.

### ⚙️ Características:

* Isolamento elétrico
* Redução de interferências

---

### 📌 Particularidade:

> Pode operar sem aterramento

---

### ⚠️ Limitação:

* Não substitui aterramento adequado

---

## 🔹 **15. Filtro de Linha**

Dispositivo de proteção contra distúrbios elétricos.

### ⚡ Funções:

* Filtrar ruídos
* Proteger contra surtos
* Estabilizar a energia de entrada

---

### ✅ Uso recomendado:

* Em conjunto com fontes modernas
* Especialmente com PFC ativo

---

### ⚠️ Atenção:

* Extensões comuns não são filtros reais

---

## 🎯 **Síntese da Aula**

Nesta aula, você aprendeu que:

* A fonte de alimentação é responsável por converter e distribuir energia
* Existem diferentes tipos, conectores e níveis de potência
* A eficiência e o PFC influenciam o desempenho
* A qualidade da energia elétrica impacta diretamente o funcionamento
* Estabilizadores são inadequados para sistemas modernos
* Filtros de linha, nobreaks e aterramento são fundamentais para proteção
