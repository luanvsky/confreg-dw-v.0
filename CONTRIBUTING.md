# Guia de Contribuição

Este documento descreve o fluxo de trabalho adotado no projeto **Conformidade de Registro de Gestão — Data Warehouse & Business Intelligence**, com atenção especial às boas práticas de **governança de dados** aplicadas ao domínio contábil público.

---

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Fluxo de trabalho](#fluxo-de-trabalho)
- [Padrão de commits](#padrão-de-commits)
- [Padrão de nomenclatura de arquivos](#padrão-de-nomenclatura-de-arquivos)
- [Versionamento de dashboards](#versionamento-de-dashboards)
- [Política de dados](#política-de-dados)
- [Abertura de issues](#abertura-de-issues)
- [Checklist de pull request](#checklist-de-pull-request)

---

## Pré-requisitos

| Ferramenta | Versão mínima | Uso no projeto |
| --- | --- | --- |
| [Git](https://git-scm.com/) | 2.40+ | Controle de versão |
| [Power BI Desktop](https://powerbi.microsoft.com/desktop/) | Versão corrente | Edição dos arquivos `.pbix` |
| [Python](https://www.python.org/) | 3.10+ | Notebooks de apoio e aplicação Streamlit |
| Conta no Power BI Service | — | Publicação e atualização dos painéis |

Para trabalhar com a aplicação Streamlit:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r apps/conformidade-streamlit/requirements.txt
streamlit run apps/conformidade-streamlit/app.py
```

---

## Fluxo de trabalho

1. **Sincronize a branch principal**

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Crie uma branch descritiva** a partir de `main`:

   | Prefixo | Uso |
   | --- | --- |
   | `feature/` | Nova funcionalidade ou visão no painel |
   | `fix/` | Correção de defeito ou de indicador incorreto |
   | `docs/` | Alteração exclusiva de documentação |
   | `data/` | Atualização de conjuntos de dados do `dataset/` |
   | `chore/` | Manutenção, dependências e configuração |

   ```bash
   git checkout -b feature/alerta-vencimento-darf
   ```

3. **Realize commits pequenos e coesos**, seguindo o padrão descrito abaixo.

4. **Abra um pull request** para `main` utilizando o [template](./.github/pull_request_template.md) e aguarde revisão.

> A branch `main` deve permanecer sempre em estado publicável. Alterações diretas na `main` só são aceitáveis para correções triviais de documentação.

---

## Padrão de commits

Adota-se uma variação de [Conventional Commits](https://www.conventionalcommits.org/), com mensagens em português:

```text
<tipo>(<escopo>): <descrição curta no imperativo>

[corpo opcional explicando o porquê da mudança]
```

**Tipos aceitos:** `feat`, `fix`, `docs`, `data`, `refactor`, `perf`, `test`, `chore`.

**Escopos sugeridos:** `dashboard`, `dataset`, `docs`, `apps`, `notebooks`.

Exemplos:

```text
feat(dashboard): adiciona medida DAX de tempo médio de análise
fix(dataset): corrige tipagem da coluna de data na base da reitoria
data(dataset): atualiza extração impconfreg de 2023
docs(governanca): detalha matriz de classificação de dados
```

---

## Padrão de nomenclatura de arquivos

A consistência de nomenclatura é um requisito de governança: nomes previsíveis são o primeiro passo para um catálogo de dados confiável.

- Use **letras minúsculas**, com palavras separadas por hífen ou sublinhado: `docs-<responsavel>-2025-02.xlsx`.
- **Não use espaços, parênteses ou acentos** em nomes de arquivos versionados.
- Datas no formato `AAAA-MM` ou `AAAA-MM-DD`.
- Versões de dashboard com sufixo `_vN` ou `_vN.M` — nunca `v5.` ou `version 2`.
- Organize arquivos por **finalidade**, não por extensão: `dataset/imagens/` e `dataset/planilhas/`, jamais `dataset/.jpg/` ou `dataset/.xls/`.

---

## Versionamento de dashboards

Para evitar ambiguidade entre arquivos com o mesmo nome:

1. Cada release do painel recebe uma versão (`cgconfreg_v8.4.pbix`).
2. Versões publicadas no Power BI Service e documentadas em [`dashboard/README.md`](./dashboard/README.md) devem ter o mesmo identificador usado no arquivo `.pbix`.
3. Arquivos obsoletos são movidos para `dashboard/pbix/legado/` em vez de excluídos, preservando a rastreabilidade histórica. Exceção: artefatos que carreguem identificação de terceiros são **retirados do repositório** e passam a armazenamento controlado, conforme a política de dados abaixo.
4. Ao publicar uma nova versão, registre o que mudou em [`dashboard/v8.md`](./dashboard/v8.md) ou no arquivo de release correspondente.

---

## Política de dados

Este repositório é **público**. Antes de commitar qualquer artefato, verifique:

- ❌ **Não** inclua dados pessoais identificáveis (nomes de servidores, matrículas, CPF, e-mails institucionais) sem anonimização.
- ❌ **Não** inclua extrações contendo identificação de **terceiros** — beneficiários e favorecidos de pagamento, fornecedores, prestadores. Esse dado é o objeto da análise de conformidade, **não pode ser descaracterizado** e, por isso, pertence a armazenamento controlado, não ao versionamento.
- ❌ **Não** inclua links internos de compartilhamento (SharePoint, OneDrive, drives corporativos) nem credenciais, tokens ou chaves de API.
- ❌ **Não** inclua arquivos temporários de ferramentas de escritório (`~$*.xlsx`, `*.pbix~`, `.pbiV5`).
- ✅ Anonimize identificadores antes da publicação, mantendo um dicionário de correspondência fora do repositório.
- ✅ Antes de versionar qualquer extração, aplique a triagem: **este arquivo contém identificação de alguém que não participou do projeto?** Se sim, ele não pertence ao versionamento.
- ✅ Registre a origem, a periodicidade e o responsável de cada conjunto de dados em [`docs/fontes-de-dados.md`](./docs/fontes-de-dados.md).

Consulte [`docs/governanca-de-dados.md`](./docs/governanca-de-dados.md) para a matriz de classificação de dados e as diretrizes de tratamento.

---

## Abertura de issues

Utilize os templates disponíveis em [`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/):

- **Relato de defeito** — indicadores incorretos, falhas de atualização, problemas de visualização.
- **Solicitação de melhoria** — novas visões, medidas, filtros ou fontes de dados.
- **Documentação** — lacunas ou inconsistências na documentação.

Toda issue de defeito em indicador deve informar a **medida ou visão afetada** e a **data de referência** dos dados.

---

## Checklist de pull request

Antes de solicitar revisão, confirme:

- [ ] A branch está atualizada com `main`.
- [ ] As mensagens de commit seguem o padrão adotado.
- [ ] Nenhum dado pessoal, link interno ou credencial foi incluído.
- [ ] Nomes de arquivos seguem o [padrão de nomenclatura](#padrão-de-nomenclatura-de-arquivos).
- [ ] A documentação afetada foi atualizada (`README.md` e `docs/`).
- [ ] Alterações em medidas DAX foram validadas comparando os totais com a base de origem.

---

## Código de conduta

Espera-se de todas as pessoas contribuintes:

- Comunicação respeitosa, objetiva e técnica.
- Transparência sobre limitações e incertezas de dados e indicadores.
- Priorização do interesse público e da confiabilidade da informação contábil.

---

## Contato

**Victor de Melo** — [GitHub](https://github.com/luanvsky) · [LinkedIn](https://www.linkedin.com/in/victor-melo-5b099942/)
