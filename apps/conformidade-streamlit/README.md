# Verificador de Checklist de Conformidade (Streamlit)

Aplicação local em **Python/Streamlit** para apoio à análise de conformidade de registros de gestão: apresenta o checklist aplicável ao tipo de documento, aplica os códigos de restrição e gera o texto do relatório de conformidade.

O objetivo é reduzir a variabilidade entre analistas e dar suporte padronizado ao preenchimento do checklist do **Anexo VII** e do **Anexo VIII**, conforme o Manual de Procedimentos para a Conformidade de Registro de Gestão.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Como executar](#como-executar)
- [Estrutura](#estrutura)
- [Dependências](#dependências)
- [Limitações](#limitações)
- [Documentos relacionados](#documentos-relacionados)

---

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Checklist por anexo** | Apresenta os itens de verificação do Anexo VII e do Anexo VIII |
| **Códigos de restrição** | Suporta os códigos `002`, `011`, `118`, `910` e `951` |
| **Geração de texto** | Monta o texto do relatório de conformidade para registro no SIAFI |
| **Padronização** | Garante que a mesma sequência de verificação seja aplicada a todos os documentos |

---

## Pré-requisitos

- **Python 3.9** ou superior
- `pip` disponível no ambiente

---

## Como executar

```bash
cd apps/conformidade-streamlit

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

O Streamlit abre a aplicação no navegador padrão, por padrão em `http://localhost:8501`.

---

## Estrutura

```text
conformidade-streamlit/
├── app.py              # Aplicação Streamlit
├── requirements.txt    # Dependências
└── README.md
```

---

## Dependências

Declaradas em [`requirements.txt`](./requirements.txt). Atualmente: `streamlit` e `pandas`.

---

## Limitações

| # | Limitação | Consequência |
| --- | --- | --- |
| L1 | Não persiste histórico entre execuções | Cada sessão começa do zero; o registro é manual |
| L2 | Não consulta as fontes de dados do painel | A conferência contra a base de origem continua manual |
| L3 | Regras de validação codificadas na aplicação | Alteração normativa exige ajuste no código |

A persistência estruturada dessas análises é justamente o que o modelo relacional descrito em [../../docs/modelo-de-dados-mysql.md](../../docs/modelo-de-dados-mysql.md) se propõe a viabilizar.

---

## Documentos relacionados

- [../../README.md](../../README.md) — visão geral do projeto
- [../../docs/governanca-de-dados.md](../../docs/governanca-de-dados.md) — governança e privacidade
- [../../docs/fontes-de-dados.md](../../docs/fontes-de-dados.md) — catálogo de fontes
- [../conformidade-web/README.md](../conformidade-web/README.md) — aplicação web de conformidade
