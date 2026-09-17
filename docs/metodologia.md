# Metodologia

Documento que registra o processo de desenvolvimento adotado no projeto **Conformidade de Registro de Gestão — Data Warehouse & Business Intelligence**, baseado em princípios ágeis com adaptação do Scrum ao contexto de uma equipe pequena em ambiente público.

---

## Sumário

- [Contexto](#contexto)
- [Por que agilidade neste projeto](#por-que-agilidade-neste-projeto)
- [Estrutura do processo](#estrutura-do-processo)
- [Papéis](#papéis)
- [Artefatos](#artefatos)
- [Cerimônias](#cerimônias)
- [Adaptações ao contexto público](#adaptações-ao-contexto-público)
- [Gestão do fluxo de trabalho](#gestão-do-fluxo-de-trabalho)
- [Definição de pronto](#definição-de-pronto)
- [Aprendizado acumulado](#aprendizado-acumulado)

---

## Contexto

| Característica | Descrição |
| --- | --- |
| **Domínio** | Conformidade de registro de gestão no serviço público federal |
| **Equipe** | Pequena, com acumulação de papéis |
| **Demanda** | Recorrente e contínua, com picos no fechamento mensal |
| **Ambiente** | Regulação em constante alteração (instruções normativas, manuais e alterações posteriores) |
| **Produto** | Painel analítico publicado e mantido ao longo do tempo |

---

## Por que agilidade neste projeto

O cenário apresenta três características que tornam a abordagem ágil mais adequada que um modelo sequencial:

1. **Requisitos emergentes.** As necessidades informacionais da gestão evoluem conforme os painéis passam a ser utilizados.
2. **Ambiente regulatório mutável.** Alterações normativas exigem ajuste imediato de regras de negócio e indicadores.
3. **Entrega incremental de valor.** Um painel parcial em produção gera valor antes da conclusão do escopo completo.

Um planejamento integral *a priori* seria rapidamente invalidado por qualquer alteração normativa, tornando as entregas curtas e iterativas a escolha mais racional.

---

## Estrutura do processo

O ciclo de trabalho segue o padrão:

```text
Necessidade da gestão
        ↓
Refinamento do item de backlog
        ↓
Implementação no Power BI / Power Query / DAX
        ↓
Validação de totais contra a base de origem
        ↓
Publicação no Power BI Service
        ↓
Coleta de feedback com a equipe de conformidade
        ↓
Novo item de backlog
```

Cada iteração produz um **incremento utilizável** — uma nova versão do painel, uma medida adicional ou uma correção de indicador — publicado e disponível para uso imediato.

---

## Papéis

| Papel Scrum | Ocupante no projeto | Responsabilidade |
| --- | --- | --- |
| **Product Owner** | Coordenação da conformidade de registro de gestão | Prioriza o backlog, define o que gera valor para a gestão e valida os resultados |
| **Scrum Master** | Acumulado pela liderança técnica | Remove impedimentos, facilita as cerimônias e protege o foco da equipe |
| **Time de desenvolvimento** | Victor de Melo (modelagem, Power Query, DAX e visualização) e equipe de conformidade (extração e curadoria) | Constrói o incremento e garante a qualidade dos dados |

---

## Artefatos

| Artefato Scrum | Instrumento utilizado | Observação |
| --- | --- | --- |
| **Product Backlog** | Issues do GitHub + quadro de roadmap no GitHub Projects | Cada item descreve a necessidade informacional, não a solução técnica |
| **Sprint Backlog** | Issues atribuídas e em andamento | Representa o compromisso da iteração corrente |
| **Incremento** | Versão publicada do painel (`.pbix` + publicação no Power BI Service) | Versionado neste repositório |
| **Definição de Pronto** | Checklist de validação | Ver seção [Definição de pronto](#definição-de-pronto) |

O backlog é mantido no GitHub, na aba de *issues* do repositório e no quadro de roadmap, o que mantém rastreabilidade entre necessidade, implementação e entrega.

---

## Cerimônias

| Cerimônia | Adaptação no projeto |
| --- | --- |
| **Planejamento da sprint** | Seleção dos itens de maior valor, com estimativa de esforço e definição do incremento esperado |
| **Reunião diária** | Alinhamento breve sobre o andamento das análises, impedimentos de extração e falhas de atualização |
| **Revisão da sprint** | Apresentação do incremento à área de conformidade e à gestão, com coleta estruturada de feedback |
| **Retrospectiva** | Avaliação do processo: o que funcionou, o que atrapalhou e o que será ajustado na próxima iteração |

As cerimônias foram **encurtadas e flexibilizadas** em relação ao formato canônico, em razão do tamanho reduzido da equipe e da natureza contínua das atividades de conformidade, que não podem ser interrompidas para dar lugar a rituais longos.

---

## Adaptações ao contexto público

| Desafio | Adaptação adotada |
| --- | --- |
| Regulação em mudança | Alterações normativas entram no backlog como item prioritário, com ajuste imediato de regras e indicadores |
| Equipe com acúmulo de papéis | Cerimônias condensadas e quadros visuais que permitem acompanhamento assíncrono |
| Demanda operacional contínua inegociável | Entregas planejadas para os períodos de menor volume de processos |
| Necessidade de evidência e auditoria | Uso de versionamento em Git e documentação das decisões arquiteturais em [`docs/`](./) |
| Múltiplas unidades gestoras | Análise segmentada por unidade, o que exige coordenação entre diferentes responsáveis |

---

## Gestão do fluxo de trabalho

O acompanhamento é feito por quadro visual com as etapas:

```text
Backlog → A fazer → Em andamento → Em validação → Concluído
```

A etapa **Em validação** é obrigatória e não pode ser suprimida: nenhum indicador é publicado sem conferência dos totais contra a base de origem. Essa é a principal adaptação de qualidade do processo ao domínio contábil, em que um número incorreto tem consequência decisória direta.

---

## Definição de pronto

Um item de backlog é considerado concluído quando:

- [ ] A implementação está funcionando no arquivo `.pbix` versionado.
- [ ] Os totais dos indicadores foram conferidos contra a planilha de controle.
- [ ] A versão publicada no Power BI Service corresponde ao arquivo versionado.
- [ ] Os nomes de medida e de visão seguem o padrão do projeto.
- [ ] A documentação afetada (`README.md`, `docs/`) foi atualizada.
- [ ] Não há exposição de dado pessoal ou link interno.

---

## Aprendizado acumulado

| Aprendizado | Implicação |
| --- | --- |
| A publicação web em `.xlsx` simplifica a arquitetura ao dispensar o gateway | Decisão mantida e documentada em [arquitetura.md](./arquitetura.md) |
| A conferência de totais contra a origem é indispensável | Tornou-se etapa formal do fluxo, não verificada ad hoc |
| A planilha não preserva histórico de alterações | Motivou o desenho do modelo relacional em [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) |
| A distribuição de carga de trabalho por unidade é informação de gestão relevante | Deu origem ao relatório consolidado em [relatorios/](./relatorios/) |
| A documentação dispersa dificultava a continuidade do projeto | Motivou a reorganização documental em [`docs/`](./) |

---

## Documentos relacionados

- [governanca-de-dados.md](./governanca-de-dados.md) — políticas de governança e qualidade
- [arquitetura.md](./arquitetura.md) — arquitetura técnica da solução
- [CONTRIBUTING.md](../CONTRIBUTING.md) — fluxo de contribuição no repositório
- [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md) — resultado consolidado da operação
