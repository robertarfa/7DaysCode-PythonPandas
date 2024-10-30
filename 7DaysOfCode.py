import pandas as pd
#objetivo
# A quantidade de empréstimos está aumentando ou diminuindo ao decorrer dos últimos anos?
# Em quais bibliotecas do sistema estão a maior quantidade de empréstimos?
# Quais são os temas mais emprestados? E os menos?

######DIA 1######
#Importar dados
dados_2010_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20101.csv?raw=true')
dados_2010_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20102.csv?raw=true')
dados_2011_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20111.csv?raw=true')
dados_2011_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20112.csv?raw=true')
dados_2012_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20121.csv?raw=true')
dados_2012_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20122.csv?raw=true')
dados_2013_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20131.csv?raw=true')
dados_2013_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20132.csv?raw=true')
dados_2014_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20141.csv?raw=true')
dados_2014_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20142.csv?raw=true')
dados_2015_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20151.csv?raw=true')
dados_2015_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20152.csv?raw=true')
dados_2016_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20161.csv?raw=true')
dados_2016_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20162.csv?raw=true')
dados_2017_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20171.csv?raw=true')
dados_2017_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20172.csv?raw=true')
dados_2018_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20181.csv?raw=true')
dados_2018_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20182.csv?raw=true')
dados_2019_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20191.csv?raw=true')
dados_2019_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20192.csv?raw=true')
dados_2020_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20201.csv?raw=true')

#Unificar tabelas
all_loan_data = pd.concat([dados_2010_1,
dados_2010_2,
dados_2011_1,
dados_2011_2,
dados_2012_1,
dados_2012_2,
dados_2013_1,
dados_2013_2,
dados_2014_1,
dados_2014_2,
dados_2015_1,
dados_2015_2,
dados_2016_1,
dados_2016_2,
dados_2017_1,
dados_2017_2,
dados_2018_1,
dados_2018_2,
dados_2019_1,
dados_2019_2,
dados_2020_1],ignore_index=True)

# all_loan_data.info()

#Verificar se existe empréstimo duplicado
all_loan_data['id_emprestimo'].value_counts()

#eliminar emprestimos duplicados
all_loan_data = all_loan_data.drop_duplicates()
all_loan_data['id_emprestimo'].value_counts()

view_duplicate = all_loan_data[all_loan_data['id_emprestimo'] == 709705]

#Importar dados livros
books_data = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')

books_data.value_counts()

complete_data = all_loan_data.merge(books_data)

######DIA 2######
CDU_lista = []
for location in complete_data['localizacao']:
  match location:
    case n if 0 <= n <= 99:
      CDU_lista.append("Generalidades. Ciência e conhecimento")
    case n if 100 <= n <= 199:
      CDU_lista.append("Filosofia e psicologia")
    case n if 200 <= n <= 299:
      CDU_lista.append("Religião")
    case n if 300 <= n <= 399:
      CDU_lista.append("Ciências sociais")
    case n if 400 <= n <= 499:
      CDU_lista.append("Classe vaga. Provisoriamente não ocupada")
    case n if 500 <= n <= 599:
      CDU_lista.append("Matemática e ciências naturais")
    case n if 600 <= n <= 699:
      CDU_lista.append("Ciências aplicadas")
    case n if 700 <= n <= 799:
      CDU_lista.append("Belas artes")
    case n if 800 <= n <= 899:
      CDU_lista.append("Linguagem. Língua. Linguística")
    case n if 900 <= n <= 999:
      CDU_lista.append("Geografia. Biografia. História")
    case _: # Caso nenhum dos casos acima seja correspondido
      CDU_lista.append("Classificação CDU não encontrada")

complete_data['CDU_classification'] = CDU_lista

#excluir coluna registro_sistema
complete_data.drop(columns=['registro_sistema'],inplace=True)

#Transformar-a coluna matricula_ou_siape está como floeat, tranformar String
complete_data.info()
complete_data['matricula_ou_siape'] = complete_data['matricula_ou_siape'].astype('string')

######DIA 3######
complete_data.head()

complete_data.isna().sum()

# verifique qual é a quantidade total de exemplares emprestados por 
#cada ano e plote um gráfico de linhas.

data_emprestimo = pd.Series(complete_data['data_emprestimo'])
complete_data['data_emprestimo'] = pd.to_datetime(data_emprestimo)

complete_data['data_renovacao'] = pd.to_datetime(complete_data['data_renovacao'])
complete_data['data_devolucao'] = pd.to_datetime(complete_data['data_devolucao'])

complete_data.head()

complete_data['data_emprestimo'].dt.year

len(complete_data['id_exemplar'])

emprestimos_data = pd.DataFrame(complete_data['data_emprestimo'].value_counts()).reset_index()
emprestimos_data.columns = ['data','quantidade']
emprestimos_data['data'] = pd.to_datetime(emprestimos_data['data'])
emprestimos_data

emprestimos_por_ano = emprestimos_data.groupby(by=emprestimos_data.data.dt.year)['quantidade'].sum()
emprestimos_por_ano.index.name = 'ano'
emprestimos_por_ano

import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

emprestimos_por_ano_df = emprestimos_por_ano.reset_index()


ax = sns.lineplot(data=emprestimos_por_ano_df,x='ano',y='quantidade', linewidth=3, color='green')
ax.set_title('Número de Empréstimos por Ano')
ax.set(xlabel="Ano",ylabel="Número de Empréstimos")
ax.tick_params(axis='x', rotation=45)
plt.show()

#gere uma tabela com a quantidade total de exemplares emprestados por mês
#férias em janeiro, dezembro e julho
emprestimos_por_mes = emprestimos_data.groupby(by=emprestimos_data.data.dt.month)['quantidade'].sum()
emprestimos_por_mes.index.name = 'mes'
emprestimos_por_mes_df = emprestimos_por_mes.reset_index()

ax = sns.lineplot(data=emprestimos_por_mes_df,x='mes',y='quantidade', linewidth=3, color='red')
ax.set_title('Número de Empréstimos por Mês')
ax.set(xlabel="Mês",ylabel="Número de Empréstimos")
ax.tick_params(axis='x', rotation=45)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()

emprestimos_por_hora = emprestimos_data.groupby(by=emprestimos_data.data.dt.hour)['quantidade'].sum()
emprestimos_por_hora.index.name = 'horas'
emprestimos_por_hora_df = emprestimos_por_hora.reset_index()
emprestimos_por_hora_df

ax = sns.barplot(data=emprestimos_por_hora_df,x='horas',y='quantidade', linewidth=3, color='blue')
ax.set_title('Número de Empréstimos por Hora')
ax.set(xlabel="Hora",ylabel="Número de Empréstimos")
ax.tick_params(axis='x', rotation=45)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()