import pandas as pd
#objetivo
# A quantidade de empréstimos está aumentando ou diminuindo ao decorrer dos últimos anos?
# Em quais bibliotecas do sistema estão a maior quantidade de empréstimos?
# Quais são os temas mais emprestados? E os menos?

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

# # --- Analisar dados ---
# books_data_copy = books_data.copy()

# duplicados_id_exemplar = books_data_copy['id_exemplar'].value_counts() > 1
# livros_duplicados = duplicados_id_exemplar[duplicados_id_exemplar == True]

# itens_duplicados = pd.merge(livros_duplicados, books_data_copy, on='id_exemplar')

# itens_duplicados_filtrados = itens_duplicados[itens_duplicados.duplicated(subset=['id_exemplar'], keep=False)]

# # --- Criar filtro para remoção ---
# # 1. Marcar linhas com 'codigo_barras' contendo ":" em 'itens_duplicados_filtrados'
# itens_duplicados_filtrados['remover'] = itens_duplicados_filtrados['codigo_barras'].str.contains("/", case=True)
# # 2. Filtrar as linhas a serem removidas
# linhas_para_remover = itens_duplicados_filtrados[itens_duplicados_filtrados['remover'] == True]
# # 3. Obter os índices das linhas a serem removidas no DataFrame ORIGINAL ('books_data_copy')
# indices_para_remover = books_data_copy[books_data_copy['id_exemplar'].isin(linhas_para_remover['id_exemplar'])].index

# # --- Remover as linhas ---
# books_data_ok = books_data_copy.drop(index=indices_para_remover, inplace=True) 

# view = books_data_copy[books_data_copy['id_exemplar'] == 206184]