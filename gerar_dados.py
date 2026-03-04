import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurando o gerador
np.random.seed(42)
n_linhas = 500

# Gerando dados fictícios
data = {
    'ID_Cliente': [f'CLIE{i:03d}' for i in np.random.randint(1, 150, n_linhas)],
    'Segmento': np.random.choice(['Varejo', 'Industria', 'Servicos'], n_linhas, p=[0.5, 0.3, 0.2]),
    'Data_Vencimento': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 90)) for _ in range(n_linhas)],
    'Valor_Boleto': np.random.uniform(100, 15000, n_linhas).round(2),
    'Dias_Atraso': np.random.choice([0, 5, 15, 30, 60, 90], n_linhas, p=[0.7, 0.1, 0.08, 0.05, 0.04, 0.03])
}

df = pd.DataFrame(data)

# Criando a coluna Status baseada nos dias de atraso
df['Status'] = df['Dias_Atraso'].apply(lambda x: 'Pago' if x == 0 else 'Em Aberto')

# Salvar CSV
df.to_csv('faturas_financeiro.csv', index=False)
print("Arquivo 'faturas_financeiro.csv' gerado com sucesso!")