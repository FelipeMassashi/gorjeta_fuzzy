import numpy as np
import plotly.graph_objects as go
import plotly.subplots as sp

# Funções de pertinência para a qualidade do serviço e da comida
def pertinencia_ruim(x):
    return max(min((5 - x) / 5, 1), 0)

def pertinencia_media(x):
    return max(min((x - 5) / 2.5, (10 - x) / 2.5), 0)

def pertinencia_boa(x):
    return max(min((x - 7.5) / 2.5, 1), 0)

# Funções de pertinência para a gorjeta
def gorjeta_baixa(x):
    return max(min((10 - x) / 10, 1), 0)

def gorjeta_media(x):
    return max(min((x - 10) / 5, (20 - x) / 5), 0)

def gorjeta_alta(x):
    return max(min((x - 15) / 10, 1), 0)

# Regras fuzzy
def regras_fuzzy(servico, comida):
    regras = []
    regras.append((min(pertinencia_ruim(servico), pertinencia_ruim(comida)), gorjeta_baixa))
    regras.append((min(pertinencia_ruim(servico), pertinencia_media(comida)), gorjeta_baixa))
    regras.append((min(pertinencia_ruim(servico), pertinencia_boa(comida)), gorjeta_media))

    regras.append((min(pertinencia_media(servico), pertinencia_ruim(comida)), gorjeta_baixa))
    regras.append((min(pertinencia_media(servico), pertinencia_media(comida)), gorjeta_media))
    regras.append((min(pertinencia_media(servico), pertinencia_boa(comida)), gorjeta_alta))

    regras.append((min(pertinencia_boa(servico), pertinencia_ruim(comida)), gorjeta_media))
    regras.append((min(pertinencia_boa(servico), pertinencia_media(comida)), gorjeta_alta))
    regras.append((min(pertinencia_boa(servico), pertinencia_boa(comida)), gorjeta_alta))
    return regras

# Inferência fuzzy aprimorada
def inferencia_fuzzy(servico, comida):
    regras = regras_fuzzy(servico, comida)
    saida_ativacao = np.zeros(30)  # Vetor para a saída fuzzy (0 a 30% de gorjeta)
    for pertinencia_entrada, func_pertinencia_saida in regras:
        for x in range(30):
            saida_ativacao[x] = max(saida_ativacao[x], min(pertinencia_entrada, func_pertinencia_saida(x)))
    return saida_ativacao

# Defuzzificação
def defuzzificacao(saida_ativacao):
    soma_ativacao = np.sum(saida_ativacao)
    if soma_ativacao == 0:
        return 0
    soma_produtos = np.sum(saida_ativacao * np.arange(30))
    return soma_produtos / soma_ativacao

# Visualização das funções de pertinência usando Plotly
def plot_pertinencia():
    x = np.linspace(0, 10, 100)
    x_gorjeta = np.linspace(0, 30, 100)

    fig = sp.make_subplots(rows=2, cols=1, subplot_titles=("Qualidade do Serviço e Comida", "Gorjeta"))

    # Funções de pertinência para serviço e comida
    fig.add_trace(go.Scatter(x=x, y=[pertinencia_ruim(i) for i in x], mode='lines', name='Ruim', line=dict(color='red')), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=[pertinencia_media(i) for i in x], mode='lines', name='Média', line=dict(color='orange')), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=[pertinencia_boa(i) for i in x], mode='lines', name='Boa', line=dict(color='green')), row=1, col=1)

    # Funções de pertinência para gorjeta
    fig.add_trace(go.Scatter(x=x_gorjeta, y=[gorjeta_baixa(i) for i in x_gorjeta], mode='lines', name='Baixa', line=dict(color='blue')), row=2, col=1)
    fig.add_trace(go.Scatter(x=x_gorjeta, y=[gorjeta_media(i) for i in x_gorjeta], mode='lines', name='Média', line=dict(color='purple')), row=2, col=1)
    fig.add_trace(go.Scatter(x=x_gorjeta, y=[gorjeta_alta(i) for i in x_gorjeta], mode='lines', name='Alta', line=dict(color='black')), row=2, col=1)

    fig.update_xaxes(title_text="Qualidade", row=1, col=1)
    fig.update_yaxes(title_text="Pertinência", row=1, col=1)
    fig.update_xaxes(title_text="Gorjeta", row=2, col=1)
    fig.update_yaxes(title_text="Pertinência", row=2, col=1)

    fig.update_layout(height=600, width=800, title_text="Funções de Pertinência", showlegend=False)
    fig.show()

plot_pertinencia()

qualidade_servico = 8  # Qualidade do serviço (exemplo: 0 a 10)
qualidade_comida = 6   # Qualidade da comida (exemplo: 0 a 10)

saida_ativacao = inferencia_fuzzy(qualidade_servico, qualidade_comida)
gorjeta = defuzzificacao(saida_ativacao)

print(f"Para uma qualidade de serviço de {qualidade_servico} e comida de {qualidade_comida}, a gorjeta deve ser {gorjeta:.2f}%")
