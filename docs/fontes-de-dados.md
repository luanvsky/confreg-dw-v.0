# Catálogo de Fontes de Dados

Documento de referência que registra **quais dados alimentam o projeto, sua origem, periodicidade, responsável e forma de acesso**. É o insumo central do catálogo de dados descrito em [governanca-de-dados.md](./governanca-de-dados.md).

---

## Sumário

- [Visão geral do fluxo](#visão-geral-do-fluxo)
- [Fontes primárias](#fontes-primárias)
- [Fontes intermediárias](#fontes-intermediárias)
- [Conjuntos de dados versionados](#conjuntos-de-dados-versionados)
- [Política de acesso](#política-de-acesso)
- [Periodicidade e janelas de atualização](#periodicidade-e-janelas-de-atualização)
- [Como solicitar acesso](#como-solicitar-acesso)

---

## Visão geral do fluxo

```text
SIAFI / Tesouro Gerencial   →   Planilha de controle   →   Power Query   →   Painel Power BI
     (origem primária)            (staging)              (tratamento)        (consumo)
```

| Camada | Natureza | Retenção histórica |
| --- | --- | --- |
| Sistemas estruturantes | Fonte da verdade contábil | Permanente, conforme legislação |
| Planilha de controle | Base operacional colaborativa | Estado atual apenas |
| Arquivos `.pbix` | Artefato de transformação e apresentação | Historizado por versão neste repositório |
| Bases exportadas (`dataset/planilhas/`) | Cópias analíticas para estudo e conferência | Por extração |

> **Limitação relevante.** A planilha de controle mantém apenas o **estado atual**; não há histórico de alterações linha a linha. Toda necessidade de auditoria retroativa depende de novas extrações dos sistemas de origem.

---

## Fontes primárias

| # | Fonte | Sistema | Descrição | Formato de extração | Responsável |
| --- | --- | --- | --- | --- | --- |
| F1 | Registro dos atos e fatos de gestão | **SIAFI** | Documentos de execução orçamentária e financeira submetidos à conformidade | Relatórios e consultas padronizadas | Equipe de conformidade |
| F2 | Consultas orçamentárias e financeiras | **Tesouro Gerencial** | Dados de apoio para conferência e complementação da análise | Exportação de consultas | Equipe de conformidade |
| F3 | Processos administrativos | **SEI** | Processos que originam os documentos analisados | Número do processo como referência | Equipe de conformidade |

---

## Fontes intermediárias

| # | Fonte | Descrição | Tecnologia | Periodicidade | Responsável |
| --- | --- | --- | --- | --- | --- |
| F4 | Planilha de controle de conformidade | Base colaborativa em que a equipe registra as análises: documento, processo, unidade gestora, responsável, data e situação | Google Sheets, publicada na web em `.xlsx` | Diária, em dias úteis | Equipe de conformidade |
| F5 | Extrações analíticas `impconfreg` | Recortes por unidade gestora e consolidado geral, utilizados para estudo e conferência | `.xlsx`, `.csv`, `.tsv` | Por extração | Victor de Melo |

A planilha de controle é a **única fonte direta** do painel publicado. As extrações `impconfreg` são utilizadas para conferência, estudo de estrutura e desenvolvimento do modelo relacional.

---

## Conjuntos de dados versionados

Os arquivos abaixo estão disponíveis em [`dataset/`](../dataset/) e classificados conforme a matriz de [governanca-de-dados.md](./governanca-de-dados.md).

| Arquivo | Descrição | Classificação |
| --- | --- | --- |
| `impconfreg_2023_v2.xlsx` | Base consolidada de 2023 — extração principal | 🟠 Restrito |
| `impconfreg_2023_v2_geral.tsv` | Recorte consolidado geral, formato texto | 🟡 Interno |
| `impconfreg_2023_v2_reitoria.csv` / `.tsv` | Recorte da unidade gestora Reitoria | 🟠 Restrito |

> ✅ Os recortes `impconfreg` que permanecem versionados não contêm CPF nem endereço de e-mail, e a coluna `servidor` foi substituída por código identificador (`SRV-0N`), conforme a seção de privacidade de [governanca-de-dados.md](./governanca-de-dados.md).

### Extrações retiradas do versionamento

Cinco arquivos deixaram de ser versionados em 16/09/2026 por conterem dados pessoais de terceiros — identificação de beneficiários e favorecidos, números com formato de CPF e e-mails institucionais. Passaram a existir apenas em armazenamento controlado, fora do repositório:

| Arquivo | Motivo da retirada |
| --- | --- |
| `impconfreg_2023_v2_reitoria.xlsx` | Base completa da UG Reitoria — identificação de terceiros e e-mails institucionais |
| `docs-victor-2025-02.xlsx` | Coluna `Favorecido Doc.` e CPFs |
| `docs-victor-2025-03.xlsx` | Coluna `Favorecido Doc.` e CPFs |
| `docs-victor-formatacao.tsv` | Coluna `Favorecido Doc.` e CPFs |
| `docs-responsavel-2-formatacao.tsv` | CPFs |

O detalhamento está em [../dataset/README.md](../dataset/README.md#retirados-do-repositório--armazenamento-controlado) e no incidente `INC-04` de [governanca-de-dados.md](./governanca-de-dados.md#inc-04--dados-pessoais-de-terceiros-no-histórico-do-repositório).

---

## Política de acesso

O acesso aos sistemas de origem e à planilha de controle é **restrito a servidores formalmente designados** para as atividades de conformidade de registro de gestão.

- Os links de compartilhamento da planilha são **internos e nominais**, concedidos por convite do proprietário.
- Links de compartilhamento **não são versionados neste repositório**, por se tratar de recurso de acesso a dado classificado como 🟡 Interno e por conterem identificadores de sessão.
- O acesso ao painel publicado é concedido conforme a classificação do conteúdo: 🟢 Público para os indicadores agregados, 🟠 Restrito para recortes nominais.

> **Atenção.** Links de compartilhamento do SharePoint/OneDrive concedem acesso a quem os possui. Não devem ser publicados em repositórios, issues ou documentos de circulação ampla. Caso tenham sido expostos, recomenda-se revogar o compartilhamento e emitir novo convite nominal.

---

## Periodicidade e janelas de atualização

| Fonte | Frequência | Janela esperada | Monitoramento |
| --- | --- | --- | --- |
| SIAFI / Tesouro Gerencial | Diária, em dias úteis | Início do expediente | Manual |
| Planilha de controle | Diária, em dias úteis | Ao longo do expediente | Manual |
| Atualização agendada do painel | Diária | Após o fechamento do dia | Verificação diária do status de atualização |
| Bases exportadas (`dataset/`) | Sob demanda | Conforme necessidade de análise | — |

Falhas de atualização devem ser tratadas como incidente, pois afetam diretamente a tempestividade dos indicadores.

---

## Como solicitar acesso

1. Identifique a fonte desejada (F1 a F5) e a finalidade do uso.
2. Formalize a solicitação ao responsável indicado na tabela, com justificativa e escopo.
3. O acesso é concedido pelo princípio da **menor permissão** e vinculado ao perfil apropriado.
4. Registre a concessão no controle de acessos da unidade.

---

## Documentos relacionados

- [governanca-de-dados.md](./governanca-de-dados.md) — classificação, qualidade e privacidade
- [arquitetura.md](./arquitetura.md) — arquitetura completa da solução
- [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) — modelo relacional proposto
- [dataset/README.md](../dataset/README.md) — inventário dos conjuntos de dados
