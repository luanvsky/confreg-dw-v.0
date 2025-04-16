
## Geral
![image](https://github.com/user-attachments/assets/40ce5c49-ddc9-4cbc-98eb-9dff481d6c64)
# https://docs.google.com/spreadsheets/d/1JPuQU6f11u_06ZLo7hIuEa6NcK5keUhgAIpRq7fYP4w/edit?gid=12633740#gid=12633740


## Reitoria
![image](https://github.com/user-attachments/assets/5db2af55-6116-41f9-b38a-463001343f79)


## Tablet
![Imagem do WhatsApp de 2025-04-16 à(s) 10 58 24_87cbbd8e](https://github.com/user-attachments/assets/df4346a1-0b40-4c7e-9ca6-a2f058c48641)


Modelo de Entidade-Relacionamento (ER) para seu banco MySQL considerando os dados das imagens! 📊🔗✨
Entidades e Atributos
1️⃣ Documento 📜
- id_documento (PK) – Identificação única do documento
- tipo_documento – Tipo do registro (Ex.: Nota de Lançamento, Arrecadação Financeira)
- data_criacao – Data de emissão do documento
- id_servidor (FK) – Servidor responsável pelo documento
- id_unidade_gestora (FK) – UG vinculada ao documento
- status – Estado do documento (Ex.: Pendente, Aprovado, Rejeitado)

2️⃣ Servidor 👥
- id_servidor (PK) – Identificação única do servidor
- nome_servidor – Nome do servidor
- cargo – Cargo/Função do servidor
- setor – Setor ao qual o servidor pertence
- data_admissao – Data de admissão

3️⃣ Unidade Gestora (UG) 🏢
- id_unidade_gestora (PK) – Identificação única da UG
- codigo_ug – Código administrativo da UG
- orgao_superior – Órgão superior vinculado
- orcamento_disponivel – Valor de orçamento disponível

4️⃣ Histórico de Processamento 📂
- id_historico (PK) – Identificação única da análise
- id_documento (FK) – Documento analisado
- id_servidor (FK) – Servidor que realizou a análise
- data_analise – Data de processamento do documento
- tempo_processamento – Tempo gasto na análise
- observacoes – Observações sobre o processamento

Relacionamentos
🔗 Cada Documento pertence a um único Servidor, mas um Servidor pode analisar vários documentos ao longo do tempo.
🔗 Documentos também estão vinculados a uma Unidade Gestora (UG), garantindo controle administrativo.
🔗 O Histórico de Processamento permite rastrear quem analisou cada documento e quando, garantindo auditoria e controle.
📌 Agora seu modelo ER está pronto para ser implementado no MySQL! 🚀💾 Se precisar de ajustes ou quiser adicionar mais complexidade, me avise! 😃📑



Ótimo! Aqui estão os comandos SQL para criação das tabelas no MySQL, garantindo integridade referencial e estrutura otimizada. 🚀💾
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

-- Tabela: Unidade Gestora (UG)
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

-- Tabela: Histórico de Processamento
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


🔗 Melhorias aplicadas:
✅ Integridade referencial garantida com chaves estrangeiras.
✅ Enumeração de status e prioridade para controle eficiente de documentos.
✅ Histórico detalhado para auditoria de processamento.
✅ Sistema de versão para rastrear mudanças nos documentos.
✅ Anexos suportados, permitindo gerenciamento completo de arquivos.
📌 Agora seu banco de dados MySQL está pronto para ser implementado! 🚀💻
Se precisar de ajustes ou melhorias adicionais, me avise! 😃📑
Quer que eu crie consultas SQL para buscar informações? 🔍✨


Ótimo! Agora vamos popular o banco de dados com alguns registros iniciais para testes. 🚀💾
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


🔗 O que foi inserido?
✅ Servidores com diferentes níveis de acesso e cargos.
✅ Unidades Gestoras com informações gerenciais.
✅ Documentos registrados com status e prioridade.
✅ Histórico de processamento detalhado para auditoria.
✅ Anexos vinculados aos documentos.
📌 Agora seu banco tem dados reais para testes e consultas! 🚀💻
Se quiser mais registros ou ajustes, só me avisar! 😃📑
Quer que eu te ajude com consultas SQL para buscar essas informações? 🔍✨

- Comandos SQL para criar essas tabelas? 💻✨
- Aqui estão **consultas SQL (queries)** para **diferentes níveis de complexidade**, desde as **simples** até as mais **avançadas**! 🚀💾  

---

## 🔹 **Consultas Simples**  
### 1️⃣ **Selecionar todos os servidores**  
```sql
SELECT * FROM Servidor;
```

### 2️⃣ **Listar todos os documentos cadastrados**  
```sql
SELECT id_documento, tipo_documento, data_criacao FROM Documento;
```

### 3️⃣ **Filtrar documentos pendentes**  
```sql
SELECT id_documento, tipo_documento FROM Documento WHERE status = 'Pendente';
```

---

## 🔹 **Consultas Intermediárias**  
### 4️⃣ **Contar a quantidade de documentos por tipo**  
```sql
SELECT tipo_documento, COUNT(*) AS total_documentos FROM Documento GROUP BY tipo_documento;
```

### 5️⃣ **Buscar documentos criados em abril de 2025**  
```sql
SELECT * FROM Documento WHERE data_criacao BETWEEN '2025-04-01' AND '2025-04-30';
```

### 6️⃣ **Listar servidores que analisaram documentos**  
```sql
SELECT DISTINCT s.nome_servidor 
FROM Servidor s 
JOIN Historico_Processamento hp ON s.id_servidor = hp.id_servidor;
```

---

## 🔹 **Consultas Avançadas**  
### 7️⃣ **Listar documentos e seus servidores responsáveis**  
```sql
SELECT d.id_documento, d.tipo_documento, s.nome_servidor 
FROM Documento d
JOIN Servidor s ON d.id_servidor = s.id_servidor;
```

### 8️⃣ **Tempo médio de processamento por servidor**  
```sql
SELECT s.nome_servidor, AVG(hp.tempo_processamento) AS media_tempo
FROM Historico_Processamento hp
JOIN Servidor s ON hp.id_servidor = s.id_servidor
GROUP BY s.nome_servidor
ORDER BY media_tempo DESC;
```

### 9️⃣ **Buscar documentos com anexos**  
```sql
SELECT d.id_documento, d.tipo_documento, a.nome_arquivo 
FROM Documento d
JOIN Anexo a ON d.id_documento = a.id_documento;
```

### 🔟 **Ranking de servidores que analisaram mais documentos**  
```sql
SELECT s.nome_servidor, COUNT(hp.id_historico) AS total_analises
FROM Servidor s
JOIN Historico_Processamento hp ON s.id_servidor = hp.id_servidor
GROUP BY s.nome_servidor
ORDER BY total_analises DESC;
```

### 1️⃣1️⃣ **Relatório completo de documentos e UGs**  
```sql
SELECT d.id_documento, d.tipo_documento, d.data_criacao, u.codigo_ug, u.responsavel_ug
FROM Documento d
JOIN Unidade_Gestora u ON d.id_unidade_gestora = u.id_unidade_gestora
ORDER BY d.data_criacao DESC;
```

---

📌 Agora você tem **queries simples, intermediárias e avançadas** para consultas eficientes no seu **banco MySQL**! 🚀💾  
Se precisar de mais alguma query personalizada, é só me avisar! 😃✨  
Quer que eu te ajude a criar **procedures ou triggers** também? 💻🔍

- 

