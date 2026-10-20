import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('CHURN_TRATADO.csv', delimiter=',' )

df = df.replace({'Yes':1,'No':0})
df = df.replace({'No internet service':0})
df = df.drop(columns=['Servico_Telefonico'])

colunas = ['Servico_Seguranca','Suporte_Tecnico','StreamingTV','Casado','Dependentes','Churn']

df[colunas] = df[colunas].astype(int)

df_qualitativas = [
    'Tempo_como_Cliente',
    'Pagamento_Mensal',
    'Total_Pago'
]

for coluna in df_qualitativas:
    media_churn = df.groupby('Churn')[df_qualitativas].mean()

    fig = px.bar(
        df,
        x='Variável Qualitativa',
        y='Média de Churn',
        text='Variável',
        color='Média',
        title=f"Média de Churn por {df_qualitativas}",
        labels={
            'Variável': df_qualitativas,
            'Média': media_churn
        }

    )

    fig.update_yaxes(
        tickprefix="R$ ",
        tickformat=",.2f"
    )

    fig.update_layout(
        separators=",."
    )

    fig.show()



