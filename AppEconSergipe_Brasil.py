import pandas as pd
import plotly.express as px

# Função para converter strings numéricas para floats
def converter_para_float(valor):
    if isinstance(valor, str):
        valor = valor.replace('.', '').replace(',', '.')
    try:
        return float(valor)
    except ValueError:
        return valor

# Ler os dados do arquivos CSV e exibir no terminal
EconDataSet = pd.read_csv('EconDataSet.csv', converters={
    'ANO': converter_para_float,
    'PIB_BRASIL': converter_para_float,
    'PIB_SERGIPE': converter_para_float,
    'PERCAPITA_BRASIL': converter_para_float,
    'PERCAPTA_SERGIPE': converter_para_float
})

print("Dados do Estado de Sergipe:")
print(EconDataSet)


df_pandas = EconDataSet

# Criação dos gráficos 
def criar_graficos(df):

    df['PIB_BRASIL'] = df['PIB_BRASIL'] * 1e6 #PIB EM TRILHÕES DE REAIS
    df['PIB_SERGIPE'] = df['PIB_SERGIPE'] * 1e6 #PIB EM BILHOES DE REAIS

    
    
    fig_PIB_BRASIL = px.line(df, x='ANO', y=['PIB_BRASIL'], 
        title="Evolução do PIB do Brasil de 2000 a 2021 (em Trilhões de Reais)")  
    fig_PIB_BRASIL.update_layout(yaxis_title='PIB do Brasil (Trilhões de Reais)', xaxis_title='ANO')
    fig_PIB_BRASIL.show()


    fig_PIB_SERGIPE = px.line(df, x='ANO', y=['PIB_SERGIPE'], 
        title="Evolução do PIB de Sergipe de 2000 a 2021 (em Bilhões de Reais)")   
    fig_PIB_SERGIPE.update_layout(yaxis_title='PIB de Sergipe (Bilhões de Reais)', xaxis_title='ANO')
    fig_PIB_SERGIPE.show()


    fig_PERCAPITA_BRASIL = px.line(df, x='ANO', y=['PERCAPITA_BRASIL'], 
        title="Pib Per Capita (Brasil) de 2000 a 2021 ")
    fig_PERCAPITA_BRASIL.update_layout(yaxis_title='Brasil (Milhares de Reais)', xaxis_title='ANO')
    fig_PERCAPITA_BRASIL.show()

    fig_PERCAPITA_SERGIPE = px.line(df, x='ANO', y=['PERCAPITA_SERGIPE'], 
        title="Pib Per Capita (Sergipe) de 2000 a 2021 ")
    fig_PERCAPITA_SERGIPE.update_layout(yaxis_title='Sergipe (Milhares de Reais)', xaxis_title='ANO')
    fig_PERCAPITA_SERGIPE.show()
    
    fig_COMPARACAO = px.line(df, x='ANO', y=['PERCAPITA_BRASIL', 'PERCAPITA_SERGIPE'], 
        title="Comparação do Pib Per Capita (Brasil vs Sergipe) de 2000 a 2021 ")
    fig_COMPARACAO.update_layout(yaxis_title='Brasil vs Sergipe (Milhares de Reais)', xaxis_title='ANO')
    fig_COMPARACAO.show()



# Chamada para exibir os gráficos
criar_graficos(df_pandas)