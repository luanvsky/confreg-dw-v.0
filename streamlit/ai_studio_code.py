import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Checklist de Conformidade - IFS", layout="wide")

st.title("📋 Sistema de Conformidade de Registro de Gestão")
st.subheader("Ferramenta de Apoio ao Conformador")

# --- LOGIN SIMULADO ---
usuario = st.sidebar.text_input("Nome do Conformador:")
unidade = st.sidebar.selectbox("Unidade Gestora:", ["Reitoria", "Campus Aracaju", "Campus São Cristóvão", "Outros"])

# --- FORMULÁRIO PRINCIPAL ---
with st.form("checklist_form"):
    st.write("### Dados do Processo")
    col1, col2 = st.columns(2)
    num_processo = col1.text_input("Número do Processo (SEI):")
    tipo_doc = col2.selectbox("Documento para Análise:", 
                               ["Nota Fiscal / Fatura", "Diárias e Passagens (SCDP)", "Almoxarifado (RMA)", "Bens Móveis (RMB)", "Ajustes Contábeis"])

    st.divider()
    st.write(f"### Checklist: {tipo_doc}")
    
    respostas = {}
    
    # Checklist Dinâmico baseado no Anexo VII do Manual
    if tipo_doc == "Nota Fiscal / Fatura":
        respostas['venda_servico'] = st.checkbox("O tipo de NF refere-se corretamente a venda ou serviço?")
        respostas['prazo_emissao'] = st.checkbox("A NF foi emitida dentro do prazo limite?")
        respostas['dados_fornecedor'] = st.checkbox("Razão Social, CNPJ e Endereço conferem com a Nota de Empenho?")
        respostas['atesto'] = st.checkbox("Existe o 'Atesto' no verso ou assinatura digital do responsável?")
        respostas['validade_nfe'] = st.checkbox("A validade da NF-e foi consultada no portal da SEFAZ?")
        
    elif tipo_doc == "Almoxarifado (RMA)":
        respostas['mes_exercicio'] = st.checkbox("Dados relativos ao mês e exercício estão corretos?")
        respostas['compativel_siafi'] = st.checkbox("Os dados estão compatibilizados entre SIAFI e RMA?")
        respostas['assinatura_setor'] = st.checkbox("RMA está datado e assinado pelo responsável do almoxarifado?")

    # --- RESULTADO DA ANÁLISE ---
    st.divider()
    situacao = st.radio("Resultado Final:", ["SEM RESTRIÇÃO", "COM RESTRIÇÃO"])
    
    codigo_restricao = ""
    if situacao == "COM RESTRIÇÃO":
        codigo_restricao = st.multiselect("Selecione os Códigos de Restrição (Anexo VIII):", 
                                          ["002 - Erro UG/Gestão", "011 - Erro Observação", "118 - Falta de Retenção", "910 - Documento sem Atesto", "951 - Documentação não analisada"])
        obs = st.text_area("Breve resumo do problema:")

    submit = st.form_submit_button("Salvar Análise e Gerar Registro")

# --- PROCESSAMENTO ---
if submit:
    if not usuario or not num_processo:
        st.error("Por favor, preencha o nome do conformador e o número do processo.")
    else:
        # Criando o dicionário de dados para salvar
        dados_analise = {
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Conformador": usuario,
            "Processo": num_processo,
            "Documento": tipo_doc,
            "Resultado": situacao,
            "Cod_Restricao": str(codigo_restricao)
        }
        
        # Simulando salvamento em banco de dados (aqui poderia ser um CSV ou SQL)
        st.success("Análise salva com sucesso!")
        
        # Gerando o texto para o relatório SIAFI
        st.info("### Texto para o Relatório Diário:")
        if situacao == "SEM RESTRIÇÃO":
            st.code(f"Análise do processo {num_processo} ({tipo_doc}): Documentação comprova de forma fidedigna os atos de gestão registrados no SIAFI.")
        else:
            st.code(f"Análise do processo {num_processo} ({tipo_doc}): Registro com restrição devido aos códigos {codigo_restricao}. {obs}")