# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram organizados para facilitar a leitura do modelo e melhorar a resposta do agente:

* O perfil do usuário foi estruturado em JSON com informações financeiras completas (renda, metas, patrimônio e perfil de risco)
* As transações foram mantidas em formato CSV para fácil leitura e análise de gastos
* O histórico de atendimento foi armazenado em CSV para simular memória de conversa
* Os produtos financeiros foram organizados em JSON para possíveis recomendações futuras

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados são carregados no início da aplicação usando json.load() para arquivos JSON e pandas.read_csv() para arquivos CSV. Eles ficam disponíveis durante toda a execução do agente.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são inseridos diretamente no contexto do prompt, junto com o system prompt e a pergunta do usuário.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Idade: 32
- Profissão: Analista de Sistemas
- Renda mensal: R$ 5000
- Perfil: Moderado
- Objetivo: Construir reserva de emergência

Reserva de emergência:
- Atual: R$ 10000
- Meta: R$ 15000
- Falta: R$ 5000

Últimas transações:
data | categoria | valor
2026-04-01 | Alimentação | 120
2026-04-03 | Transporte | 80
2026-04-05 | Alimentação | 60

Atendimentos anteriores:
Usuário: Quanto gastei com alimentação?
Agente: Você gastou R$ 180 neste período.
```
