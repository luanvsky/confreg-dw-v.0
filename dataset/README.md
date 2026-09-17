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
| [`impconfreg_2023_v2.xlsx`](./planilhas/impconfreg_2023_v2.xlsx) | Base consolidada de conformidade — extração principal | `.xlsx` | 2023 | 🟡 Interno |
| [`impconfreg_2023_v2_geral.tsv`](./planilhas/impconfreg_2023_v2_geral.tsv) | Recorte consolidado geral em texto delimitado | `.tsv` | 2023 | 🟠 Restrito |
| [`impconfreg_2023_v2_reitoria.xlsx`](./planilhas/impconfreg_2023_v2_reitoria.xlsx) | Recorte da unidade gestora Reitoria | `.xlsx` | 2023 | 🟠 Restrito |
| [`impconfreg_2023_v2_reitoria.csv`](./planilhas/impconfreg_2023_v2_reitoria.csv) | Recorte da unidade gestora Reitoria | `.csv` | 2023 | 🟠 Restrito |
| [`impconfreg_2023_v2_reitoria.tsv`](./planilhas/impconfreg_2023_v2_reitoria.tsv) | Recorte da unidade gestora Reitoria | `.tsv` | 2023 | 🟠 Restrito |
| [`docs-victor-formatacao.tsv`](./planilhas/docs-victor-formatacao.tsv) | Base de trabalho para padronização de formatação | `.tsv` | — | 🟠 Restrito |
| [`docs-responsavel-2-formatacao.tsv`](./planilhas/docs-responsavel-2-formatacao.tsv) | Base de trabalho para padronização de formatação | `.tsv` | — | 🟠 Restrito |
| [`docs-victor-2025-02.xlsx`](./planilhas/docs-victor-2025-02.xlsx) | Extração mensal de acompanhamento | `.xlsx` | Fev/2025 | 🟡 Interno |
| [`docs-victor-2025-03.xlsx`](./planilhas/docs-victor-2025-03.xlsx) | Extração mensal de acompanhamento | `.xlsx` | Mar/2025 | 🟡 Interno |

### `imagens/` — recursos de documentação

| Arquivo | Descrição | Classificação |
| --- | --- | --- |
| [`cgconfreg.png`](./imagens/cgconfreg.png) | Captura de tela do painel de conformidade | 🟢 Público |
| [`verde.jpg`](./imagens/verde.jpg) | Recurso visual de apoio à documentação | 🟢 Público |

### Convenções de duplicidade

Os recortes `impconfreg_2023_v2*` foram mantidos em três formatos (`xlsx`, `csv`, `tsv`) por questões de compatibilidade das ferramentas de análise utilizadas. Trata-se de **redundância deliberada de formato**, não de conteúdo distinto: o mesmo recorte em formatos diferentes.

> **Nota.** Durante a reorganização do acervo foi identificada uma **duplicata byte a byte** de `impconfreg_csv_v4.pbix`, que existia simultaneamente em duas pastas. A cópia excedente foi removida e o arquivo passou a ter um único local em [`../dashboard/pbix/`](../dashboard/pbix/).

---

## Classificação e uso

| Nível | Arquivos | Tratamento |
| --- | --- | --- |
| 🟢 **Público** | Imagens | Uso livre |
| 🟡 **Interno** | Bases consolidadas e recortes mensais | Uso restrito a atividades de conformidade; não redistribuir sem revisão |
| 🟠 **Restrito** | Recortes com identificação de servidor | Acesso nominal; exige anonimização antes de qualquer compartilhamento |

> ⚠️ **Atenção.** Os recortes `impconfreg_2023_v2*` contêm a coluna `servidor`, com identificação pessoal (por exemplo, o cabeçalho `documento,numero,servidor,data,,` seguido de registros individuais). Trate-os como **dado pessoal** sob a LGPD: antes de reutilizar ou publicar, substitua o nome por um código identificador. Procedimento em [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md).

Nenhum arquivo deste diretório está coberto pela licença MIT do software — os dados permanecem sujeitos às restrições institucionais de origem. Consulte [../LICENSE](../LICENSE).

---

## Convenção de nomenclatura

| Elemento | Padrão | Exemplo |
| --- | --- | --- |
| Base principal | `<origem>_<ano>_v<N>` | `impconfreg_2023_v2.xlsx` |
| Recorte por unidade | `<base>_<unidade>` | `impconfreg_2023_v2_reitoria.csv` |
| Recorte consolidado | `<base>_geral` | `impconfreg_2023_v2_geral.tsv` |
| Extração mensal | `docs-<responsavel>-<AAAA-MM>` | `docs-victor-2025-02.xlsx` |

O padrão completo, com as regras aplicáveis a todo o repositório, está em [../CONTRIBUTING.md](../CONTRIBUTING.md).

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
- [ ] **Substituir a coluna `servidor` por código identificador** nos recortes destinados a compartilhamento.
- [ ] **Avaliar a consolidação dos formatos duplicados** (`xlsx`/`csv`/`tsv`) em um formato único com script de conversão versionado.

---

## Documentos relacionados

- [../docs/fontes-de-dados.md](../docs/fontes-de-dados.md) — catálogo de fontes e política de acesso
- [../docs/governanca-de-dados.md](../docs/governanca-de-dados.md) — classificação, qualidade e privacidade
- [../docs/modelo-de-dados-mysql.md](../docs/modelo-de-dados-mysql.md) — modelo relacional proposto
- [../dashboard/README.md](../dashboard/README.md) — painéis e versões
- [../CONTRIBUTING.md](../CONTRIBUTING.md) — padrões de contribuição e política de dados
