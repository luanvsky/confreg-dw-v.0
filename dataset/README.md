# Conjuntos de Dados

Repositório de arquivos analíticos, extrações e imagens utilizados no projeto de **Conformidade de Registro de Gestão**. Este diretório é a **camada de dados versionada** do projeto: contém recortes utilizados para estudo, conferência e desenvolvimento do modelo, e **não** a base operacional em produção.

A base operacional é a planilha de controle colaborativa mantida pela equipe de conformidade, documentada em [../docs/fontes-de-dados.md](../docs/fontes-de-dados.md).

---

## Sumário

- [Organização do diretório](#organização-do-diretório)
- [Inventário de arquivos](#inventário-de-arquivos)
- [Classificação e uso](#classificação-e-uso)
- [Convenção de nomenclatura](#convenção-de-nomenclatura)
- [Como abrir os arquivos](#como-abrir-os-arquivos)
- [Pendências](#pendências)
- [Documentos relacionados](#documentos-relacionados)

---

## Organização do diretório

```text
dataset/
├── planilhas/    # Extrações analíticas e bases de trabalho
├── imagens/      # Imagens e capturas usadas na documentação
└── README.md
```

As antigas pastas ocultas `.xls/`, `.jpg/` e `.pbi/` foram eliminadas: nomes iniciados por ponto não são legíveis nem navegáveis em contexto de dados, o que dificultava a descoberta dos arquivos e a própria governança do acervo.

Os arquivos `.pbix` que estavam em `.pbi/` foram consolidados em [`../dashboard/pbix/`](../dashboard/pbix/), junto dos demais artefatos de Power BI.

---

## Inventário de arquivos

### `planilhas/` — extrações e bases de trabalho

| Arquivo | Descrição | Formato | Período | Classificação |
| --- | --- | --- | --- | --- |
| [`impconfreg_2023_v2.xlsx`](./planilhas/impconfreg_2023_v2.xlsx) | Base consolidada de conformidade — extração principal; identificação de integrantes pseudonimizada | `.xlsx` | 2023 | 🟠 Restrito |
| [`impconfreg_2023_v2_geral.tsv`](./planilhas/impconfreg_2023_v2_geral.tsv) | Recorte consolidado geral em texto delimitado — agregação por tipo de documento, sem identificação pessoal | `.tsv` | 2023 | 🟡 Interno |
| [`impconfreg_2023_v2_reitoria.csv`](./planilhas/impconfreg_2023_v2_reitoria.csv) | Recorte da unidade gestora Reitoria; coluna `servidor` pseudonimizada | `.csv` | 2023 | 🟠 Restrito |
| [`impconfreg_2023_v2_reitoria.tsv`](./planilhas/impconfreg_2023_v2_reitoria.tsv) | Recorte da unidade gestora Reitoria; coluna `servidor` pseudonimizada | `.tsv` | 2023 | 🟠 Restrito |

### Retirados do repositório — armazenamento controlado

Cinco arquivos foram **removidos do versionamento em 16/09/2026** por conterem dados pessoais de terceiros (identificação de beneficiários e favorecidos, números com formato de CPF e endereços de e-mail institucional). Eles existem apenas fora da árvore de trabalho, em armazenamento controlado.

| Arquivo retirado | Dados pessoais identificados |
| --- | --- |
| `impconfreg_2023_v2_reitoria.xlsx` | ~83 CPFs formatados distintos; ~313 sequências de 11 dígitos; 2 e-mails institucionais |
| `docs-victor-2025-02.xlsx` | 4 CPFs formatados; coluna `Favorecido Doc.`; ~156 sequências de 11 dígitos |
| `docs-victor-2025-03.xlsx` | 5 CPFs formatados; coluna `Favorecido Doc.`; ~119 sequências de 11 dígitos |
| `docs-victor-formatacao.tsv` | 5 CPFs formatados; coluna `Favorecido Doc.` |
| `docs-responsavel-2-formatacao.tsv` | 5 CPFs formatados |

Os contadores são **distintos** e resultam de varredura por expressão regular sobre o conteúdo textual dos arquivos, não de conferência nominal caso a caso. Hashes SHA-256 de integridade e regras de uso constam do leitor do diretório de armazenamento.

O `.gitignore` mantém os caminhos bloqueados, impedindo que retornem por engano ao versionamento. Detalhes do controle em [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md#dados-pessoais-de-terceiros).

> ✅ **Situação em 16/09/2026.** Os cinco arquivos foram removidos **da árvore atual e de todo o histórico alcançável** das ramificações publicadas, por reescrita de histórico com `git filter-repo` e `force push` sobre cópia integral do repositório. Permanecem recuperáveis apenas por canais que a plataforma mantém fora do alcance do `force push` — ver [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md#inc-05--exposição-residual-não-alcançada-pelo-force-push).


### `imagens/` — recursos de documentação

| Arquivo | Descrição | Classificação |
| --- | --- | --- |
| [`cgconfreg.png`](./imagens/cgconfreg.png) | Captura de tela do painel de conformidade | 🟢 Público |
| [`verde.jpg`](./imagens/verde.jpg) | Recurso visual de apoio à documentação | 🟢 Público |

### Convenções de duplicidade

Os recortes `impconfreg_2023_v2*` foram mantidos em três extensões (`xlsx`, `csv`, `tsv`) por questões de compatibilidade das ferramentas de análise utilizadas. Trata-se de **redundância deliberada**, não de conteúdo distinto: o mesmo recorte em extensões diferentes — e, no caso de `reitoria.csv` e `reitoria.tsv`, de **duplicatas byte a byte** com separador idêntico (ver [Divergência entre extensão e formato](#divergência-entre-extensão-e-formato)).

> **Nota.** Durante a reorganização do acervo foi identificada uma **duplicata byte a byte** de `impconfreg_csv_v4.pbix`, que existia simultaneamente em duas pastas. A cópia excedente foi removida e o arquivo passou a ter um único local em [`../dashboard/pbix/`](../dashboard/pbix/).

### Divergência entre extensão e formato

A extensão `.tsv` deste acervo **não é um indicador confiável de formato**. Entre os arquivos que permanecem versionados:

| Arquivo | Extensão | Formato real | Observação |
| --- | --- | --- | --- |
| [`impconfreg_2023_v2_reitoria.tsv`](./planilhas/impconfreg_2023_v2_reitoria.tsv) | `.tsv` | Texto **separado por vírgula** | Não contém nenhum caractere de tabulação; é uma duplicata byte a byte do `.csv` correspondente. |
| [`impconfreg_2023_v2_geral.tsv`](./planilhas/impconfreg_2023_v2_geral.tsv) | `.tsv` | Texto separado por tabulação | Formato coerente com a extensão. |

Dois arquivos hoje em armazenamento controlado (`docs-victor-formatacao.tsv` e `docs-responsavel-2-formatacao.tsv`) eram, na verdade, **pastas compactadas `.xlsx`** exportadas com extensão incorreta. Como deixaram de ser versionados, a leitura por `pandas.read_csv` deixou de ser um risco no repositório — mas o histórico do Git preserva essa ambiguidade.

Como regra geral, inspecione o separador antes de carregar qualquer arquivo deste diretório.


---

## Classificação e uso

| Nível | Arquivos | Tratamento |
| --- | --- | --- |
| 🟢 **Público** | Imagens | Uso livre |
| 🟡 **Interno** | Agregações consolidadas | Uso restrito a atividades de conformidade; não redistribuir sem revisão |
| 🟠 **Restrito** | Recortes de conformidade | Acesso restrito; a identificação dos integrantes foi pseudonimizada (`SRV-0N`) |
| 🔴 **Restrito — dados pessoais de terceiros** | Fora do repositório | Não versionado; armazenamento controlado com acesso nominal |

> ✅ **Minimização aplicada.** A coluna `servidor` e o texto livre de observação dos recortes `impconfreg_2023_v2_reitoria.*` foram **pseudonimizados**: os nomes foram substituídos pelos códigos `SRV-01` a `SRV-05`, e as métricas agregadas foram preservadas integralmente. A tabela de correspondência entre código e pessoa **não é versionada** — procedimento em [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md#pseudonimização-e-minimização).

> ✅ **Segregação aplicada.** Os arquivos com identificação de terceiros foram **retirados do versionamento** e mantidos fora da árvore de trabalho. Os quatro arquivos que permanecem no diretório foram verificados e **não contêm CPF nem endereço de e-mail**.

Nenhum arquivo deste diretório está coberto pela licença MIT do software — os dados permanecem sujeitos às restrições institucionais de origem. Consulte [../LICENSE](../LICENSE).

---

## Convenção de nomenclatura

| Elemento | Padrão | Exemplo |
| --- | --- | --- |
| Base principal | `<origem>_<ano>_v<N>` | `impconfreg_2023_v2.xlsx` |
| Recorte por unidade | `<base>_<unidade>` | `impconfreg_2023_v2_reitoria.csv` |
| Recorte consolidado | `<base>_geral` | `impconfreg_2023_v2_geral.tsv` |
| Extração mensal | `docs-<responsavel>-<AAAA-MM>` | `docs-<responsavel>-2025-02.xlsx` |

O padrão completo, com as regras aplicáveis a todo o repositório, está em [../CONTRIBUTING.md](../CONTRIBUTING.md). As extrações mensais seguem o padrão de nome, porém não são versionadas — ver [Retirados do repositório](#retirados-do-repositório--armazenamento-controlado).

---

## Como abrir os arquivos

```bash
# Ler uma extração em TSV preservando os tipos originais
python -c "import pandas as pd; print(pd.read_csv('dataset/planilhas/impconfreg_2023_v2_geral.tsv', sep='\t', dtype=str).head())"

# Ler uma extração em Excel
python -c "import pandas as pd; print(pd.read_excel('dataset/planilhas/impconfreg_2023_v2.xlsx').head())"
```

O caderno [`../notebooks/impconfreg.ipynb`](../notebooks/impconfreg.ipynb) contém a análise exploratória inicial da estrutura dessas bases.

---

## Pendências

- [ ] **Incluir a base `v8` e o arquivo `confreg.txt.xlsx`** — pendência herdada do acervo original.
- [ ] **Documentar o dicionário de dados das extrações** — descrição de cada coluna, tipo e regra de preenchimento (previsto em [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md)).
- [x] **Substituir a coluna `servidor` por código identificador** nos recortes destinados a compartilhamento — concluído em 16/09/2026, com os códigos `SRV-01` a `SRV-05`.
- [x] **Retirar do versionamento os arquivos com dados pessoais de terceiros** — concluído em 16/09/2026; cinco arquivos movidos para armazenamento controlado externo e caminhos bloqueados no `.gitignore`.
- [x] **Reescrever o histórico do Git** — concluído em 16/09/2026 com `git filter-repo` e `force push` sobre as três ramificações, após cópia integral do repositório. Restam os objetos retidos pela plataforma e as referências de *pull request* `47` e `92`, que o `force push` não alcança — ver `INC-05` em [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md#inc-05--exposição-residual-não-alcançada-pelo-force-push).
- [ ] **Corrigir a extensão de `impconfreg_2023_v2_reitoria.tsv`** — o arquivo é separado por vírgula, não por tabulação.
- [ ] **Avaliar a consolidação dos formatos duplicados** (`csv`/`tsv`) em um formato único com script de conversão versionado.

---

## Documentos relacionados

- [../docs/fontes-de-dados.md](../docs/fontes-de-dados.md) — catálogo de fontes e política de acesso
- [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md) — classificação, qualidade e privacidade
- [../docs/modelo-de-dados-mysql.md](../docs/modelo-de-dados-mysql.md) — modelo relacional proposto
- [../dashboard/README.md](../dashboard/README.md) — painéis e versões
- [../CONTRIBUTING.md](../CONTRIBUTING.md) — padrões de contribuição e política de dados
