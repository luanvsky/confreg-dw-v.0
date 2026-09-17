# CONFORMIDADE IFS — Registro de Gestão (aplicação web)

Aplicação web para análise, cálculo de retenções e gestão da conformidade de documentos fiscais no **Instituto Federal de Sergipe**. Baseada no **Manual de Procedimentos para a Conformidade de Registro de Gestão — IFS** e na **Instrução Normativa RFB nº 1.234/2012**.

> **Escopo neste repositório.** Este diretório contém **apenas a documentação** da aplicação. O código-fonte é mantido em repositório próprio e não está versionado aqui. A documentação é preservada por descrever a extensão do domínio tratado pelo projeto — os tipos de documento, as alíquotas aplicáveis e o roteiro de análise —, informação relevante para a evolução do modelo de dados do Data Warehouse.

---

## Sumário

- [Demonstração](#demonstração)
- [Módulos e funcionalidades](#módulos-e-funcionalidades)
- [Tipos de documento suportados](#tipos-de-documento-suportados)
- [Stack tecnológica](#stack-tecnológica)
- [Objetivo](#objetivo)
- [Execução local](#execução-local)
- [Perguntas frequentes](#perguntas-frequentes)
- [Base legal](#base-legal)
- [Autor](#autor)

---

## Demonstração

**Aplicação publicada:** <https://ais-pre-rxxw4xraqndg73w5bkb6jj-213322120758.us-east1.run.app/>

A versão publicada é de demonstração e opera com dados fictícios de teste. **Não insira dados reais** de processos, servidores ou documentos.

---

## Módulos e funcionalidades

### 1. Análise

- **Roteiro de análise:** checklist com 11 itens críticos de verificação para Nota Fiscal.
- **Campos críticos:** validação da chave de acesso, do CNPJ do emitente contra a nota de empenho, do atesto de recebimento e das retenções tributárias da IN 1.234.
- **Progresso dinâmico:** barra de percentual de conformidade preenchida em tempo real.
- **Identificação:** conformista, processo SEI, número do documento e tipo de documento.
- **Status final:** "Sem Ocorrência" ou "Com Ocorrência".
- **Certidões e glosa:** verificação de SICAF/CND e aplicação de glosa por descumprimento contratual.

### 2. Calculadora

- **Cálculo automático de retenções** conforme a IN RFB nº 1.234/2012 e alterações posteriores.
- **Parâmetros de entrada:** valor bruto da NF-e, natureza do serviço, percentual de ISSQN retido, INSS normal e INSS especial.
- **Detalhamento federal:** IR 4,8%, CSLL 1%, COFINS 3%, PIS/PASEP 0,65%.
- **Previdenciário e municipal:** INSS normal, INSS especial, ISSQN 2%.
- **Memória de cálculo:** exibe a retenção total e o valor líquido a pagar.
- **Referências SIAFI:** DARF Único 6190 e natureza DDF por tipo de serviço.
- **Alerta ao analista:** validação sobre Simples Nacional e isenções específicas antes de confirmar a retenção.

### 3. Histórico

- **Histórico de análises:** tabela com data/hora, processo SEI, documento, resultado, ocorrências e conformista.
- **Busca de processos:** filtro por análises anteriores.
- **Exportação:** geração de relatório em CSV.
- **Rastreabilidade:** registro das conformidades realizadas.

---

## Tipos de documento suportados

A aplicação cobre 21 tipos de documento da gestão pública:

| Sigla | Documento |
| --- | --- |
| **ND** | Nota de Dotação |
| **NC** | Nota de Crédito |
| **NE** | Nota de Empenho |
| **NL** | Nota de Lançamento |
| **OB** | Ordem Bancária |
| **GPS** | Guia de Previdência Social |
| **DARF** | Documento de Arrecadação de Receitas Federais |
| **PF** | Nota de Programação Financeira |
| **PE** | Pré-Empenho |
| **NS** | Nota de Lançamento de Sistema |
| **DAR** | Documento de Arrecadação Municipal |
| **GR/GRU** | Guia de Recolhimento da União |
| **Nota Fiscal** | Análise completa com checklist |
| **SCDP** | Diárias |
| **RMA** | Almoxarifado |
| **RMB** | Bens Móveis |
| **DH** | Documento de Habilitação |
| **CPR** | Contas a Pagar e a Receber |
| **GFIP** | Guia de Recolhimento do FGTS |
| **RP** | Restos a Pagar |

---

## Stack tecnológica

| Categoria | Tecnologias |
| --- | --- |
| **Frontend** | React, TypeScript, TailwindCSS |
| **Interface** | Design system próprio, modo escuro, layout responsivo |
| **Implantação** | Google Cloud Run |
| **Legislação** | IN RFB 1.234/2012 e Manual de Conformidade IFS |

---

## Objetivo

Padronizar e agilizar a análise de conformidade de registros de gestão no IFS. O sistema verifica a validade jurídica da chave de acesso, a correspondência com o empenho e a regularidade fiscal, e calcula retenções tributárias automaticamente. O atesto deve ser realizado por servidor designado, reduzindo erros manuais e garantindo aderência à legislação federal.

---

## Execução local

O código-fonte não está neste repositório. Quando disponível localmente, o fluxo é:

```bash
npm install
npm run dev
```

A aplicação fica acessível em `http://localhost:5173`.

---

## Perguntas frequentes

**É necessário estar autenticado para usar?**
A versão atual é aberta para demonstração. A integração com o **Gov.br** está prevista no roadmap.

**Os cálculos seguem integralmente a IN 1.234?**
Seguem as alíquotas e as exceções para Simples Nacional. Valide sempre com o setor contábil antes de confirmar a retenção — a própria aplicação emite alerta nesse sentido.

**É possível usar em outro órgão público?**
Sim. O código é distribuído sob licença MIT; basta ajustar as regras específicas do órgão. Observe que os **dados** não são cobertos pela licença — consulte [../../LICENSE](../../LICENSE).

---

## Base legal

- Manual de Procedimentos para a Conformidade de Registro de Gestão — IFS
- Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012

---

## Autor

**Victor de Melo** — Mestrando em Ciência da Computação

[GitHub](https://github.com/luanvsky) · [LinkedIn](https://www.linkedin.com/in/victor-melo-5b099942)

---

## Documentos relacionados

- [../../README.md](../../README.md) — visão geral do projeto
- [../conformidade-streamlit/README.md](../conformidade-streamlit/README.md) — aplicação complementar de checklist
- [../../docs/governanca-de-dados.md](../../docs/governanca-de-dados.md) — governança e privacidade
