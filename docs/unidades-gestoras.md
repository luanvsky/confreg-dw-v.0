# Unidades Gestoras

Mapeamento das unidades gestoras abrangidas pela rotina de conformidade de registro de gestão e dos responsáveis pela análise de cada uma.

---

> ⚠️ **DOCUMENTO COM DADOS PESSOAIS**
>
> Este documento associa **códigos de unidade gestora a servidores identificados nominalmente**,
> o que configura tratamento de dado pessoal nos termos da Lei nº 13.709/2018 (LGPD).
>
> **Antes de reutilizar ou compartilhar:** substitua os nomes por pseudônimos ou códigos
> funcionais e limite a circulação ao escopo das atividades de conformidade.
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
| `23060` | Reitoria | Victor |
| `23856` | Poço | Victor |
| `23707` | Tobias Barreto | SRV-05 |
| `23464` | Glória | SRV-04 |
| `23463` | Estância | SRV-04 |
| `23290` | Aracaju | SRV-05 |
| `23462` | Itabaiana | SRV-04 |
| `23289` | São Cristóvão | SRV-02 |
| `23706` | Propriá | SRV-01 |
| `23832` | Nossa Senhora do Socorro | SRV-01 |
| `23288` | Lagarto | SRV-01 |

**Total: 11 unidades gestoras**, com distribuição entre 5 responsáveis.

> Os nomes de unidades gestoras seguem a designação dos *campi* e unidades do Instituto Federal de Sergipe. A grafia nesta tabela foi normalizada em relação ao acervo original.

---

## Distribuição da carga de análise

A distribuição efetiva do volume de documentos analisados por responsável, apurada no período de maio a agosto de 2025, está consolidada em [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md).

| Responsável | Unidades atribuídas | Participação no total analisado |
| --- | --- | --- |
| SRV-01 | 3 | 32,6% |
| SRV-02 | 1 | 22,7% |
| Victor | 2 | 18,0% |
| SRV-04 | 3 | 16,5% |
| SRV-05 | 2 | 10,3% |

A leitura conjunta das duas tabelas evidencia que **o volume analisado não é proporcional ao número de unidades atribuídas** — cada unidade gestora tem porte e complexidade distintos. Essa é uma das informações de gestão que o painel passou a tornar visível, apoiando a redistribuição de carga entre os responsáveis.

> O período de referência (maio a agosto de 2025) e os critérios de apuração estão documentados no relatório consolidado. Trata-se de **apuração administrativa**, não de medição experimental.

---

## Convenções de identificação

A operação de conformidade foi conduzida por cinco integrantes. Neste repositório, eles são identificados conforme a política de minimização de dados pessoais descrita em [governanca-de-dados.md](./governanca-de-dados.md):

| Integrante | Identificação neste repositório |
| --- | --- |
| Victor | Nome próprio — autor do projeto técnico |
| SRV-01 | `SRV-01` / pseudônimo `SRV-01` nos painéis |
| SRV-05 | `SRV-05` / pseudônimo `SRV-05` nos painéis |
| SRV-02 | `SRV-02` / pseudônimo `Pavsjy` nos painéis |
| SRV-04 | `SRV-04` / pseudônimo `Tavky` nos painéis |

Os pseudônimos são os mesmos utilizados na documentação dos painéis e na seção de distribuição de tarefas de [../dashboard/README.md](../dashboard/README.md).

> **Recomendação de governança.** Para elevar o projeto ao nível 2 de maturidade (ver [governanca-de-dados.md](./governanca-de-dados.md#roteiro-de-maturidade)), a identificação nominal deve ser substituída por **código funcional** em todo o repositório, inclusive nos painéis publicados. A decisão é do responsável pelo tratamento dos dados.

---

## Documentos relacionados

- [governanca-de-dados.md](./governanca-de-dados.md) — classificação, privacidade e LGPD
- [relatorios/analise-documental-2025.md](./relatorios/analise-documental-2025.md) — volume consolidado por responsável
- [modelo-de-dados-mysql.md](./modelo-de-dados-mysql.md) — dimensão `Unidade_Gestora` no modelo relacional
- [fontes-de-dados.md](./fontes-de-dados.md) — origem dos dados de unidade gestora
