# Governança de Dados

Documento de referência para a gestão dos dados do projeto **Conformidade de Registro de Gestão — Data Warehouse & Business Intelligence**.

Este documento conecta as práticas de engenharia de dados adotadas no projeto às dimensões clássicas de governança de dados, com atenção às particularidades do **domínio contábil público**: obrigatoriedade de rastreabilidade, exigência de auditabilidade, sensibilidade das informações e necessidade de prestação de contas.

---

## Sumário

- [Objetivo e escopo](#objetivo-e-escopo)
- [Princípios norteadores](#princípios-norteadores)
- [Papéis e responsabilidades](#papéis-e-responsabilidades)
- [Classificação da informação](#classificação-da-informação)
- [Ciclo de vida do dado](#ciclo-de-vida-do-dado)
- [Dimensões de qualidade de dados aplicadas](#dimensões-de-qualidade-de-dados-aplicadas)
- [Linhagem e rastreabilidade](#linhagem-e-rastreabilidade)
- [Catálogo de dados e dicionário](#catálogo-de-dados-e-dicionário)
- [Privacidade e proteção de dados pessoais](#privacidade-e-proteção-de-dados-pessoais)
- [Segurança e controle de acesso](#segurança-e-controle-de-acesso)
- [Riscos e controles](#riscos-e-controles)
- [Registro de incidentes de exposição](#registro-de-incidentes-de-exposição)
- [Indicadores de governança](#indicadores-de-governança)
- [Roteiro de maturidade](#roteiro-de-maturidade)
- [Referências](#referências)

---

## Objetivo e escopo

**Objetivo.** Estabelecer diretrizes para que os dados que sustentam os painéis de conformidade sejam **confiáveis, rastreáveis, íntegros e adequadamente protegidos**, garantindo que os indicadores utilizados na tomada de decisão reflitam fielmente os atos de gestão registrados.

**Escopo.** Abrange os dados que percorrem o fluxo origem → planilha de controle → Power Query → modelo dimensional → painel, bem como os artefatos derivados mantidos neste repositório e as aplicações de apoio em [`apps/`](../apps/).

**Fora de escopo.** A gestão dos sistemas estruturantes de origem (SIAFI e Tesouro Gerencial), cujas políticas de acesso e retenção são definidas por seus órgãos gestores.

---

## Princípios norteadores

| Princípio | Aplicação no projeto |
| --- | --- |
| **Finalidade** | Os dados são tratados exclusivamente para fins de análise de conformidade de registro de gestão e apoio à decisão. |
| **Adequação** | Coleta-se apenas o necessário para a análise: documento, processo, unidade gestora, responsável e data. |
| **Transparência** | A origem e as regras de transformação de cada indicador são documentadas neste diretório. |
| **Segurança** | Acesso restrito por perfil e por unidade gestora, com princípio da menor permissão. |
| **Rastreabilidade** | Todo indicador deve ser reconduzível à sua fonte primária e às transformações aplicadas. |
| **Responsabilização** | Cada conjunto de dados possui um responsável formalmente identificado. |
| **Qualidade por projeto** | Regras de validação são definidas antes da publicação dos indicadores, não depois. |
| **Prestação de contas** | Os artefatos aqui mantidos servem como evidência da evolução e das decisões do projeto. |

---

## Papéis e responsabilidades

A definição explícita de papéis é o que distingue um projeto de dados de uma iniciativa de governança de dados.

| Papel | Responsabilidade | Ocupante |
| --- | --- | --- |
| **Patrocinador (data owner institucional)** | Define prioridades, aprova a política de acesso e responde institucionalmente pelos dados | Gestão do IFS |
| **Proprietário do domínio (data owner)** | Responde pela correção semântica dos dados de conformidade e pelas regras de negócio | Coordenação da conformidade de registro de gestão |
| **Curador de dados (data steward)** | Garante a integridade do preenchimento, padroniza rótulos e reporta inconsistências | Equipe de conformidade |
| **Engenheiro de dados (data custodian)** | Mantém o pipeline, o modelo dimensional e as consultas do Power Query | Victor de Melo |
| **Administrador da plataforma** | Gerencia workspace, permissões, atualizações agendadas e segurança por perfil | Victor de Melo |
| **Consumidor de dados** | Utiliza os painéis respeitando a classificação e a finalidade declarada | Gestores e equipe de conformidade |

As unidades gestoras envolvidas e seus respectivos responsáveis estão relacionados em [unidades-gestoras.md](./unidades-gestoras.md).

---

## Classificação da informação

Todo dado tratado no projeto deve ser classificado antes de ser armazenado ou publicado. A classificação determina as regras de acesso, compartilhamento e retenção.

| Nível | Definição | Exemplo no projeto | Publicável neste repositório? |
| --- | --- | --- | --- |
| 🟢 **Público** | Informação de livre acesso, sem restrição | Painéis publicados no Power BI Service, documentação técnica, versões dos `.pbix` | Sim |
| 🟡 **Interno** | Informação de circulação restrita à instituição, sem dado pessoal | Planilha de controle, conjuntos de dados agregados, Termo de Referência | Somente agregada e revisada |
| 🟠 **Restrito** | Informação administrativa sensível, de acesso limitado por função | Relatórios de volume por servidor, códigos de restrição associados a processos | Não |
| 🔴 **Pessoal** | Dado pessoal identificável, nos termos da LGPD | Nome de servidor, matrícula, e-mail institucional, identificação de conformador | Não, salvo anonimização |

### Matriz de classificação dos artefatos do repositório

| Artefato | Classificação | Observação |
| --- | --- | --- |
| `dashboard/pbix/*.pbix` | 🟠 Restrito | O modelo de dados embutido de duas versões mantém identificação nominal de integrantes — ver [`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix) |
| `dashboard/README.md`, `docs/arquitetura.md` | 🟢 Público | Documentação técnica |
| `dataset/planilhas/impconfreg_2023_v2_reitoria.csv` / `.tsv` | 🟠 Restrito | Coluna `servidor` **pseudonimizada** (`SRV-0N`); o restante do conteúdo é registro contábil |
| `dataset/planilhas/impconfreg_2023_v2.xlsx` | 🟠 Restrito | Extração consolidada; varredura não localizou CPF nem e-mail institucional |
| `dataset/planilhas/impconfreg_2023_v2_geral.tsv` | 🟡 Interno | Agregação por tipo de documento; sem identificação pessoal |
| Extrações em armazenamento controlado (5 arquivos) | 🔴 Restrito — dados pessoais de terceiros | **Não versionadas.** Identificação de beneficiários e favorecidos, CPFs e e-mails institucionais — ver [`INC-04`](#inc-04--dados-pessoais-de-terceiros-no-histórico-do-repositório) |
| `docs/relatorios/analise-documental-2025.md` | 🟠 Restrito | Produtividade individual associada a código pseudônimo |
| `docs/unidades-gestoras.md` | 🟠 Restrito | Associa unidades gestoras a código pseudônimo |
| `docs/termo-referencia-aquisicao-bi.md` | 🟡 Interno | Documento administrativo de contratação |
| `apps/**` | 🟢 Público | Código-fonte de protótipos |

> **Recomendação.** Os artefatos classificados como 🟠 Restrito devem ser movidos para armazenamento institucional controlado. Enquanto permanecerem neste repositório público, o acesso deve ser tratado como **já divulgado**, com registro expresso da decisão — é o caso das bases de conformidade, mantidas por exigência de reprodutibilidade da pesquisa. Os artefatos classificados como 🔴 Restrito com dados pessoais de terceiros não admitem essa exceção e foram retirados do versionamento.

---

## Ciclo de vida do dado

| Fase | Descrição | Controle adotado |
| --- | --- | --- |
| **1. Definição** | Identificação da necessidade informacional e do indicador a ser produzido | Registro no catálogo ([fontes-de-dados.md](./fontes-de-dados.md)) |
| **2. Aquisição** | Extração do SIAFI e do Tesouro Gerencial | Uso de consultas padronizadas e reutilizáveis |
| **3. Curadoria** | Registro e padronização na planilha de controle | Padronização de rótulos e verificação de duplicidades |
| **4. Transformação** | Limpeza, tipagem e modelagem no Power Query | Consultas versionadas nos arquivos `.pbix` |
| **5. Armazenamento** | Persistência na planilha e nos arquivos do repositório | Versionamento Git dos artefatos publicáveis |
| **6. Uso** | Análise pelos painéis e aplicações de apoio | Acesso por perfil e por unidade gestora |
| **7. Compartilhamento** | Publicação para as partes interessadas | Links públicos apenas para conteúdo classificado como 🟢 |
| **8. Retenção** | Manutenção pelo prazo legal aplicável | Prazos definidos pela legislação arquivística e contábil |
| **9. Descarte** | Eliminação segura após o prazo | A ser formalizado com a área de arquivo institucional |

---

## Dimensões de qualidade de dados aplicadas

As dimensões abaixo são aplicadas aos campos efetivamente presentes na base de conformidade.

| Dimensão | Definição | Verificação aplicável no projeto | Situação atual |
| --- | --- | --- | --- |
| **Completude** | Ausência de valores obrigatórios em branco | Verificar nulos em `documento`, `numero`, `servidor` e `data` | ⚠️ Verificação manual |
| **Acurácia** | Correspondência entre o dado registrado e o fato ocorrido | Conferência amostral contra o SIAFI | ⚠️ Verificação manual |
| **Consistência** | Coerência entre registros correlacionados | Documento classificado deve possuir código de restrição compatível | ❌ Não automatizada |
| **Unicidade** | Ausência de duplicidade indevida | Verificar duplicidade por `numero` de documento | ⚠️ Verificação manual |
| **Validade** | Aderência a domínios e formatos definidos | `data` no formato `dd/mm/aaaa`; códigos de restrição pertencentes à lista oficial | ⚠️ Parcial |
| **Tempestividade** | Disponibilidade do dado no prazo esperado | Monitoramento diário da atualização agendada do painel | ✅ Monitorado |
| **Rastreabilidade** | Possibilidade de reconstruir a origem do dado | Recondução do indicador ao registro na planilha de controle | ⚠️ Documentada em texto |

**Legenda:** ✅ implantado · ⚠️ parcial ou manual · ❌ inexistente

### Regras de validação propostas

```text
R01 — documento e numero não podem ser nulos ou vazios.
R02 — a combinação (numero, unidade_gestora) deve ser única na base.
R03 — data deve ser uma data válida e não posterior à data corrente.
R04 — registros com situação "COM RESTRIÇÃO" devem possuir ao menos um código de restrição.
R05 — registros com situação "SEM RESTRIÇÃO" não podem possuir código de restrição associado.
R06 — unidade_gestora deve pertencer à lista oficial de unidades do IFS.
R07 — todo documento analisado deve estar associado a um processo SEI válido.
```

A implantação dessas regras na camada de ingestão é pré-requisito para reduzir a dependência de conferência manual.

---

## Linhagem e rastreabilidade

A linhagem descreve o caminho percorrido por cada dado, da origem ao indicador. É o que permite responder "de onde veio este número?" — pergunta central em auditoria contábil.

```mermaid
flowchart LR
    S[SIAFI / Tesouro Gerencial] --> P[Planilha de controle]
    P --> Q[Power Query]
    Q --> M[Modelo dimensional]
    M --> D[Medida DAX]
    D --> V[Visual do painel]
```

### Exemplo de rastreabilidade de um indicador

| Etapa | Elemento | Registro |
| --- | --- | --- |
| Indicador | Percentual de documentos com restrição | Cartão no painel |
| Medida DAX | `% Documentos com Restrição` | Definida no arquivo `.pbix` |
| Fato | Tabela de análises de conformidade | Modelo dimensional |
| Transformação | Normalização do rótulo de situação | Consulta Power Query |
| Origem | Coluna de situação na planilha de controle | Google Sheets |
| Fonte primária | Registro do ato de gestão | SIAFI |

**Lacuna identificada.** Cada indicador deveria ter sua linhagem registrada de forma estruturada, permitindo auditoria automatizada. A forma narrativa atual depende de conhecimento tácito da equipe.

---

## Catálogo de dados e dicionário

O catálogo formaliza **quais dados existem, de onde vêm, quem responde por eles e com que frequência são atualizados**. As fontes estão catalogadas em [fontes-de-dados.md](./fontes-de-dados.md).

### Dicionário de dados (camada de conformidade)

| Campo | Tipo | Obrigatório | Descrição | Regra de negócio |
| --- | --- | --- | --- | --- |
| `documento` | texto | Sim | Tipo do documento de gestão analisado | Deve pertencer à lista oficial de tipos documentais |
| `numero` | texto | Sim | Identificador do documento no sistema de origem | Único por unidade gestora |
| `servidor` | texto | Sim | Código pseudônimo do responsável pela análise de conformidade | Formato `SRV-0N`; a correspondência nome ↔ código é mantida fora do repositório |
| `data` | data | Sim | Data da análise | Formato `dd/mm/aaaa`, não futura |
| `unidade_gestora` | texto/código | Sim | Unidade responsável pelo registro | Deve constar na lista oficial de unidades |
| `situacao` | texto | Sim | Resultado da análise | Domínio: `SEM RESTRIÇÃO` ou `COM RESTRIÇÃO` |
| `codigo_restricao` | texto | Condicional | Código que caracteriza a restrição | Obrigatório quando `situacao = COM RESTRIÇÃO` |

---

## Privacidade e proteção de dados pessoais

O projeto trata dados pessoais de servidores públicos envolvidos na análise de conformidade. A observância à **Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)** é requisito do projeto, não opção.

### Dados pessoais identificados

| Dado | Onde ocorre | Finalidade | Tratamento aplicado |
| --- | --- | --- | --- |
| Nome do integrante responsável pela análise | Documentação, bases redistribuídas e arquivos `.xlsx` | Distribuição de carga de trabalho e acompanhamento de produtividade | ✅ **Pseudonimizado** para código `SRV-0N` |
| Métricas individuais de produtividade | Relatório de análise documental | Gestão da força de trabalho | Mantidas, agora vinculadas apenas a código |
| E-mail institucional | Colunas de controle das bases `.xlsx` | Contato operacional | ✅ **Removido do versionamento** — arquivos em armazenamento controlado |
| Nome de terceiros (beneficiários e favorecidos) | Conteúdo das bases `.xlsx` | Objeto próprio da análise de conformidade | ✅ **Removido do versionamento** — arquivos em armazenamento controlado |
| Identificação de unidade gestora | Todo o fluxo | Análise por unidade | Mantida — dado institucional, não pessoal |

### Pseudonimização e minimização

A identificação nominal dos integrantes foi substituída por **código pseudônimo** em toda a documentação e nas bases redistribuídas.

| Item | Definição |
| --- | --- |
| **Esquema de código** | `SRV-01` a `SRV-05`, atribuídos por ordem alfabética do nome original |
| **Escopo** | Nomes em documentos `.md`; coluna `servidor` e texto livre de observação das bases `.csv`/`.tsv`; células, listas de seleção e comentários dos arquivos `.xlsx` |
| **Métricas agregadas** | Preservadas integralmente — a substituição alterou apenas a identificação, não os valores |
| **Correspondência código ↔ pessoa** | **Não versionada.** Mantida pelo responsável pelo tratamento dos dados, fora do controle de versão |
| **Natureza jurídica** | **Pseudonimização, não anonimização** — o código é reversível por quem detém a tabela de correspondência, e a combinação de unidade gestora, percentual de participação e período permite identificação indireta |

A convenção aplicada está descrita em [unidades-gestoras.md](./unidades-gestoras.md#convenções-de-identificação).

### Dados pessoais de terceiros

As extrações do projeto contêm identificação de **pessoas alheias à equipe**: beneficiários e favorecidos de pagamento, além de endereços de e-mail institucional em colunas de controle. Esse conteúdo é **inerente ao registro contábil** — removê-lo ou substituí-lo destruiria o valor de auditoria do próprio dado, que é o objeto da análise de conformidade.

O tratamento aplicado não foi a pseudonimização, e sim a **segregação**: em 16/09/2026 os cinco arquivos afetados foram retirados do versionamento e passaram a existir apenas em armazenamento controlado, fora da árvore de trabalho.

| Arquivo | Dados pessoais identificados na varredura |
| --- | --- |
| `impconfreg_2023_v2_reitoria.xlsx` | 83 CPFs formatados distintos; 313 sequências de 11 dígitos; 2 e-mails institucionais |
| `docs-victor-2025-02.xlsx` | 4 CPFs formatados; coluna `Favorecido Doc.`; 156 sequências de 11 dígitos |
| `docs-victor-2025-03.xlsx` | 5 CPFs formatados; coluna `Favorecido Doc.`; 119 sequências de 11 dígitos |
| `docs-victor-formatacao.tsv` | 5 CPFs formatados; coluna `Favorecido Doc.` |
| `docs-responsavel-2-formatacao.tsv` | 5 CPFs formatados |

Os contadores são **distintos** e provêm de varredura por expressão regular sobre o conteúdo textual dos arquivos. Duas ressalvas de método: sequências de onze dígitos podem corresponder a códigos de documento, e não a CPF; e a varredura cobre o texto extraído dos arquivos, não o conteúdo comprimido — portanto os números são um **piso**, não um total exato.

**Tratamento:**

| Item | Definição |
| --- | --- |
| **Medida aplicada** | Retirada do versionamento, não pseudonimização — o dado não pode ser descaracterizado sem perder a função probatória |
| **Localização atual** | Diretório de armazenamento controlado, fora do repositório, com leitor próprio descrevendo procedência, hashes de integridade e regras de uso |
| **Salvaguarda técnica** | Os cinco caminhos permanecem bloqueados no `.gitignore`, impedindo o retorno acidental ao versionamento |
| **Base legal** | Execução de políticas públicas e cumprimento de obrigação legal, no âmbito da conformidade de registro de gestão |
| **Acesso** | Restrito a quem executa a análise; sem redistribuição |

> **Atualização de 16/09/2026.** A recuperabilidade retroativa foi tratada pela [reescrita do histórico](#reescrita-do-histórico): os cinco arquivos e os artefatos de `dataset/.xls/` deixaram de existir em qualquer commit alcançável das três ramificações publicadas. Restam dois resíduos que o `force push` não elimina — objetos antigos ainda recuperáveis por SHA direto até a coleta de lixo do GitHub, e as referências de *pull request* `47` e `92`. Ambos estão registrados em [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push).

### Medidas adotadas e recomendadas

- **Minimização:** os painéis expõem indicadores agregados, não registros individuais.
- **Pseudonimização na publicação:** o campo `servidor`, o texto livre de observação das bases redistribuídas e os campos nominais dos arquivos `.xlsx` foram substituídos por código.
- **Segregação:** os arquivos com identificação de terceiros foram retirados do versionamento e mantidos em armazenamento controlado.
- **Controle de finalidade:** o uso dos dados é restrito à análise de conformidade e à gestão da força de trabalho.
- **Revisão de exposição:** artefatos classificados como 🟠 Restrito não deveriam ser mantidos em repositório público.
- **Registro de decisão:** toda divulgação externa deve ser precedida de avaliação formal.

> **Alerta de conformidade.** A presença de nomes de servidores e de métricas individuais de produtividade em repositório público caracterizou exposição de dados pessoais (registrada em [`INC-02`](#inc-02--identificação-nominal-de-integrantes-em-artefatos-versionados)). A presença de identificação de terceiros em escala caracterizou exposição adicional ([`INC-04`](#inc-04--dados-pessoais-de-terceiros-no-histórico-do-repositório)). A mitigação na árvore atual e no histórico alcançável está concluída. Permanecem abertas três frentes: a regeneração dos painéis (`.pbix`), a revogação do compartilhamento na origem e a remoção dos objetos que a plataforma retém fora do alcance do `force push`.

---

## Segurança e controle de acesso

| Controle | Descrição | Situação |
| --- | --- | --- |
| **Workspace dedicado** | Publicação dos painéis em workspace institucional próprio | ✅ |
| **Segurança em nível de linha (RLS)** | Restringir a visão por unidade gestora, conforme o perfil do usuário | 🔲 Proposto |
| **Perfis de acesso** | Diferenciação entre administrador, curador e consumidor | 🔲 Proposto |
| **Atualização agendada monitorada** | Verificação diária da atualização do conjunto de dados | ✅ |
| **Links públicos controlados** | Publicação apenas de conteúdos classificados como 🟢 Público | ⚠️ Requer revisão |
| **Pseudonimização** | Identificação nominal dos integrantes substituída por código `SRV-0N` nos artefatos de texto, nas bases redistribuídas e em todas as versões do histórico | ✅ Aplicada — pendente nos `.pbix` ([`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix)) |
| **Segregação de dados de terceiros** | Arquivos com identificação de beneficiários e favorecidos retirados do versionamento e mantidos em armazenamento controlado, com caminhos bloqueados no `.gitignore` | ✅ Aplicada |
| **Reescrita do histórico** | Remoção dos caminhos sensíveis e substituição de identificadores em todos os commits alcançáveis, com `git filter-repo` e `force push` sobre cópia integral do histórico original | ✅ Aplicada — resíduo em [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |
| **Gestão de credenciais e links compartilhados** | Nenhuma credencial, token ou link interno versionado | ⚠️ [`INC-01`](#inc-01--link-de-compartilhamento-interno-com-token-de-acesso) — URLs eliminadas na reescrita, revogação na origem pendente |

---

## Riscos e controles

| # | Risco | Probabilidade | Impacto | Controle |
| --- | --- | --- | --- | --- |
| R1 | Indicador incorreto utilizado em decisão de gestão | Média | Alto | Conferência de totais contra a origem; versionamento dos `.pbix` |
| R2 | Exposição de dados pessoais de integrantes em repositório público | Média | Alto | Pseudonimização aplicada na documentação, nas bases redistribuídas e no histórico alcançável ([`INC-02`](#inc-02--identificação-nominal-de-integrantes-em-artefatos-versionados)); exposição residual nos `.pbix` ([`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix)) |
| R3 | Quebra da consulta por alteração da estrutura da planilha | Média | Médio | Monitoramento diário; padronização de colunas |
| R4 | Duplicidade de registros inflando indicadores | Média | Alto | Regra de unicidade `R02` |
| R5 | Falha silenciosa na atualização agendada | Média | Alto | Verificação diária do status de atualização |
| R6 | Perda da linhagem por rotatividade da equipe | Alta | Médio | Documentação neste diretório e no catálogo |
| R7 | Divergência entre painel publicado e versão do `.pbix` | Média | Médio | Correspondência de identificadores de versão ([CONTRIBUTING.md](../CONTRIBUTING.md)) |
| R8 | Dependência de pessoa única (*bus factor*) | Alta | Médio | Versionamento em Git e documentação do processo |
| R9 | Link de compartilhamento interno com token de acesso exposto em histórico de repositório público | Média | Alto | URLs removidas de todos os commits alcançáveis pela [reescrita do histórico](#reescrita-do-histórico); revogação do compartilhamento na origem pendente; proibição de versionar URLs internas ([CONTRIBUTING.md](../CONTRIBUTING.md)) |
| R10 | Identificação nominal residual nos `.pbix` e nos relatórios publicados — no dicionário de strings do modelo, como valor literal de filtro e como rótulo de campo | Alta | Médio | Retirada dos dois artefatos com identificação de terceiros (executada em 16/09/2026); regeneração dos painéis a partir das bases pseudonimizadas, com revisão dos filtros que usam prenome como valor literal, e republicação ([`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix)) |
| R11 | Reidentificação indireta por cruzamento das métricas individuais com bases públicas do Instituto | Média | Médio | Agregação das métricas ou substituição do código de projeto por código funcional institucional |
| R12 | Dados pessoais de terceiros recuperáveis no histórico do repositório público, apesar da remoção da árvore atual | Média | Alto | [Reescrita do histórico](#reescrita-do-histórico) executada em 16/09/2026 com `git filter-repo`; resíduo restrito aos objetos retidos pela plataforma e às referências de *pull request* ([`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push)) |
| R13 | Dados pessoais publicados no corpo de issues, no corpo de *pull requests* e em comentários — superfície fora do alcance da reescrita de histórico | Alta | Alto | Exclusão manual dos itens afetados ([`INC-06`](#inc-06--exposição-em-issues-comentários-e-site-publicado)); aviso de não colar dados pessoais nos modelos de issue; triagem obrigatória antes de publicar qualquer conteúdo de discussão |
| R14 | Republicação automática da árvore do repositório em site público, sem controle de acesso e sujeito a indexação por buscadores | Alta | Médio | Publicação restrita à árvore corrente; retenção de um dia nos artefatos de implantação; desabilitar o site quando ele não for necessário ([`INC-06`](#inc-06--exposição-em-issues-comentários-e-site-publicado)) |

---

## Registro de incidentes de exposição

Registro das ocorrências de exposição de informação identificadas no repositório, com a respectiva mitigação. O registro é mantido como evidência de diligência e como insumo para revisão das práticas de publicação.

| Incidente | Natureza | Status |
| --- | --- | --- |
| [`INC-01`](#inc-01--link-de-compartilhamento-interno-com-token-de-acesso) | Link interno com token de acesso no histórico | ⚠️ URLs eliminadas na reescrita — revogação na origem pendente |
| [`INC-02`](#inc-02--identificação-nominal-de-integrantes-em-artefatos-versionados) | Identificação nominal de integrantes em artefatos versionados | ✅ Mitigado na árvore atual e no histórico alcançável |
| [`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix) | Identificação nominal residual no modelo embutido dos `.pbix` | ⚠️ Eliminado do repositório — regeneração e republicação pendentes |
| [`INC-04`](#inc-04--dados-pessoais-de-terceiros-no-histórico-do-repositório) | Dados pessoais de terceiros em extrações versionadas e no histórico | ✅ Mitigado na árvore atual e no histórico alcançável |
| [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) | Exposição residual não alcançada pelo `force push` | 🔲 Requer ação junto ao GitHub |
| [`INC-06`](#inc-06--exposição-em-issues-comentários-e-site-publicado) | Dados pessoais em issues e comentários; republicação em site público | 🔲 Requer ação junto ao GitHub |

### INC-01 — Link de compartilhamento interno com token de acesso

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-01` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Revisão de classificação e auditoria de conteúdo versionado |
| **Natureza** | Link de compartilhamento interno com token de acesso (`?e=`) publicado em arquivo versionado |
| **Artefato** | `dataset/.xls/readme.md` (removido da árvore atual na reestruturação e do histórico na [reescrita](#reescrita-do-histórico)) |
| **Origem do link** | OneDrive institucional (conta `@ifs.edu.br`) — arquivo `CONFREG.xlsx` |
| **Classificação do conteúdo** | 🟠 Restrito — planilha de controle da conformidade com potencial dado pessoal |
| **Amplitude** | Um único compartilhamento, referenciado em três formatos de URL |
| **Exposição na árvore atual** | Não — verificada ausência de URLs internas em todos os `.md` |
| **Exposição no histórico** | **Remediada em 16/09/2026.** As URLs dos dois arquivos afetados foram substituídas por `[link-interno-removido]` em todas as versões dos commits alcançáveis, e `dataset/.xls/readme.md` foi removido de todo o histórico. Ver [Reescrita do histórico](#reescrita-do-histórico) |
| **Decisão** | Reescrita do histórico com `git filter-repo` e `force push` sobre cópia integral do repositório, **e** revogação do compartilhamento na origem |
| **Status** | ⚠️ URLs eliminadas — revogação na origem pendente |

### Histórico da decisão

A primeira avaliação, registrada em 16/09/2026, foi **não** reescrever o histórico, por três razões:

1. **O token já é público há mais de dois anos.** Qualquer agente pode já tê-lo capturado; apagar o histórico não desfaz a exposição passada.
2. **A revogação na origem é a única mitigação efetiva.** Um link revogado deixa de conceder acesso independentemente de quem o possua.
3. **Custo de coordenação.** A reescrita invalida todos os SHAs, quebrando clones, *forks* e referências existentes.

A avaliação foi **revista em 16/09/2026**, quando a auditoria descrita em [`INC-04`](#inc-04--dados-pessoais-de-terceiros-no-histórico-do-repositório) evidenciou dados pessoais de terceiros no mesmo histórico. As razões 1 e 3 continuam verdadeiras, mas deixaram de ser decisivas: o ganho de segurança a partir da razão 2 **não se aplica** a arquivos que são, eles próprios, o dado. Prevaleceu a diretriz de interromper o acesso continuado e de não manter em repositório público conteúdo classificado como 🔴 Restrito.

### Ação de remediação requerida

A revogação na origem permanece necessária: a reescrita remove o link do repositório, mas não invalida o token já distribuído.

1. Acessar o OneDrive institucional (conta `@ifs.edu.br`).
2. Abrir **Compartilhados** → **Gerenciados por mim**.
3. Localizar o compartilhamento do arquivo `CONFREG.xlsx`.
4. Selecionar **Gerenciar acesso** e **remover** os vínculos do tipo *Qualquer pessoa com o link* e *Pessoas da instituição com o link*.
5. Confirmar que a planilha permanece acessível apenas aos proprietários legítimos.
6. Atualizar o `Status` deste registro para ✅ Concluído, com a data.

> **Recomendação permanente.** Links de compartilhamento institucional não devem ser versionados. Ao documentar uma fonte, registre o **sistema de origem** e a **forma de acesso institucional** — não a URL com token. Ver [fontes-de-dados.md](./fontes-de-dados.md).

### INC-02 — Identificação nominal de integrantes em artefatos versionados

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-02` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Revisão de classificação e auditoria de conteúdo versionado |
| **Natureza** | Nome próprio de integrante associado a métricas individuais de produtividade e a unidades gestoras, em repositório público |
| **Artefatos** | Documentação (`README.md`, `dashboard/README.md`, `docs/relatorios/analise-documental-2025.md`, `docs/unidades-gestoras.md`); coluna `servidor` das bases `.csv`/`.tsv`; células, listas de seleção e comentários dos arquivos `.xlsx` |
| **Classificação do conteúdo** | 🔴 Pessoal |
| **Amplitude** | Cinco integrantes; cerca de trinta mil registros na coluna `servidor` |
| **Causa raiz** | Ausência de política de minimização de dados pessoais na concepção do projeto. O repositório nasceu como artefato técnico de uso interno e passou a ser público sem revisão de classificação |
| **Decisão** | **Pseudonimizar** os integrantes por código `SRV-0N` em toda a documentação e nas bases redistribuídas, **preservando integralmente as métricas agregadas** para não comprometer a reprodutibilidade |
| **Exposição residual** | Histórico do Git — **remediada em 16/09/2026**: os nomes foram substituídos por código `SRV-0N` em todas as versões dos commits alcançáveis. Resíduo em [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |
| **Status** | ✅ Mitigado na árvore atual e no histórico alcançável |

**Nota sobre o método.** A substituição foi feita por **casamento de valor integral**, nunca por busca textual. Em um primeiro ensaio, uma substituição por expressão regular alterou registros de **pessoas alheias à equipe**: o prenome de um dos integrantes ocorre como nome intermediário de terceiros e em descrições de contratação nas planilhas. O ensaio foi integralmente descartado e refeito com correspondência exata. A verificação comparou as versões original e pseudonimizada parte a parte, confirmando que a diferença ficou restrita às células de identificação e que as contagens de registros e de valores permaneceram idênticas.

**Divergência entre decisão e execução.** A decisão inicial previa **remover** a coluna `servidor` das bases redistribuídas. A execução **manteve** a coluna, com os nomes substituídos por código: a remoção descaracterizaria a distribuição de carga de trabalho por unidade gestora, que é objeto da análise. A divergência fica registrada porque altera o conjunto de dados efetivamente publicado — a coluna existe, ainda que pseudonimizada.

> **Recomendação permanente.** A tabela de correspondência entre código e pessoa **não deve ser versionada**. Ela é mantida pelo responsável pelo tratamento dos dados, fora do controle de versão, e é o único artefato capaz de reverter a pseudonimização.

### INC-03 — Identificação nominal residual no modelo embutido dos `.pbix`

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-03` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Auditoria dos artefatos derivados após a pseudonimização das fontes |
| **Natureza** | Os arquivos `.pbix` embutem uma cópia do modelo de dados. Como a pseudonimização foi aplicada às fontes e aos artefatos de texto, os arquivos gerados antes dela mantêm a identificação nominal no modelo |
| **Artefatos** | Doze arquivos auditados em [`dashboard/pbix/`](../dashboard/pbix/): **dez** permanecem no repositório e **dois** foram retirados em 16/09/2026 |
| **Evidência** | Varredura parte a parte dos doze arquivos — e de todos os treze blobs `.pbix` do histórico —, nas codificações UTF-8 e UTF-16LE, independente de alinhamento de bytes e com cadeias de controle para estimar falso positivo. **Duas ocorrências reais:** `cgconfreg_v6.pbix` mantinha, no dicionário de strings do modelo embutido — armazenado sem compressão —, os prenomes de quatro integrantes (`SRV-01`, `SRV-02`, `SRV-04` e `SRV-05`) e o do autor; `cgconfreg_v8.pbix` mantinha, no layout do relatório, oito filtros cujo valor literal era o prenome de um integrante. Além disso, cinco arquivos nomeiam objetos do modelo com o prenome do autor (`Docs Victor`), o que é dado do próprio autor. As ocorrências em `impconfreg_csv_v4.pbix` e no modelo embutido de `cgconfreg_v8.4.pbix` são coincidências de sequência de bytes em conteúdo comprimido, não texto legível |
| **Classificação do conteúdo** | 🔴 Pessoal |
| **Amplitude** | Doze arquivos; **dois** continham identificação de terceiros. Os relatórios publicados no Power BI Service consomem o mesmo modelo e **não foram auditados** — a auditoria cobriu os artefatos versionados |
| **Causa raiz** | O modelo é interno ao formato `.pbix` e não é editável de forma segura sem reprocessamento do arquivo. A pseudonimização foi aplicada às fontes, que já não alimentam estes artefatos |
| **Decisão** | **Retirar** do repositório os artefatos com identificação de terceiros — a classificação 🔴 Restrito não admite conteúdo em repositório público — e **regenerar** os painéis a partir das bases pseudonimizadas, com republicação no workspace institucional, em substituição à edição direta do arquivo |
| **Ação executada** | `cgconfreg_v6.pbix` e `cgconfreg_v8.pbix` retirados da árvore e de todos os commits alcançáveis das três ramificações publicadas em 16/09/2026, sob qualquer caminho anterior, e preservados em armazenamento controlado com verificação de integridade. As versões de legado e as demais permanecem no repositório, sob classificação 🟠 Restrito. Resíduo alcançável pela referência de *pull request* `92` — ver [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |
| **Status** | ⚠️ Eliminado do repositório — regeneração e republicação pendentes |

> **Recomendação.** Enquanto a regeneração não for concluída, os artefatos `.pbix` que permanecem no repositório são classificados como 🟠 Restrito e os relatórios publicados não devem ser compartilhados com público externo. Regenerar é preferível a editar: além de eliminar a identificação, reconstrói o modelo a partir de uma fonte verificada. A regeneração é também a única medida capaz de alcançar os painéis publicados no Power BI Service, que têm a mesma origem dos artefatos retirados e não são afetados por nenhuma ação sobre o repositório.

### INC-04 — Dados pessoais de terceiros no histórico do repositório

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-04` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Auditoria de dados pessoais nos artefatos redistribuídos, posterior à pseudonimização dos integrantes |
| **Natureza** | Extrações versionadas em repositório público contendo identificação de pessoas alheias à equipe: beneficiários e favorecidos de pagamento, números com formato de CPF e endereços de e-mail institucional |
| **Artefatos** | `impconfreg_2023_v2_reitoria.xlsx`, `docs-victor-2025-02.xlsx`, `docs-victor-2025-03.xlsx`, `docs-victor-formatacao.tsv`, `docs-responsavel-2-formatacao.tsv` |
| **Classificação do conteúdo** | 🔴 Pessoal — dado de terceiros |
| **Amplitude** | Cinco arquivos; 83 CPFs formatados distintos no conjunto mais extenso; 313 sequências de 11 dígitos no mesmo arquivo |
| **Causa raiz** | A classificação inicial tratou como "dados operacionais" bases que contêm identificação de terceiros. A distinção entre identificação de integrantes e identificação de terceiros não havia sido feita, o que direcionou a primeira remediação apenas para os nomes da equipe |
| **Decisão** | **Segregar**, não pseudonimizar — o dado de terceiro é o objeto da análise de conformidade e perderia a função probatória se descaracterizado. Os cinco arquivos foram retirados do versionamento e movidos para armazenamento controlado, com os caminhos bloqueados no `.gitignore` |
| **Exposição na árvore atual** | Não — verificada a ausência de CPF e de e-mail nos quatro arquivos remanescentes |
| **Exposição no histórico** | **Remediada em 16/09/2026.** Os cinco arquivos foram removidos de todos os commits alcançáveis das três ramificações publicadas, junto com os artefatos de `dataset/.xls/`. Ver [Reescrita do histórico](#reescrita-do-histórico) |
| **Status** | ✅ Mitigado na árvore atual e no histórico alcançável — resíduo em [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |

### Reescrita do histórico

Executada em **16/09/2026** sobre as três ramificações publicadas — `main`, `79-impconfreg22nov23` e `CON-25-SIAFI-WEB` — e precedida de cópia integral do repositório (`git clone --mirror`), mantida até a conclusão da verificação. A operação exigiu quatro passes: cada passe foi seguido de auditoria dos objetos alcançáveis, e o resíduo identificado orientou o passe seguinte.

| Item | Conteúdo |
| --- | --- |
| **Ferramenta** | `git filter-repo` 2.47.0, aplicado sobre a cópia espelhada |
| **Passes executados** | Quatro passes sucessivos, todos em 16/09/2026. Cada passe seguinte foi orientado pela auditoria dos objetos ainda alcançáveis, que revelou caminhos históricos remanescentes — inclusive de arquivos que a árvore corrente mantém sob nome diferente |
| **Remoção de caminhos** | Os cinco arquivos do `INC-04`, os artefatos de `dataset/.xls/` e de `.github/python/`, `.vscode/impconfreg-HTMLK.zip`, `.vscode/impconfreg_2023 (version 2).xlsx`, `dataset/impconfreg_2023 (version 2).xlsx` e os dois artefatos do `INC-03` — `dashboard/cgconfreg_v6.pbix` e `dashboard/cgconfreg_v8.pbix` —, em qualquer versão e sob qualquer caminho anterior |
| **Substituição de identificadores** | Prenomes de integrantes e o nome do responsável, em toda versão de todo arquivo de texto, por código `SRV-0N`; URLs internas de compartilhamento por `[link-interno-removido]` |
| **Substituição de conteúdo binário** | Os arquivos binários foram preservados sem alteração, com uma exceção deliberada: `dataset/planilhas/impconfreg_2023_v2.xlsx` permanece na árvore corrente na forma pseudonimizada, mas suas versões históricas ainda continham a extração bruta. Como retirar o caminho também o retiraria da árvore corrente, as versões históricas receberam **os bytes sanitizados**, o que elimina o objeto bruto sem alterar o caminho nem o conteúdo publicado |
| **Preservação de terceiros** | A substituição operou por correspondência de valor integral. Prenomes que ocorrem como nome intermediário de terceiros ou em descrições de contratação não foram tocados; a auditoria confrontou as contagens antes e depois no histórico |
| **Autoria** | Preservada nas três ramificações (`main`: 103 commits; `79-impconfreg22nov23`: 44; `CON-25-SIAFI-WEB`: 85) |
| **Efeito no conjunto de dados corrente** | Nenhum conteúdo. As 44 entradas de arquivo da árvore corrente são idênticas, byte a byte, ao estado anterior à reescrita |
| **Efeito no histórico** | Os SHAs anteriores deixaram de ser alcançáveis; os commits que ficaram vazios com a remoção de caminhos foram descartados — `main`: 112 → 103, `79-impconfreg22nov23`: 50 → 44, `CON-25-SIAFI-WEB`: 98 → 85 |
| **Verificação** | Varredura dos 139 blobs alcançáveis das três ramificações: nenhum nome de terceiro, nenhum CPF válido, nenhum e-mail institucional, nenhuma URL interna e nenhum dos quatro blobs sensíveis identificados. A única ocorrência nominal remanescente é o prenome do autor, que é dado público por desenho |

**Limites da remediação.** O `force push` controla o que o repositório publica, não o que a plataforma retém:

1. **Objetos retidos pela plataforma.** O GitHub mantém commits antigos acessíveis por SHA direto até executar a própria coleta de lixo. Enquanto isso não ocorrer, quem conhecer o SHA ainda alcança o conteúdo original.
2. **Referências de *pull request*.** As referências `47` e `92` são mantidas pela plataforma e não são atualizadas por `force push` — ver [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push).

A alternativa de recriar o repositório a partir do estado atual permanece disponível e é a única forma de certeza absoluta, ao custo de descartar o histórico de desenvolvimento.

### INC-05 — Exposição residual não alcançada pelo `force push`

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-05` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Auditoria dos objetos remanescentes no repositório remoto após a reescrita do histórico |
| **Natureza** | Conteúdo pessoal ainda alcançável por canais que a reescrita e o `force push` não controlam |
| **Canais** | **Objetos retidos pela plataforma:** commits antigos acessíveis por SHA direto até a coleta de lixo do GitHub. **Referências de *pull request*:** `refs/pull/47/head` e `refs/pull/92/head`, mantidas pela plataforma |
| **Conteúdo alcançável** | Reconferido em 17/09/2026 por busca direta nos dois refs. O ref `47` alcança 26 commits e a identificação nominal de integrantes de `.github/python/teams.md`. O ref `92` alcança 84 commits — cópia congelada do `main` de 19/04/2025 — e ali são alcançáveis: a identificação nominal de integrantes em `.github/python/teams.md`; a versão **não pseudonimizada** de `dataset/.xls/impconfreg_2023 (version 2) - reitoria.csv` e `.tsv`, com o prenome do responsável na coluna `servidor` em 18.031 ocorrências; duas planilhas de formatação cujo nome de arquivo traz o prenome do autor e o de um integrante (`Docs * formatação.tsv`); e **três** dos quatro blobs sensíveis já eliminados da história das ramificações — o modelo embutido de `cgconfreg_v6.pbix`, a extração bruta `impconfreg_2023 (version 2).xlsx` (49.930 bytes) e `.vscode/impconfreg-HTMLK.zip`, cujas partes incluem a exportação `servidores.html`. Nenhum CPF com dígito verificador válido é alcançável por esses dois refs: o que os caracteriza é a identificação nominal |
| **Classificação do conteúdo** | 🔴 Pessoal — dado de terceiros |
| **Amplitude** | Dois refs de *pull request*, não alcançáveis a partir das ramificações publicadas. Os refs `2`, `3`, `5`, `6`, `45` e `46` foram auditados e não contêm ocorrências |
| **Causa raiz** | O `force push` substitui o conteúdo das ramificações, não dos objetos que a plataforma mantém por conta própria |
| **Mitigação pelo repositório** | Nenhuma |
| **Ação requerida** | Solicitar ao suporte do GitHub a remoção dos objetos órfãos e a exclusão definitiva das referências de *pull request*; alternativa de certeza absoluta: recriar o repositório a partir do estado atual |
| **Status** | 🔲 Requer ação junto ao GitHub |

> **Nota.** A exclusão de *pull requests* não é uma operação disponível ao mantenedor do repositório. Encerrar ou excluir a ramificação de origem não remove a referência; a remoção depende do suporte da plataforma.

> **Recomendação permanente.** Antes de versionar qualquer extração, aplicar a pergunta de triagem: *este arquivo contém identificação de alguém que não participou do projeto?* Se sim, a classificação é 🔴 Restrito e o arquivo não pertence ao versionamento.

---

### INC-06 — Exposição em issues, comentários e site publicado

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-06` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Auditoria das superfícies de publicação do repositório, estendida às issues, aos corpos de *pull request*, aos comentários e ao site publicado automaticamente |
| **Natureza** | Dados pessoais de terceiros e link interno com token de acesso publicados em conteúdo de discussão; republicação integral da árvore do repositório em site público |
| **Canais** | Corpo de issues e de *pull requests*, comentários de issues e site `github.io` do projeto, habilitado em 13/09/2023 |
| **Conteúdo alcançável** | Em três comentários de uma mesma issue, colagens de bases de trabalho do projeto — **dois deles com 70 CPFs válidos (69 distintos)**, além de grande volume de sequências numéricas com formato compatível com telefone e com CEP. Prenomes de integrantes em três corpos de issue e três comentários. Três endereços internos de compartilhamento, em dois corpos de issue e um comentário — **um deles com token de acesso** |
| **Classificação do conteúdo** | 🔴 Pessoal — dado de terceiros |
| **Amplitude** | 88 issues (incluindo *pull requests*), 122 comentários e 7 anexos de usuário de conteúdo não verificado |
| **Causa raiz** | Issues e comentários são superfície de **publicação**, não de versionamento: a reescrita com `git filter-repo` e o `force push` não os alcançam, e a exclusão é manual e item a item. O mesmo vale para o site publicado, que espelha a árvore do repositório |
| **Mitigação pelo repositório** | Nenhuma sobre o conteúdo já publicado. Controle preventivo: aviso de não anexar dados pessoais nos modelos de issue |
| **Ação requerida** | Exclusão dos comentários afetados e edição dos corpos de issue pelo proprietário, no navegador; revogação do compartilhamento do link com token na origem; solicitação ao suporte do GitHub da remoção das visualizações em cache e da exclusão dos anexos de usuário, que o mantenedor não pode excluir |
| **Status** | 🔲 Requer ação junto ao GitHub |

**Sobre o site publicado.** A auditoria verificou que a publicação corrente serve a árvore limpa — os artefatos retirados em `INC-04` não são mais acessíveis por esse canal — e que os artefatos de implantação têm **retenção de um dia**, de modo que a versão publicada antes da remoção já expirou e não é recuperável pela API da plataforma. Permanece, ainda assim, uma superfície de amplificação: todo conteúdo versionado, inclusive os `.pbix` do `INC-03`, é republicado sem autenticação e sujeito a indexação. Se o site não for necessário, desabilitá-lo reduz a superfície sem perda de conteúdo.

> **Regra derivada.** Antes de colar qualquer conteúdo em issue, comentário ou corpo de *pull request*, aplicar a mesma pergunta de triagem aplicada ao versionamento: *este conteúdo identifica alguém que não participou do projeto?* Não existe reescrita de histórico do lado da plataforma para conteúdo de discussão — a correção é sempre manual e posterior à exposição.

---

## Indicadores de governança

| Indicador | Fórmula | Meta |
| --- | --- | --- |
| Cobertura de catálogo | Fontes catalogadas ÷ fontes existentes | 100% |
| Cobertura de linhagem | Indicadores com linhagem documentada ÷ total | 100% |
| Aderência às regras de qualidade | Registros aprovados ÷ registros avaliados | ≥ 99% |
| Tempestividade da atualização | Atualizações dentro do prazo ÷ total de ciclos | ≥ 98% |
| Exposição de dados pessoais | Artefatos restritos publicados | 0 |
| Cobertura de pseudonimização | Artefatos com identificação nominal tratada ÷ artefatos com identificação nominal | 100% |
| Defasagem de pseudonimização | Bases com dado pessoal não tratado | 0 |
| Identificação nominal em artefatos derivados | Arquivos `.pbix` com prenome de terceiro no modelo embutido ou no layout do relatório | 0 |
| Arquivos com dados de terceiros versionados | Extrações versionadas contendo CPF, nome de favorecido ou e-mail institucional | 0 |
| Recuperabilidade histórica de dados pessoais | Incidentes de exposição cujo conteúdo permanece recuperável nas ramificações publicadas | 0 |
| Exposição residual por referências de *pull request* | Referências de *pull request* com conteúdo pessoal alcançável | 0 |
| Links internos versionados | URLs com token de acesso presentes em artefatos versionados | 0 |
| Incidentes de exposição abertos | Incidentes com status diferente de concluído | 0 |
| Dados pessoais em conteúdo de discussão | Itens de discussão (issue, *pull request* ou comentário) com dado pessoal de terceiros | 0 |
| Visibilidade externa do conteúdo versionado | Superfícies públicas que republicam a árvore do repositório | 1 (somente o repositório) |

**Medição de 16/09/2026.** Valores apurados para os indicadores de exposição:

| Indicador | Valor apurado | Situação |
| --- | --- | --- |
| Identificação nominal em artefatos derivados | **0** de **10** arquivos `.pbix` no repositório — **2** retirados em 16/09/2026 | ⚠️ [`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix) |
| Exposição residual por referências de *pull request* | **2** de 8 referências | 🔲 [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |
| Recuperabilidade histórica de dados pessoais | **0** nas três ramificações publicadas, em **139** blobs auditados; resíduo nominal em `refs/pull/47/head` e `refs/pull/92/head` — **0** CPF válido alcançável por esses refs — e em objetos retidos pela plataforma | 🔲 [`INC-05`](#inc-05--exposição-residual-não-alcançada-pelo-force-push) |
| Eliminação de blobs sensíveis do histórico | **4** de **4** blobs identificados, eliminados ou substituídos nas ramificações publicadas | ✅ |
| Links internos versionados | 0 — árvore atual e histórico alcançável | ✅ |
| Arquivos com dados de terceiros versionados | 0 — quatro arquivos remanescentes auditados | ✅ |
| Defasagem de pseudonimização | 0 nas bases redistribuídas | ✅ |
| Exposição de dados pessoais | **10** artefatos 🟠 Restrito versionados; **2** retirados por identificação de terceiros | ⚠️ [`INC-03`](#inc-03--identificação-nominal-residual-no-modelo-embutido-dos-pbix) |
| Incidentes de exposição abertos | **4** (`INC-01`, `INC-03`, `INC-05`, `INC-06`) | 🔲 |
| Dados pessoais em conteúdo de discussão | **70 CPFs válidos em 2 comentários**; prenomes de integrantes em **6** itens de discussão; **3** endereços internos, um deles com token | 🔲 [`INC-06`](#inc-06--exposição-em-issues-comentários-e-site-publicado) |
| Visibilidade externa do conteúdo versionado | **2** — repositório e site publicado | 🔲 [`INC-06`](#inc-06--exposição-em-issues-comentários-e-site-publicado) |

Os demais indicadores dependem de medição sobre a operação corrente e ainda não possuem série histórica.

---

## Roteiro de maturidade

```text
Nível 1 — Inicial        Documentação dispersa; qualidade verificada manualmente.
Nível 2 — Gerenciado     Fontes catalogadas; papéis definidos; regras de qualidade documentadas.
Nível 3 — Definido       Regras de qualidade implantadas; linhagem estruturada; classificação aplicada.
Nível 4 — Medido         Indicadores de governança monitorados; acesso controlado por perfil.
Nível 5 — Otimizado      Validação automatizada; alertas proativos; melhoria contínua.
```

**Posição atual:** transição do **Nível 1** para o **Nível 2**, com o catálogo de fontes e a definição de papéis formalizados neste diretório.

### Ações prioritárias

1. Excluir os comentários com dados pessoais e editar os corpos de issue afetados, e desabilitar o site publicado caso ele não seja necessário (`INC-06`).
2. Revogar o compartilhamento do arquivo `CONFREG.xlsx` na origem (`INC-01`).
3. Solicitar ao suporte do GitHub a remoção dos objetos retidos, a exclusão definitiva das referências de *pull request* `47` e `92`, a remoção das visualizações em cache e a exclusão dos anexos de usuário (`INC-05`, `INC-06`) — única ação capaz de eliminar o resíduo que o `force push` não alcança.
4. Regenerar os painéis a partir das bases pseudonimizadas, revisando os filtros que usavam prenome como valor literal, e repor os artefatos retirados (`INC-03`) — a edição direta do `.pbix` não é segura, e os painéis publicados no Power BI Service só se tornam alcançáveis por essa via.
5. Revisar a classificação e a exposição dos artefatos restritos.
6. Implantar as regras de validação `R01`–`R07` na camada de ingestão.
7. Formalizar o catálogo de dados com responsáveis nomeados.
8. Implantar segurança em nível de linha nos painéis publicados.
9. Estabelecer a triagem de dados de terceiros como etapa obrigatória antes de qualquer versionamento e antes de qualquer publicação em issue, comentário ou *pull request*.

---

## Referências

- **Lei nº 13.709/2018** — Lei Geral de Proteção de Dados Pessoais (LGPD).
- **Lei nº 12.527/2011** — Lei de Acesso à Informação.
- **Instrução Normativa RFB nº 1.234/2012** — retenção de tributos sobre pagamentos pela administração pública federal.
- **Manual de Procedimentos para a Conformidade de Registro de Gestão — IFS.**
- **Normativos da Controladoria-Geral da União** aplicáveis à conformidade de registro de gestão e aos atos de gestão.
- **DAMA International — DAMA-DMBOK: Data Management Body of Knowledge** (dimensões de qualidade de dados e áreas de governança).

---

## Documentos relacionados

- [arquitetura.md](./arquitetura.md) — arquitetura da solução e limitações conhecidas
- [fontes-de-dados.md](./fontes-de-dados.md) — catálogo das fontes de dados
- [unidades-gestoras.md](./unidades-gestoras.md) — unidades gestoras e responsáveis
- [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) — modelo relacional proposto
- [CONTRIBUTING.md](../CONTRIBUTING.md) — política de dados para contribuições
