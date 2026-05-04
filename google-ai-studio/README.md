# CONFORMIDADE IFS - Registro de Gestão

Sistema web para análise, cálculo de retenções e gestão de conformidade de documentos fiscais no Instituto Federal de Sergipe. Baseado no Manual de Procedimentos para a Conformidade de Registro de Gestão - IFS e na IN RFB nº 1.234/2012.

### 🚀 Demo
**Link da aplicação:** [Acesse aqui](https://ais-pre-rxxw4xraqndg73w5bkb6jj-213322120758.us-east1.run.app/)

## ✨ Módulos e Funcionalidades

### 1. Módulo Análise
- **Roteiro de Análise**: Checklist com 11 itens críticos de verificação para Nota Fiscal
- **Campos Críticos**: Validação de Chave de Acesso, CNPJ Emitente vs NE, Atesto de Recebimento, Retenções Tributárias IN 1234
- **Progresso Dinâmico**: Barra de % de conformidade preenchida em tempo real
- **Identificação Completa**: Conformista, Processo SEI, Número do Documento e Tipo de Documento
- **Status Final**: "Sem Ocorrência" ou "Com Ocorrência" para conclusão da análise
- **Certidões e Glosa**: Verificação de SICAF/CND e aplicação de glosa por descumprimento contratual

### 2. Módulo Calculadora
- **Cálculo Automático de Retenções**: Conforme IN RFB nº 1.234/2012 e alterações posteriores
- **Parâmetros de Cálculo**: Valor Bruto da NF-e, Natureza do Serviço, % ISSQN Retido, INSS Normal e Especial
- **Detalhamento Federal**: IR 4.8%, CSLL 1%, COFINS 3%, PIS/PASEP 0.65%
- **Previdenciário e Municipal**: INSS Normal, INSS Especial, ISSQN 2%
- **Memória de Cálculo**: Exibe Retenção Total e Valor Líquido a Pagar
- **Referências SIAFI**: DARF Único 6190 e Natureza DDF por tipo de serviço
- **Alerta ao Auditor**: Validação sobre Simples Nacional e isenções específicas antes de confirmar a retenção

### 3. Módulo Histórico
- **Histórico de Análises**: Tabela com Data/Hora, Processo SEI, Documento, Resultado, Ocorrências e Conformista
- **Busca de Processos**: Campo para filtrar análises anteriores
- **Exportação**: Botão "Baixar CSV" para geração de relatórios
- **Rastreabilidade**: Registro completo de todas as conformidades realizadas

## 📋 Tipos de Documento Suportados
O sistema cobre 21 tipos de documentos da gestão pública:

| Sigla | Documento |
| --- | --- |
| **ND** | Nota de Dotação |
| **NC** | Nota de Crédito |
| **NE** | Nota de Empenho |
| **NL** | Nota de Lançamento |
| **OB** | Ordem Bancária |
| **GPS** | Guia de Previdência Social |
| **DARF** | Doc. de Arrecadação de Receitas Federais |
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

## 🛠️ Tech Stack
| Categoria | Tecnologias |
| --- | --- |
| **Frontend** | React, TypeScript, TailwindCSS |
| **UI/UX** | Design System próprio, Dark Mode, Responsivo |
| **Deploy** | Google Cloud Run |
| **Legislação** | IN RFB 1.234/2012, Manual de Conformidade IFS |

## 🎯 Objetivo
Padronizar e agilizar a análise de conformidade de registros de gestão no IFS. O sistema verifica validade jurídica da Chave de Acesso, correspondência com o empenho, regularidade fiscal e calcula retenções tributárias automaticamente. O Atesto deve ser realizado por servidor designado, reduzindo erros manuais e garantindo aderência à legislação federal.


## ⚙️ Como rodar localmente
```bash
# Clone o repositório
git clone https://github.com/seu-user/conformidade-ifs.git

# Entre na pasta
cd conformidade-ifs

# Instale as dependências
npm install

# Rode o projeto
npm run dev
```
Acesse `http://localhost:5173` no navegador.

🧠 Aprendizados
Com esse projeto pratiquei:

1. Desenvolvimento de SaaS para compliance no setor público
2. Implementação de lógica tributária complexa da IN RFB 1234/2012
3. Arquitetura de sistemas com múltiplos módulos: análise + cálculo + auditoria
4. Exportação de dados e geração de relatórios em CSV
Deploy de aplicações containerizadas no Google Cloud Run

❓ FAQ
P: Preciso estar logado para usar?
R: A versão atual é aberta para demonstração. Versão com Gov.br está no roadmap.

P: Os cálculos seguem 100% a IN 1234?
R: Sim, incluindo alíquotas atualizadas e exceções para Simples Nacional. Sempre valide com o setor contábil.

P: Posso usar em outro órgão público?
R: Sim, o código é MIT. Só ajustar as regras específicas do seu órgão.

📄 Base Legal
Baseado no Manual de Procedimentos para a Conformidade de Registro de Gestão - IFS e na Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012.


👨‍💻 Autor
Victor de Melo

[GitHub](https://github.com/luanvsky)
[LinkedIn](https://linkedin.com/in/victor-melo-5b099942)

<div align="center"> Desenvolvido para otimizar a gestão pública no IFS 🇧🇷 </div>
