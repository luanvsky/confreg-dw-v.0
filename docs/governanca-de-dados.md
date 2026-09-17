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
| `dashboard/pbix/*.pbix` | 🟢 Público | Não contêm dados embutidos com informação pessoal além do necessário à demonstração |
| `dashboard/README.md`, `docs/arquitetura.md` | 🟢 Público | Documentação técnica |
| `dataset/planilhas/impconfreg_2023_v2_*.csv/.tsv` | 🟠 Restrito | Contêm coluna `servidor` com identificação pessoal — **requer anonimização antes de qualquer redistribuição** |
| `dataset/planilhas/*.xlsx` | 🟡 Interno | Bases de trabalho da equipe |
| `docs/relatorios/analise-documental-2025.md` | 🟠 Restrito | Apresenta produtividade nominal por servidor |
| `docs/unidades-gestoras.md` | 🟠 Restrito | Associa unidades gestoras a pessoas responsáveis |
| `docs/termo-referencia-aquisicao-bi.md` | 🟡 Interno | Documento administrativo de contratação |
| `apps/**` | 🟢 Público | Código-fonte de protótipos |

> **Recomendação.** Os artefatos classificados como 🟠 Restrito devem ser movidos para armazenamento institucional controlado ou anonimizados. Enquanto permanecerem neste repositório público, o acesso deve ser tratado como já divulgado, com registro da decisão.

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
| `servidor` | texto | Sim | Responsável pela análise de conformidade | **Dado pessoal — sujeito a anonimização** |
| `data` | data | Sim | Data da análise | Formato `dd/mm/aaaa`, não futura |
| `unidade_gestora` | texto/código | Sim | Unidade responsável pelo registro | Deve constar na lista oficial de unidades |
| `situacao` | texto | Sim | Resultado da análise | Domínio: `SEM RESTRIÇÃO` ou `COM RESTRIÇÃO` |
| `codigo_restricao` | texto | Condicional | Código que caracteriza a restrição | Obrigatório quando `situacao = COM RESTRIÇÃO` |

---

## Privacidade e proteção de dados pessoais

O projeto trata dados pessoais de servidores públicos envolvidos na análise de conformidade. A observância à **Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)** é requisito do projeto, não opção.

### Dados pessoais identificados

| Dado | Finalidade | Necessário? | Tratamento recomendado |
| --- | --- | --- | --- |
| Nome do servidor responsável pela análise | Distribuição de carga de trabalho e acompanhamento de produtividade | Sim, para fins de gestão | Substituir por código identificador (`SRV-001`) e manter o dicionário de correspondência fora do repositório |
| E-mail institucional | Contato operacional | Não no repositório público | Remover de artefatos versionados |
| Identificação de unidade gestora | Análise por unidade | Sim | Manter |

### Medidas adotadas e recomendadas

- **Minimização:** os painéis expõem indicadores agregados, não registros individuais.
- **Anonimização na publicação:** o campo `servidor` deve ser substituído por código antes de qualquer redistribuição das bases.
- **Controle de finalidade:** o uso dos dados é restrito à análise de conformidade e à gestão da força de trabalho.
- **Revisão de exposição:** artefatos classificados como 🟠 Restrito não deveriam ser mantidos em repositório público.
- **Registro de decisão:** toda divulgação externa deve ser precedida de avaliação formal.

> **Alerta de conformidade.** A presença de nomes de servidores e de métricas individuais de produtividade em repositório público caracteriza exposição de dados pessoais. Recomenda-se a anonimização imediata das bases redistribuídas e a revisão dos documentos [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md) e [unidades-gestoras.md](./unidades-gestoras.md).

---

## Segurança e controle de acesso

| Controle | Descrição | Situação |
| --- | --- | --- |
| **Workspace dedicado** | Publicação dos painéis em workspace institucional próprio | ✅ |
| **Segurança em nível de linha (RLS)** | Restringir a visão por unidade gestora, conforme o perfil do usuário | 🔲 Proposto |
| **Perfis de acesso** | Diferenciação entre administrador, curador e consumidor | 🔲 Proposto |
| **Atualização agendada monitorada** | Verificação diária da atualização do conjunto de dados | ✅ |
| **Links públicos controlados** | Publicação apenas de conteúdos classificados como 🟢 Público | ⚠️ Requer revisão |
| **Gestão de credenciais e links compartilhados** | Nenhuma credencial, token ou link interno versionado | ⚠️ Incidente `INC-01` identificado no histórico — ver [Registro de incidentes](#registro-de-incidentes-de-exposição) |

---

## Riscos e controles

| # | Risco | Probabilidade | Impacto | Controle |
| --- | --- | --- | --- | --- |
| R1 | Indicador incorreto utilizado em decisão de gestão | Média | Alto | Conferência de totais contra a origem; versionamento dos `.pbix` |
| R2 | Exposição de dados pessoais em repositório público | Alta | Alto | Anonimização e revisão de classificação |
| R3 | Quebra da consulta por alteração da estrutura da planilha | Média | Médio | Monitoramento diário; padronização de colunas |
| R4 | Duplicidade de registros inflando indicadores | Média | Alto | Regra de unicidade `R02` |
| R5 | Falha silenciosa na atualização agendada | Média | Alto | Verificação diária do status de atualização |
| R6 | Perda da linhagem por rotatividade da equipe | Alta | Médio | Documentação neste diretório e no catálogo |
| R7 | Divergência entre painel publicado e versão do `.pbix` | Média | Médio | Correspondência de identificadores de versão ([CONTRIBUTING.md](../CONTRIBUTING.md)) |
| R8 | Dependência de pessoa única (*bus factor*) | Alta | Médio | Versionamento em Git e documentação do processo |
| R9 | Link de compartilhamento interno com token de acesso exposto em histórico de repositório público | Média | Alto | Revogação do compartilhamento na origem; proibição de versionar URLs internas ([CONTRIBUTING.md](../CONTRIBUTING.md)) |

---

## Registro de incidentes de exposição

Registro das ocorrências de exposição de informação identificadas no repositório, com a respectiva mitigação. O registro é mantido como evidência de diligência e como insumo para revisão das práticas de publicação.

| Campo | Conteúdo |
| --- | --- |
| **Identificador** | `INC-01` |
| **Data de detecção** | 16/09/2026 |
| **Detectado por** | Revisão de classificação e auditoria de conteúdo versionado |
| **Natureza** | Link de compartilhamento interno com token de acesso (`?e=`) publicado em arquivo versionado |
| **Artefato** | `dataset/.xls/readme.md` (removido da árvore atual na reestruturação; permanece no histórico) |
| **Origem do link** | `[link-interno-removido]` — arquivo `CONFREG.xlsx` |
| **Classificação do conteúdo** | 🟠 Restrito — planilha de controle da conformidade com potencial dado pessoal |
| **Amplitude** | Um único compartilhamento, referenciado em três formatos de URL |
| **Exposição na árvore atual** | Não — verificada ausência de URLs internas em todos os `.md` |
| **Exposição no histórico** | Sim — commits anteriores a `bcf3fb0` |
| **Decisão** | Revogar o compartilhamento na origem; **não** reescrever o histórico |
| **Status** | 🔲 Aguardando revogação na origem |

### Justificativa da decisão

A reescrita do histórico (`git filter-repo` + *force push*) foi **descartada** por três razões:

1. **O token já é público há mais de dois anos.** Qualquer agente pode já tê-lo capturado; apagar o histórico não desfaz a exposição passada.
2. **A revogação na origem é a única mitigação efetiva.** Um link revogado deixa de conceder acesso independentemente de quem o possua.
3. **Custo de coordenação.** A reescrita invalida todos os SHAs, quebrando clones, *forks* e referências existentes, sem ganho de segurança proporcional.

### Ação de remediação requerida

1. Acessar o OneDrive institucional (conta `@ifs.edu.br`).
2. Abrir **Compartilhados** → **Gerenciados por mim**.
3. Localizar o compartilhamento do arquivo `CONFREG.xlsx`.
4. Selecionar **Gerenciar acesso** e **remover** os vínculos do tipo *Qualquer pessoa com o link* e *Pessoas da instituição com o link*.
5. Confirmar que a planilha permanece acessível apenas aos proprietários legítimos.
6. Atualizar o `Status` deste registro para ✅ Concluído, com a data.

> **Recomendação permanente.** Links de compartilhamento institucional não devem ser versionados. Ao documentar uma fonte, registre o **sistema de origem** e a **forma de acesso institucional** — não a URL com token. Ver [fontes-de-dados.md](./fontes-de-dados.md).

---

## Indicadores de governança

| Indicador | Fórmula | Meta |
| --- | --- | --- |
| Cobertura de catálogo | Fontes catalogadas ÷ fontes existentes | 100% |
| Cobertura de linhagem | Indicadores com linhagem documentada ÷ total | 100% |
| Aderência às regras de qualidade | Registros aprovados ÷ registros avaliados | ≥ 99% |
| Tempestividade da atualização | Atualizações dentro do prazo ÷ total de ciclos | ≥ 98% |
| Exposição de dados pessoais | Artefatos restritos publicados | 0 |
| Defasagem de anonimização | Bases com dado pessoal não tratado | 0 |
| Links internos versionados | URLs com token de acesso presentes em artefatos versionados | 0 |
| Incidentes de exposição abertos | Incidentes com status diferente de concluído | 0 |

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

1. Revogar o compartilhamento do arquivo `CONFREG.xlsx` na origem (incidente `INC-01`).
2. Anonimizar o campo `servidor` nas bases redistribuídas.
3. Revisar a classificação e a exposição dos artefatos restritos.
4. Implantar as regras de validação `R01`–`R07` na camada de ingestão.
5. Formalizar o catálogo de dados com responsáveis nomeados.
6. Implantar segurança em nível de linha nos painéis publicados.

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
