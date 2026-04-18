import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open("./data/perfil_investidor.json"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json"))

contexto = f"""
CLIENTE: {perfil['nome']}
IDADE: {perfil['idade']}
PROFISSÃO: {perfil['profissao']}
RENDA MENSAL: R$ {perfil['renda_mensal']}
PERFIL DE INVESTIDOR: {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """
Você é um assistente financeiro chamado FinBot.

Seu objetivo é ajudar o usuário a controlar seus gastos, acompanhar metas e melhorar sua organização financeira.

REGRAS:
1. Sempre use apenas os dados fornecidos
2. Nunca invente valores
3. Se não souber algo, diga claramente
4. Responda de forma simples e direta
5. Não julgue o usuário
6. Sugira formas simples de economizar
7. Não recomende investimentos sem contexto
8. Se a pergunta for fora de finanças, recuse educadamente

EXEMPLOS:

Pergunta: "Como está minha reserva de emergência?"
Resposta: "Você já tem R$ 10.000 de R$ 15.000. Faltam R$ 5.000 para atingir sua meta."

Pergunta: "Estou indo bem?"
Resposta: "Você já completou cerca de 66% da sua reserva. Está no caminho certo."

Pergunta: "Onde devo investir?"
Resposta: "Como seu perfil é moderado, posso sugerir opções seguras, mas preciso entender melhor seus objetivos."
"""

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]

st.title("Nina, sua assistente financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
