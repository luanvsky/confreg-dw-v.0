# Dashboards — Conformidade de Registro de Gestão

Camada de apresentação da solução: painéis analíticos em **Power BI** para acompanhamento da conformidade de registro de gestão no **SIAFI**, com foco na melhoria da tomada de decisão no setor público.

Este diretório reúne os arquivos editáveis versionados, o histórico de evolução das versões e o relato técnico da versão mais recente.

---

## Sumário

- [Organização do diretório](#organização-do-diretório)
- [Sobre o painel](#sobre-o-painel)
- [Versões](#versões)
- [Como acessar](#como-acessar)
- [Padrão de versionamento](#padrão-de-versionamento)
- [Evolução do modelo](#evolução-do-modelo)
- [Distribuição de tarefas](#distribuição-de-tarefas)
- [Limitações conhecidas](#limitações-conhecidas)
- [Melhorias planejadas](#melhorias-planejadas)

---

## Organização do diretório

```text
dashboard/
├── pbix/                        # Versões vigentes e editáveis
│   ├── cgconfreg_v5.pbix
│   ├── cgconfreg_v7.pbix
│   ├── cgconfreg_v7.1.pbix
│   ├── cgconfreg_v7.2.pbix
│   ├── cgconfreg_v7.3.pbix
│   ├── cgconfreg_v8.1.pbix
│   ├── cgconfreg_v8.3.pbix
│   ├── cgconfreg_v8.4.pbix
│   ├── impconfreg_csv_v4.pbix
│   └── legado/                  # Versões substituídas, preservadas para histórico
│       └── cgconfreg_v6_2023-11.pbix
├── README.md                    # Este documento
└── v8.md                        # Relato técnico da versão 8
```

> Os arquivos `.pbix` são artefatos binários e não permitem revisão de diferenças em *pull requests*. Por isso, toda alteração de modelo, medida ou visão deve ser acompanhada da atualização documental correspondente.

---

## Sobre o painel

Objetivo central: **reduzir o tempo necessário para analisar os processos** que chegam à conformidade de registro de gestão, tornando a administração pública mais ágil e a decisão mais bem embasada.

**Características da solução:**

| Aspecto | Descrição |
| --- | --- |
| **Modelo** | Dimensional, com separação entre fatos e dimensões |
| **Fonte primária** | Planilha de controle no Google Sheets, publicada na web em `.xlsx` |
| **Origem dos dados** | SIAFI e Tesouro Gerencial |
| **Granularidade temporal** | Acompanhamento diário, mensal e anual |
| **Atualização** | Agendada no Power BI Service |
| **Arquitetura de conexão** | Publicação web, **sem gateway de dados local** |
| **Foco de análise** | Volume, distribuição por unidade gestora, situação da análise e tendências |

A decisão de usar a publicação web em `.xlsx` como fonte direta do Power BI Service simplifica a arquitetura e a manutenção, ao custo de depender de um recurso que não é auditável como uma conexão gerenciada. A análise completa dessa decisão, com riscos e mitigações, está em [../docs/arquitetura.md](../docs/arquitetura.md).

---

## Versões

| Versão | Arquivo | Publicação online |
| --- | --- | --- |
| 5 | [`pbix/cgconfreg_v5.pbix`](./pbix/cgconfreg_v5.pbix) | — |
| 6 | — (retirado do repositório; ver [abaixo](#artefatos-retirados-do-repositório)) | — |
| 7 | [`pbix/cgconfreg_v7.pbix`](./pbix/cgconfreg_v7.pbix) | — |
| 7.1 | [`pbix/cgconfreg_v7.1.pbix`](./pbix/cgconfreg_v7.1.pbix) | [Visualizar](https://app.powerbi.com/view?r=eyJrIjoiMDg1MTYzYWUtMzM5Zi00Zjg3LWE5Y2ItZjVlMzQ4MThjNTdkIiwidCI6IjJhMzZhZGVhLTQ5MTAtNDM3NS1hYjQzLWFiNDgxOTc0YjRlOCJ9) |
| 7.2 | [`pbix/cgconfreg_v7.2.pbix`](./pbix/cgconfreg_v7.2.pbix) | [Visualizar](https://app.powerbi.com/view?r=eyJrIjoiYTIwOTM4NDItNzU2NC00ODZmLWI4NzQtZDlmNzEwYTA3NDFkIiwidCI6IjJhMzZhZGVhLTQ5MTAtNDM3NS1hYjQzLWFiNDgxOTc0YjRlOCJ9) |
| 7.3 | [`pbix/cgconfreg_v7.3.pbix`](./pbix/cgconfreg_v7.3.pbix) | — |
| 7.4 | — (não versionada) | [Visualizar](https://app.powerbi.com/view?r=eyJrIjoiNmI1YjE3ZTktNzkzYS00NmU4LThlOTUtMDY2YzJjOTg4NDhjIiwidCI6IjJhMzZhZGVhLTQ5MTAtNDM3NS1hYjQzLWFiNDgxOTc0YjRlOCJ9) |
| 8 | — (retirado do repositório; ver [abaixo](#artefatos-retirados-do-repositório)) | [Visualizar](https://app.powerbi.com/view?r=eyJrIjoiNjM0MWIzOTYtZGEzMS00MTBmLTg4YjItNWM5YjBmZTQzZjY0IiwidCI6IjJhMzZhZGVhLTQ5MTAtNDM3NS1hYjQzLWFiNDgxOTc0YjRlOCJ9) |
| 8.1 | [`pbix/cgconfreg_v8.1.pbix`](./pbix/cgconfreg_v8.1.pbix) | — |
| 8.3 | [`pbix/cgconfreg_v8.3.pbix`](./pbix/cgconfreg_v8.3.pbix) | — |
| 8.4 | [`pbix/cgconfreg_v8.4.pbix`](./pbix/cgconfreg_v8.4.pbix) | [Visualizar](https://app.powerbi.com/view?r=eyJrIjoiMjgyNTNiNzctMTQ0Zi00YmU0LThlZmMtMzhlODE1NDZlMWMwIiwidCI6ImNmZGMwZGI0LWM2OWQtNDEzNS1iMDAzLWRmOTA2Nzc0N2NmZiJ9) |
| — | [`pbix/impconfreg_csv_v4.pbix`](./pbix/impconfreg_csv_v4.pbix) | Importação da base analítica `impconfreg` |

### Versões de legado

| Arquivo | Origem | Observação |
| --- | --- | --- |
| [`pbix/legado/cgconfreg_v6_2023-11.pbix`](./pbix/legado/cgconfreg_v6_2023-11.pbix) | Primeiro artefato versionado da versão 6, em novembro de 2023 | Substituído pelo artefato de dezembro de 2024, mantido em `pbix/`. Preservado apenas para rastreabilidade histórica |

### Artefatos retirados do repositório

| Arquivo | Motivo | Situação |
| --- | --- | --- |
| `cgconfreg_v6.pbix` | Identificação nominal de terceiros no dicionário de strings do modelo embutido | Retirado em 16/09/2026 — em armazenamento controlado |
| `cgconfreg_v8.pbix` | Identificação nominal de terceiros como valor literal de filtro no layout do relatório | Retirado em 16/09/2026 — em armazenamento controlado |

> Os dois artefatos foram retirados **da árvore e de todos os commits alcançáveis das ramificações publicadas**, por conterem identificação nominal de terceiros — conteúdo incompatível com a classificação 🔴 Restrito em repositório público, conforme a [política de dados](../docs/governanca-de-dados.md). As cópias integrais, com verificação de integridade, permanecem em armazenamento controlado e servirão de base para a **regeneração** dos painéis a partir das bases pseudonimizadas: a edição direta do `.pbix` não é segura. As publicações correspondentes no Power BI Service continuam ativas, independentes do repositório, até que essa regeneração seja concluída e publicada.

---

## Como acessar

**Arquivo editável.** Abra qualquer `.pbix` de [`pbix/`](./pbix/) com o **Power BI Desktop**. O arquivo `impconfreg_csv_v4.pbix` importa a base analítica em CSV/TSV e serve de referência para a estrutura das colunas.

**Visualização online.** As versões publicadas no **Power BI Service** estão nos links da tabela acima e não exigem a instalação do Power BI Desktop.

> Os links de publicação são de visualização restrita ao público autorizado. O acesso a recortes com identificação de servidor é classificado como 🟠 Restrito, conforme [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md).

---

## Padrão de versionamento

```text
cgconfreg_v<MAJOR>[.<MINOR>].pbix
```

| Componente | Significado | Exemplo |
| --- | --- | --- |
| `<MAJOR>` | Mudança estrutural no modelo de dados ou no conjunto de indicadores | `v8` |
| `<MINOR>` | Ajuste incremental de visão, medida ou desempenho | `v8.4` |

**Regras:**

1. Toda versão publicada recebe arquivo próprio em `pbix/` — arquivos são **imutáveis após a publicação**.
2. A versão substituída é movida para `pbix/legado/` com sufixo de data (`_AAAA-MM`) em vez de ser apagada. Artefatos que carreguem identificação de terceiros são **retirados do repositório** e passam a armazenamento controlado — ver [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md).
3. Arquivos temporários do Power BI (`~$*.pbix`, `*.pbix~`, `.pbiV5`) são ignorados por [../.gitignore](../.gitignore).
4. A versão publicada em `pbix/` deve corresponder exatamente à do Power BI Service.

---

## Evolução do modelo

| Versão | Principais mudanças |
| --- | --- |
| 5–6 | Estruturação inicial do modelo dimensional e consolidação das fontes |
| 7.x | Ampliação das visões de análise, ajustes de indicadores e refinamento visual |
| 8.x | Inclusão de nova fonte de dados, medidas DAX revisadas, otimização de desempenho e ampliação dos atributos analisados |

O relato técnico detalhado da versão 8 — desafios de conexão, tratamento da nova tabela, otimização de medidas DAX e resultados observados — está em [v8.md](./v8.md).

---

## Distribuição de tarefas

A operação contou com cinco integrantes, identificados apenas por **código pseudônimo** conforme a política de minimização de dados pessoais.

| Código | Atribuição |
| --- | --- |
| **`SRV-01`** | Extração de dados do SIAFI e edição na planilha de controle |
| **`SRV-02`** | Extração de dados do SIAFI e edição na planilha de controle |
| **`SRV-03`** | Criação das visualizações no Power BI, limpeza e transformação dos dados, modelagem e medidas DAX |
| **`SRV-04`** | Extração de dados do SIAFI e edição na planilha de controle |
| **`SRV-05`** | Extração de dados do SIAFI e edição na planilha de controle |

O mapeamento entre código pseudônimo e unidade gestora está em [../docs/unidades-gestoras.md](../docs/unidades-gestoras.md).

---

## Limitações conhecidas

| # | Limitação | Consequência |
| --- | --- | --- |
| L1 | Dependência de planilha mantida manualmente | Erros de digitação e risco de campos em branco |
| L2 | Ausência de histórico de alterações por linha | Não permite auditoria retroativa sem nova extração |
| L3 | Fonte publicada na web sem gateway | Atualização dependente de recurso sem controle de acesso granular |
| L4 | Arquivos `.pbix` são binários | Sem revisão de diferenças em *pull requests* |
| L5 | Ausência de medição formal do impacto | Os resultados relatados são observacionais, não experimentais |

---

## Melhorias planejadas

| Iniciativa | Benefício esperado |
| --- | --- |
| **Integração com banco de dados MySQL** | Consultas mais rápidas, maior escalabilidade, integridade e eliminação da atualização manual da planilha |
| **Alertas automáticos via Power Automate** | Notificação proativa de desvios nos indicadores de conformidade |
| **Análise preditiva (R/Python no Power BI)** | Identificação de tendências de não conformidade e ação preventiva |
| **Integração via API** | Visão integrada com outros sistemas de gestão |
| **Drill-through e drill-down avançados** | Exploração em diferentes granularidades para identificação de causa raiz |
| **Governança de dados** | Controles adicionais de confidencialidade e integridade |

O modelo relacional proposto está em [../docs/modelo-de-dados-mysql.md](../docs/modelo-de-dados-mysql.md); o plano de evolução completo, em [../docs/arquitetura.md](../docs/arquitetura.md).

---

## Documentos relacionados

- [../README.md](../README.md) — visão geral do projeto
- [v8.md](./v8.md) — relato técnico da versão 8
- [../docs/arquitetura.md](../docs/arquitetura.md) — arquitetura e decisões
- [../docs/modelo-de-dados-mysql.md](../docs/modelo-de-dados-mysql.md) — modelo relacional proposto
- [../docs/fontes-de-dados.md](../docs/fontes-de-dados.md) — catálogo de fontes
- [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md) — governança e classificação
