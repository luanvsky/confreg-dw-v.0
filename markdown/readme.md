# ⚙️ Projeto de Banco de Dados MySQL: Documentos, Servidores e Unidades Gestoras 🏢

## Visão Geral do Projeto

Este projeto tem como objetivo criar um banco de dados MySQL para gerenciar documentos, servidores responsáveis, unidades gestoras e o histórico de processamento desses documentos. O modelo de dados foi desenvolvido a partir da análise das imagens no final deste readme buscando otimizar a organização, o controle e a rastreabilidade das informações.

## Modelo de Entidade-Relacionamento (ER) 📊🔗✨

O Modelo Entidade-Relacionamento (ER) abaixo representa a estrutura do banco de dados proposto:

**Entidades e Atributos**

1️⃣ **Documento** 📜
- `id_documento` (PK) – Identificação única do documento
- `tipo_documento` – Tipo do registro (Ex.: Nota de Lançamento, Arrecadação Financeira)
- `descricao` - Descrição detalhada do documento
- `data_criacao` – Data de emissão do documento
- `data_ultima_atualizacao` – Data da última atualização do documento
- `id_servidor` (FK) – Servidor responsável pelo documento
- `id_unidade_gestora` (FK) – UG vinculada ao documento
- `status` – Estado do documento (Ex.: Pendente, Aprovado, Rejeitado)
- `prioridade` - Nível de prioridade do documento
- `versao` - Número da versão do documento

2️⃣ **Servidor** 👥
- `id_servidor` (PK) – Identificação única do servidor
- `nome_servidor` – Nome do servidor
- `cargo` – Cargo/Função do servidor
- `setor` – Setor ao qual o servidor pertence
- `data_admissao` – Data de admissão
- `id_supervisor` (FK) - ID do supervisor do servidor (auto-relacionamento)
- `nivel_acesso` - Nível de acesso do servidor ao sistema

3️⃣ **Unidade Gestora (UG)** 🏢
- `id_unidade_gestora` (PK) – Identificação única da UG
- `codigo_ug` – Código administrativo da UG
- `orgao_superior` – Órgão superior vinculado
- `orcamento_disponivel` – Valor de orçamento disponível
- `total_documentos_processados` - Total de documentos processados pela UG
- `responsavel_ug` - Nome do responsável pela UG

4️⃣ **Histórico de Processamento** 📂
- `id_historico` (PK) – Identificação única da análise
- `id_documento` (FK) – Documento analisado
- `id_servidor` (FK) – Servidor que realizou a análise
- `data_analise` – Data e hora de processamento do documento
- `tempo_processamento` – Tempo gasto na análise (em minutos)
- `observacoes` – Observações sobre o processamento
- `acao_realizada` - Ação realizada no documento

5️⃣ **Anexo** 📎
- `id_anexo` (PK) - Identificação única do anexo
- `id_documento` (FK) - Documento ao qual o anexo pertence
- `nome_arquivo` - Nome do arquivo do anexo
- `tipo_arquivo` - Tipo do arquivo do anexo
- `tamanho_kb` - Tamanho do arquivo em KB
- `data_upload` - Data e hora do upload do anexo

**Relacionamentos**

🔗 Cada `Documento` pertence a um único `Servidor`, mas um `Servidor` pode analisar vários documentos.
🔗 `Documentos` estão vinculados a uma `Unidade Gestora` (UG).
🔗 O `Histórico de Processamento` rastreia as análises de cada `Documento` por `Servidor`.
🔗 Um `Servidor` pode ter um `supervisor` (auto-relacionamento).
🔗 Um `Documento` pode ter múltiplos `Anexos`.

## Criação das Tabelas em MySQL 💻💾

Os comandos SQL abaixo criam as tabelas no MySQL, definindo as chaves primárias, chaves estrangeiras e outros constraints para garantir a integridade do banco de dados.

```sql
-- Tabela: Servidor
CREATE TABLE Servidor (
    id_servidor INT PRIMARY KEY AUTO_INCREMENT,
    nome_servidor VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    setor VARCHAR(50),
    data_admissao DATE,
    id_supervisor INT,
    nivel_acesso ENUM('Leitura', 'Edição', 'Aprovação'),
    FOREIGN KEY (id_supervisor) REFERENCES Servidor(id_servidor)
);

-- Tabela: Unidade_Gestora (UG)
CREATE TABLE Unidade_Gestora (
    id_unidade_gestora INT PRIMARY KEY AUTO_INCREMENT,
    codigo_ug VARCHAR(20) NOT NULL UNIQUE,
    orgao_superior VARCHAR(100),
    orcamento_disponivel DECIMAL(15,2),
    total_documentos_processados INT DEFAULT 0,
    responsavel_ug VARCHAR(100)
);

-- Tabela: Documento
CREATE TABLE Documento (
    id_documento INT PRIMARY KEY AUTO_INCREMENT,
    tipo_documento VARCHAR(50) NOT NULL,
    descricao TEXT,
    data_criacao DATE,
    data_ultima_atualizacao DATE DEFAULT CURRENT_DATE,
    id_servidor INT,
    id_unidade_gestora INT,
    status ENUM('Pendente', 'Aprovado', 'Rejeitado'),
    prioridade ENUM('Baixa', 'Média', 'Alta'),
    versao INT DEFAULT 1,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor),
    FOREIGN KEY (id_unidade_gestora) REFERENCES Unidade_Gestora(id_unidade_gestora)
);

-- Tabela: Historico_Processamento
CREATE TABLE Historico_Processamento (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    id_documento INT,
    id_servidor INT,
    data_analise DATETIME DEFAULT CURRENT_TIMESTAMP,
    tempo_processamento INT,
    observacoes TEXT,
    acao_realizada ENUM('Criado', 'Editado', 'Deletado', 'Aprovado'),
    FOREIGN KEY (id_documento) REFERENCES Documento(id_documento),
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);

-- Tabela: Anexo
CREATE TABLE Anexo (
    id_anexo INT PRIMARY KEY AUTO_INCREMENT,
    id_documento INT,
    nome_arquivo VARCHAR(255) NOT NULL,
    tipo_arquivo ENUM('PDF', 'DOCX', 'XLSX', 'CSV', 'JPG', 'PNG'),
    tamanho_kb INT,
    data_upload DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_documento) REFERENCES Documento(id_documento)
);
```

## População Inicial do Banco de Dados 🚀💾

Abaixo estão alguns comandos INSERT para popular as tabelas com dados de exemplo para testes.

```sql
-- Inserindo servidores
INSERT INTO Servidor (nome_servidor, cargo, setor, data_admissao, id_supervisor, nivel_acesso) VALUES
('SRV-02 Silva', 'Analista', 'Financeiro', '2020-06-15', NULL, 'Aprovação'),
('SRV-04 Souza', 'Gerente', 'Administrativo', '2018-10-22', NULL, 'Aprovação'),
('Carlos Oliveira', 'Assistente', 'Financeiro', '2023-02-10', 1, 'Edição');

-- Inserindo unidades gestoras
INSERT INTO Unidade_Gestora (codigo_ug, orgao_superior, orcamento_disponivel, total_documentos_processados, responsavel_ug) VALUES
('UG152420', 'Secretaria de Finanças', 500000.00, 20, 'João Ferreira'),
('UG154679', 'Secretaria de Administração', 350000.00, 15, 'Maria Santos');

-- Inserindo documentos
INSERT INTO Documento (tipo_documento, descricao, data_criacao, id_servidor, id_unidade_gestora, status, prioridade, versao) VALUES
('Nota de Lançamento', 'Lançamento de valores para sistema contábil.', '2025-04-14', 1, 1, 'Aprovado', 'Alta', 1),
('Arrecadação Financeira', 'Relatório de arrecadação do setor financeiro.', '2025-04-15', 2, 2, 'Pendente', 'Média', 1);

-- Inserindo histórico de processamento
INSERT INTO Historico_Processamento (id_documento, id_servidor, data_analise, tempo_processamento, observacoes, acao_realizada) VALUES
(1, 1, '2025-04-14 10:15:00', 30, 'Documento analisado e aprovado.', 'Aprovado'),
(2, 2, '2025-04-15 11:45:00', 45, 'Necessário revisão por outro setor.', 'Editado');

-- Inserindo anexos
INSERT INTO Anexo (id_documento, nome_arquivo, tipo_arquivo, tamanho_kb, data_upload) VALUES
(1, 'nota_lancamento_152420.pdf', 'PDF', 250, '2025-04-14 10:16:00'),
(2, 'relatorio_arrecadacao.xlsx', 'XLSX', 180, '2025-04-15 11:46:00');
```

## Consultas SQL (Queries) 🔍✨

Abaixo estão exemplos de consultas SQL para buscar informações no banco de dados, divididas por nível de complexidade.

### 🔹 **Consultas Simples**

```sql
-- 1️⃣ Selecionar todos os servidores
SELECT * FROM Servidor;

-- 2️⃣ Listar todos os documentos cadastrados
SELECT id_documento, tipo_documento, data_criacao FROM Documento;

-- 3️⃣ Filtrar documentos pendentes
SELECT id_documento, tipo_documento FROM Documento WHERE status = 'Pendente';
```

### 🔹 **Consultas Intermediárias**

```sql
-- 4️⃣ Contar a quantidade de documentos por tipo
SELECT tipo_documento, COUNT(*) AS total_documentos FROM Documento GROUP BY tipo_documento;

-- 5️⃣ Buscar documentos criados em abril de 2025
SELECT * FROM Documento WHERE data_criacao BETWEEN '2025-04-01' AND '2025-04-30';

-- 6️⃣ Listar servidores que analisaram documentos
SELECT DISTINCT s.nome_servidor
FROM Servidor s
JOIN Historico_Processamento hp ON s.id_servidor = hp.id_servidor;
```

### 🔹 **Consultas Avançadas**

```sql
-- 7️⃣ Listar documentos e seus servidores responsáveis
SELECT d.id_documento, d.tipo_documento, s.nome_servidor
FROM Documento d
JOIN Servidor s ON d.id_servidor = s.id_servidor;

-- 8️⃣ Tempo médio de processamento por servidor
SELECT s.nome_servidor, AVG(hp.tempo_processamento) AS media_tempo
FROM Historico_Processamento hp
JOIN Servidor s ON hp.id_servidor = s.id_servidor
GROUP BY s.nome_servidor
ORDER BY media_tempo DESC;

-- 9️⃣ Buscar documentos com anexos
SELECT d.id_documento, d.tipo_documento, a.nome_arquivo
FROM Documento d
JOIN Anexo a ON d.id_documento = a.id_documento;

-- 🔟 Ranking de servidores que analisaram mais documentos
SELECT s.nome_servidor, COUNT(hp.id_historico) AS total_analises
FROM Servidor s
JOIN Historico_Processamento hp ON s.id_servidor = hp.id_servidor
GROUP BY s.nome_servidor
ORDER BY total_analises DESC;

-- 1️⃣1️⃣ Relatório completo de documentos e UGs
SELECT d.id_documento, d.tipo_documento, d.data_criacao, u.codigo_ug, u.responsavel_ug
FROM Documento d
JOIN Unidade_Gestora u ON d.id_unidade_gestora = u.id_unidade_gestora
ORDER BY d.data_criacao DESC;
```

## Próximos Passos e Contato 📧

Este projeto demonstra habilidades em modelagem de banco de dados relacional, criação de esquemas eficientes em MySQL, implementação de integridade referencial, população de dados para testes e elaboração de consultas SQL para diferentes necessidades de informação. A capacidade de analisar requisitos a partir de dados visuais e transformá-los em um modelo de banco de dados funcional é uma competência valiosa para o desenvolvimento de sistemas robustos e escaláveis.

Se você busca um profissional com expertise em design e implementação de bancos de dados, análise de dados e desenvolvimento de soluções eficientes, entre em contato:

* **E-mail:** victortqp@hotmail.com
* **E-mail:** victorcupinxa@gmail.com

Estou à disposição para discutir suas necessidades e contribuir para o sucesso dos seus projetos.

---

Este foi um projeto desenvolvido com o objetivo de demonstrar um fluxo completo de trabalho em design de bancos de dados, desde a concepção até a implementação e consulta. As etapas incluíram:

1.  **Análise de Requisitos:** Interpretação de dados visuais para identificar entidades, atributos e relacionamentos.
2.  **Modelagem Conceitual:** Criação de um Modelo Entidade-Relacionamento (ER) para representar a estrutura do banco de dados.
3.  **Modelagem Lógica:** Tradução do modelo ER para um esquema relacional específico para MySQL, definindo tabelas, colunas, tipos de dados, chaves primárias e estrangeiras.
4.  **Implementação Física:** Geração de scripts SQL para criar as tabelas no MySQL.

# Geral
![image](https://github.com/user-attachments/assets/40ce5c49-ddc9-4cbc-98eb-9dff481d6c64)
https://docs.google.com/spreadsheets/d/1JPuQU6f11u_06ZLo7hIuEa6NcK5keUhgAIpRq7fYP4w/edit?gid=12633740#gid=12633740
# Reitoria
![image](https://github.com/user-attachments/assets/5db2af55-6116-41f9-b38a-463001343f79)
# Tablet
![Imagem do WhatsApp de 2025-04-16 à(s) 10 58 24_87cbbd8e](https://github.com/user-attachments/assets/df4346a1-0b40-4c7e-9ca6-a2f058c48641)

5.  **População de Dados:** Inserção de dados de exemplo para facilitar testes e demonstrações.
6.  **Elaboração de Consultas SQL:** Desenvolvimento de queries para extrair informações relevantes do banco de dados, abrangendo diferentes níveis de complexidade.

As habilidades demonstradas neste projeto são fundamentais para a construção de sistemas de informação eficazes e para a gestão inteligente de dados.
