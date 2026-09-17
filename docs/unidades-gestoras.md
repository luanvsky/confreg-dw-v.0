# Unidades Gestoras

Mapeamento das unidades gestoras abrangidas pela rotina de conformidade de registro de gestão e dos responsáveis pela análise de cada uma.

---

> ⚠️ **DOCUMENTO COM DADOS PESSOAIS PSEUDONIMIZADOS**
>
> Este documento associa **códigos de unidade gestora a integrantes identificados por código
> pseudônimo** (`SRV-01` a `SRV-05`). A tabela de correspondência entre código e pessoa **não
> é versionada neste repositório**.
>
> A associação remanescente configura dado pessoal na acepção da Lei nº 13.709/2018 (LGPD),
> pois permite identificar indiretamente um indivíduo quando combinada com outras bases.
> **Antes de reutilizar ou compartilhar:** limite a circulação ao escopo das atividades de
> conformidade.
>
> Classificação: 🟠 **Restrito** — ver [governança de dados](./governanca-de-dados.md#privacidade-e-proteção-de-dados-pessoais).

---

## Sumário

- [Contexto](#contexto)
- [Mapeamento](#mapeamento)
- [Distribuição da carga de análise](#distribuição-da-carga-de-análise)
- [Convenções de identificação](#convenções-de-identificação)
- [Documentos relacionados](#documentos-relacionados)

---

## Contexto

A conformidade de registro de gestão é apurada **por unidade gestora**. O código da unidade (formato `23xxx`) é o atributo que segmenta as análises, os indicadores do painel e as obrigações de prestação de contas.

O mapeamento abaixo é o insumo da dimensão `Unidade_Gestora` do modelo dimensional descrito em [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) e alimenta os recortes por unidade em [`../dataset/planilhas/`](../dataset/planilhas/).

---

## Mapeamento

| Código | Unidade gestora | Responsável pela análise |
| --- | --- | --- |
| `23060` | Reitoria | `SRV-03` |
| `23856` | Poço | `SRV-03` |
| `23707` | Tobias Barreto | `SRV-05` |
| `23464` | Glória | `SRV-04` |
| `23463` | Estância | `SRV-04` |
| `23290` | Aracaju | `SRV-05` |
| `23462` | Itabaiana | `SRV-04` |
| `23289` | São Cristóvão | `SRV-02` |
| `23706` | Propriá | `SRV-01` |
| `23832` | Nossa Senhora do Socorro | `SRV-01` |
| `23288` | Lagarto | `SRV-01` |

**Total: 11 unidades gestoras**, com distribuição entre 5 responsáveis.

> Os nomes de unidades gestoras seguem a designação dos *campi* e unidades do Instituto Federal de Sergipe. A grafia nesta tabela foi normalizada em relação ao acervo original.

---

## Distribuição da carga de análise

A distribuição efetiva do volume de documentos analisados por responsável, apurada no período de maio a agosto de 2025, está consolidada em [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md).

| Integrante | Unidades atribuídas | Participação no total analisado |
| --- | --- | --- |
| `SRV-01` | 3 | 32,6% |
| `SRV-02` | 1 | 22,7% |
| `SRV-03` | 2 | 18,0% |
| `SRV-04` | 3 | 16,5% |
| `SRV-05` | 2 | 10,3% |

A leitura conjunta das duas tabelas evidencia que **o volume analisado não é proporcional ao número de unidades atribuídas** — cada unidade gestora tem porte e complexidade distintos. Essa é uma das informações de gestão que o painel passou a tornar visível, apoiando a redistribuição de carga entre os responsáveis.

> O período de referência (maio a agosto de 2025) e os critérios de apuração estão documentados no relatório consolidado. Trata-se de **apuração administrativa**, não de medição experimental.

---

## Convenções de identificação

A operação de conformidade foi conduzida por cinco integrantes. Neste repositório, todos são identificados **exclusivamente por código pseudônimo**, conforme a política de minimização de dados pessoais descrita em [governanca-de-dados.md](./governanca-de-dados.md):

| Código | Atribuição na operação |
| --- | --- |
| `SRV-01` | Extração de dados do SIAFI e registro na planilha de controle |
| `SRV-02` | Extração de dados do SIAFI e registro na planilha de controle |
| `SRV-03` | Modelagem de dados, Power Query, medidas DAX e visualizações no Power BI |
| `SRV-04` | Extração de dados do SIAFI e registro na planilha de controle |
| `SRV-05` | Extração de dados do SIAFI e registro na planilha de controle |

Os mesmos códigos são usados na coluna `servidor` de [`../dataset/planilhas/`](../dataset/planilhas/), no [relatório de análise documental](./relatorios/analise-documental-2025.md) e na seção de distribuição de tarefas de [../dashboard/README.md](../dashboard/README.md).

> **Correspondência código ↔ pessoa.** A tabela que associa cada código ao integrante real **não é versionada neste repositório**. Ela é mantida pelo responsável pelo tratamento dos dados, fora do controle de versão, e é o único artefato capaz de reverter a pseudonimização.

> **Risco residual.** A pseudonimização reduz, mas não elimina, a identificabilidade: os percentuais e a distribuição por unidade gestora permanecem estáveis no tempo e podem ser cruzados com outras bases públicas do Instituto. Para elevar o projeto ao nível 2 de maturidade (ver [governanca-de-dados.md](./governanca-de-dados.md#roteiro-de-maturidade)), a alternativa é substituir o código de projeto por **código funcional institucional** ou eliminar a granularidade individual, publicando apenas agregados. A decisão é do responsável pelo tratamento dos dados.

---

## Documentos relacionados

- [governanca-de-dados.md](./governanca-de-dados.md) — classificação, privacidade e LGPD
- [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md) — volume consolidado por responsável
- [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) — dimensão `Unidade_Gestora` no modelo relacional
- [fontes-de-dados.md](./fontes-de-dados.md) — origem dos dados de unidade gestora
