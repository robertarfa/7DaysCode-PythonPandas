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
# all_loan_data['id_emprestimo'].value_counts()

#eliminar emprestimos duplicados
all_loan_data = all_loan_data.drop_duplicates()
# all_loan_data['id_emprestimo'].value_counts()

# view_duplicate = all_loan_data[all_loan_data['id_emprestimo'] == 709705]

#Importar dados livros
books_data = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')

# books_data.value_counts()

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
# complete_data.info()
complete_data['matricula_ou_siape'] = complete_data['matricula_ou_siape'].astype('string')

######DIA 3######
# complete_data.head()

# complete_data.isna().sum()

# verifique qual é a quantidade total de exemplares emprestados por 
#cada ano e plote um gráfico de linhas.

data_emprestimo = pd.Series(complete_data['data_emprestimo'])
complete_data['data_emprestimo'] = pd.to_datetime(data_emprestimo)

complete_data['data_renovacao'] = pd.to_datetime(complete_data['data_renovacao'])
complete_data['data_devolucao'] = pd.to_datetime(complete_data['data_devolucao'])

# complete_data.head()

# complete_data['data_emprestimo'].dt.year

# len(complete_data['id_exemplar'])

emprestimos_data = pd.DataFrame(complete_data['data_emprestimo'].value_counts()).reset_index()
emprestimos_data.columns = ['data','quantidade']
emprestimos_data['data'] = pd.to_datetime(emprestimos_data['data'])
# emprestimos_data

emprestimos_por_ano = emprestimos_data.groupby(by=emprestimos_data.data.dt.year)['quantidade'].sum()
emprestimos_por_ano.index.name = 'ano'
# emprestimos_por_ano

import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

emprestimos_por_ano_df = emprestimos_por_ano.reset_index()


# ax = sns.lineplot(data=emprestimos_por_ano_df,x='ano',y='quantidade', linewidth=3, color='green')
# ax.set_title('Número de Empréstimos por Ano')
# ax.set(xlabel="Ano",ylabel="Número de Empréstimos")
# ax.tick_params(axis='x', rotation=45)
# plt.show()

#gere uma tabela com a quantidade total de exemplares emprestados por mês
#férias em janeiro, dezembro e julho
# emprestimos_por_mes = emprestimos_data.groupby(by=emprestimos_data.data.dt.month)['quantidade'].sum()
# emprestimos_por_mes.index.name = 'mes'
# emprestimos_por_mes_df = emprestimos_por_mes.reset_index()

# ax = sns.lineplot(data=emprestimos_por_mes_df,x='mes',y='quantidade', linewidth=3, color='red')
# ax.set_title('Número de Empréstimos por Mês')
# ax.set(xlabel="Mês",ylabel="Número de Empréstimos")
# ax.tick_params(axis='x', rotation=45)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# plt.show()

# emprestimos_por_hora = emprestimos_data.groupby(by=emprestimos_data.data.dt.hour)['quantidade'].sum()
# emprestimos_por_hora.index.name = 'horas'
# emprestimos_por_hora_df = emprestimos_por_hora.reset_index()
# emprestimos_por_hora_df

# ax = sns.barplot(data=emprestimos_por_hora_df,x='horas',y='quantidade', linewidth=3, color='blue')
# ax.set_title('Número de Empréstimos por Hora')
# ax.set(xlabel="Hora",ylabel="Número de Empréstimos")
# ax.tick_params(axis='x', rotation=45)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# plt.show()

######DIA 4######

# def analise_frequencia(variavel):
#   '''
#   Esta função irá gerar uma tabela de frequência com percentuais de acordo 
#   com a variável passada, além de um gráfico de barras.

#   variavel = variável categórica escolhida de dentro do conjunto de dados 
#   complete_data
#   '''

#   dataframe = pd.DataFrame(complete_data[variavel].value_counts())                      
#   dataframe.columns = ['quantidade']
#   dataframe['percentual'] = round((dataframe.quantidade / dataframe.quantidade.sum())*100,1)
#   dataframe = dataframe.reset_index() # Aqui você precisa atribuir o resultado de reset_index()
  
#   ax = sns.barplot(y=dataframe[variavel], x=dataframe['percentual'])
#   plt.xlabel(variavel) # Adicione rótulo ao eixo X
#   plt.ylabel('Percentual') # Adicione rótulo ao eixo Y
#   plt.title('Frequência de {} em Porcentagem'.format(variavel)) # Adicione título ao gráfico
#   plt.xticks(rotation=45, ha='right') # Ajuste o layout dos rótulos do eixo X

#   plt.show()

#   return dataframe

#Como se distribuem os empréstimos de exemplares 
#pelos tipos de vínculo dos usuários

# analise_frequencia('tipo_vinculo_usuario')

#Quais coleções são mais emprestadas?

# analise_frequencia('colecao')

# Quais são as bibliotecas com mais ou menos quantidade de empréstimos?
# analise_frequencia('biblioteca')

#De quais temas da CDU são os exemplares emprestados?
# analise_frequencia('CDU_classification')

#Quanto tempo os livros ficam emprestados
complete_data['tempo_emprestimo'] = complete_data['data_devolucao']-complete_data['data_emprestimo']

# def analise_media_frequencia(variavel):
#   '''
#   Esta função irá gerar uma tabela de frequência com percentuais de acordo 
#   com a variável passada, além de um gráfico de barras.

#   variavel = variável categórica escolhida de dentro do conjunto de dados 
#   complete_data
#   '''

#   dataframe = pd.DataFrame(complete_data[variavel].value_counts())                      
#   dataframe.columns = ['quantidade']
#   dataframe['media'] = complete_data.groupby(variavel)['tempo_emprestimo'].mean().sort_values(ascending=False)
#   dataframe = dataframe.reset_index() # Aqui você precisa atribuir o resultado de reset_index()
  
#   # Inverter o eixo y:
#   ax = sns.barplot(x=dataframe[variavel], y=dataframe['media'])
#   plt.xlabel('Média de dias de empréstimo') # Adicione rótulo ao eixo X
#   plt.ylabel('') # Adicione rótulo ao eixo Y
#   plt.title('Média de dias de empréstimo por {}'.format(variavel)) # Adicione título ao gráfico
#   plt.xticks(rotation=45, ha='right') # Ajuste o layout dos rótulos do eixo X
#   # Inverter o eixo Y:
#   plt.gca().invert_yaxis() 
#   plt.show()

#   return dataframe

# analise_media_frequencia('biblioteca')
# analise_media_frequencia('tipo_vinculo_usuario')

# complete_data.info()

######DIA 5######

# fazer dois recortes em seus dados para entender como eles se distribuíram ao decorrer desses anos

# alunos de graduação e pós graduação a distribuição de empréstimos mensais por ano realizados 
#entre 2010 e 2020 da coleção que tiver a maior frequência de empréstimos.

# complete_data.head()

##Graduação
# alunos_graduacao = complete_data.query('tipo_vinculo_usuario == "ALUNO DE GRADUAÇÃO"')
# alunos_graduacao.colecao.value_counts()

# alunos_graduacao_acervo_circulante = alunos_graduacao.query('colecao == "Acervo Circulante"')
# alunos_graduacao_acervo_circulante = pd.DataFrame(alunos_graduacao_acervo_circulante)
# alunos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_graduacao_acervo_circulante['data_emprestimo'])
# alunos_graduacao_acervo_circulante['ano'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.year
# alunos_graduacao_acervo_circulante['mes'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.month
# alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.loc[:,['ano','mes']]
# alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()

# def gera_box_plot(dataset,x,y,titulo,subtitulo):
#   '''
#   Esta função irá gerar um gráfico de boxplot.

#   Dataset = conjunto de dados do gráfico
#   x = valor do eixo x do gráfico
#   y = valor do eixo y do gráfico
#   título = título do gráfico
#   subtitulo = subtitulo do texto
#   '''

#   sns.set_theme(style="darkgrid", palette='Blues',font_scale=1.3)                    
#   plt.figure(figsize=(16,10))                                                           

#   ax = sns.boxplot(y= y, x= x, data= dataset,color='#4171EF')                                           
#   ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))                


#   plt.ylim(0,max(dataset[y])*1.1)                                               #Definir o limite do eixo y
#   plt.xlabel(None)                                                                     
#   plt.ylabel(None)                                                                    

#   ax.set_title(titulo+"\n",size=20,loc='left',weight='bold')
#   ax.text(s=subtitulo,x=-0.5,y=max(dataset[y])*1.11,fontsize=18, ha='left',color='gray')  
  
#   gera_box_plot(alunos_graduacao_acervo_circulante,'ano','quantidade','Distribuição dos empréstimos mensais', 'Realizados pelos alunos de graduação no acervo circulante')
  
  #Pós Graduação

  
# alunos_pos_graduacao = complete_data.query('tipo_vinculo_usuario == "ALUNO DE PÓS-GRADUAÇÃO"')
# alunos_pos_graduacao.colecao.value_counts()


# alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao.query('colecao == "Acervo Circulante"')
# alunos_pos_graduacao_acervo_circulante = pd.DataFrame(alunos_pos_graduacao_acervo_circulante)
# alunos_pos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_pos_graduacao_acervo_circulante['data_emprestimo'])
# alunos_pos_graduacao_acervo_circulante['ano'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.year
# alunos_pos_graduacao_acervo_circulante['mes'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.month
# alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.loc[:,['ano','mes']]
# alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()
# # alunos_pos_graduacao_acervo_circulante

# gera_box_plot(alunos_pos_graduacao_acervo_circulante,'ano','quantidade','Distribuição dos empréstimos mensais', 'Realizados pelos alunos de pós graduação no acervo circulante')

###DIA 6 ###

# calcular a quantidade de empréstimos realizados entre 2015 e 2020 
#por cada curso de graduação que passará pela avaliação.
# Biblioteconomia
# Ciências sociais
# Comunicação social
# Direito
# Filosofia
# Pedagogia

matricula_alunos_plan = 'matricula_alunos.xlsx'

cadastro_usuarios_json = "https://raw.githubusercontent.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/main/Dia_6-Novos_dados_novas_analises/Datasets/cadastro_alunos.json?utm_medium=email&_hsenc=p2ANqtz-9LbQ_ZLKK4VfdCieRRAGTcKjuzY2tltzcbNN96naXXOE1N7sR2YOrWFZufEs7EIfYn5Shkt8o1AhrPjF9wa_cSNAEMWQ&_hsmi=270881120&utm_content=270881120&utm_source=hs_automation"

matricula_alunos_excel = pd.ExcelFile(matricula_alunos_plan)
numero_de_abas = len(matricula_alunos_excel.sheet_names)
matricula_alunos_sheet_names = matricula_alunos_excel.sheet_names

matricula_alunos_ate_2010 = pd.read_excel(matricula_alunos_plan, sheet_name=matricula_alunos_sheet_names[0],skiprows=1)
matricula_alunos_apos_2010 = pd.read_excel(matricula_alunos_plan, sheet_name=matricula_alunos_sheet_names[1],skiprows=1)

matricula_alunos_ate_2010.columns = ['matricula_ou_siape','tipo_vinculo_usuario','curso']
matricula_alunos_apos_2010.columns = ['matricula_ou_siape','tipo_vinculo_usuario','curso']
# matricula_alunos_ate_2010.info()

cadastro_usuarios_excel = pd.concat([matricula_alunos_ate_2010,matricula_alunos_apos_2010],ignore_index=True)
cadastro_usuarios_excel.matricula_ou_siape = cadastro_usuarios_excel.matricula_ou_siape.astype('string')
# cadastro_usuarios_excel.info()

cadastro_usuarios = pd.read_json(cadastro_usuarios_json)

cadastro_usuarios_graduacao_json = pd.read_json(cadastro_usuarios.registros[0])
cadastro_usuarios_graduacao_json.matricula_ou_siape = cadastro_usuarios_graduacao_json.matricula_ou_siape.astype('float')
cadastro_usuarios_graduacao_json.matricula_ou_siape = cadastro_usuarios_graduacao_json.matricula_ou_siape.astype('string')
     
# cadastro_usuarios_graduacao_json.info()

cadastro_usuarios_cursos = pd.concat([cadastro_usuarios_excel,cadastro_usuarios_graduacao_json],ignore_index=True)


matricula_data_de_emprestimo = complete_data.query("tipo_vinculo_usuario == 'ALUNO DE GRADUAÇÃO'")
matricula_data_de_emprestimo = matricula_data_de_emprestimo.loc[:,['matricula_ou_siape','data_emprestimo']]
matricula_data_de_emprestimo = matricula_data_de_emprestimo.query('data_emprestimo > 2015')
matricula_data_de_emprestimo = matricula_data_de_emprestimo.reset_index(drop=True)
matricula_data_de_emprestimo

matricula_data_de_emprestimo.isna().sum()
matricula_data_de_emprestimo = matricula_data_de_emprestimo.dropna()

cursos = ['BIBLIOTECONOMIA','CIÊNCIAS SOCIAIS','COMUNICAÇÃO SOCIAL','DIREITO','FILOSOFIA','PEDAGOGIA']

cadastro_usuarios_cursos_selecionados = cadastro_usuarios_cursos.query("curso == ['BIBLIOTECONOMIA','CIÊNCIAS SOCIAIS','COMUNICAÇÃO SOCIAL','DIREITO','FILOSOFIA','PEDAGOGIA']")
# cadastro_usuarios_cursos_selecionados


cadastro_usuarios_cursos_selecionados = matricula_data_de_emprestimo.merge(cadastro_usuarios_cursos_selecionados)
# cadastro_usuarios_cursos_selecionados

cadastro_usuarios_cursos_selecionados.data_emprestimo = cadastro_usuarios_cursos_selecionados.data_emprestimo.dt.year


emprestimos_cursos_selecionados = cadastro_usuarios_cursos_selecionados.iloc[:,[1,3]].value_counts().reset_index()
emprestimos_cursos_selecionados.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']
# emprestimos_cursos_selecionados
     
emprestimos_tipo_usuario_curso_pivot = emprestimos_cursos_selecionados.pivot_table(
        index = 'CURSO',
        columns = 'ANO',
        values = 'QUANTIDADE_EMPRESTIMOS',
        fill_value = '-',
        aggfunc= sum,
        margins = True,
        margins_name = 'TOTAL',
)
# emprestimos_tipo_usuario_curso_pivot

###DIA 7 ###

#diferença percentual de empréstimos realizados 
#nos últimos anos (2017, 2018, 2019) para cada curso.
cadastro_usuarios_pos_graduacao_json = pd.read_json(cadastro_usuarios.registros[1])
cadastro_usuarios_pos_graduacao_json.matricula_ou_siape = cadastro_usuarios_pos_graduacao_json.matricula_ou_siape.astype('float')
cadastro_usuarios_pos_graduacao_json.matricula_ou_siape = cadastro_usuarios_pos_graduacao_json.matricula_ou_siape.astype('string')
    
cadastro_usuarios_pos_graduacao_json.info()
cadastro_usuarios_cursos_pos = pd.concat([cadastro_usuarios_excel,cadastro_usuarios_pos_graduacao_json],ignore_index=True)


matricula_data_de_emprestimo_pos = complete_data.query("tipo_vinculo_usuario == 'ALUNO DE PÓS-GRADUAÇÃO'")
matricula_data_de_emprestimo_pos = matricula_data_de_emprestimo_pos.loc[:,['matricula_ou_siape','data_emprestimo']]
matricula_data_de_emprestimo_pos = matricula_data_de_emprestimo_pos.query('data_emprestimo > 2017')
matricula_data_de_emprestimo_pos = matricula_data_de_emprestimo_pos.reset_index(drop=True)
matricula_data_de_emprestimo_pos

matricula_data_de_emprestimo_pos.isna().sum()
matricula_data_de_emprestimo_pos = matricula_data_de_emprestimo_pos.dropna()

emprestimos_pos_graduacao_desde_2017 = matricula_data_de_emprestimo_pos.merge(cadastro_usuarios_cursos_pos)
emprestimos_pos_graduacao_desde_2017


emprestimos_pos_graduacao_desde_2017.data_emprestimo = emprestimos_pos_graduacao_desde_2017.data_emprestimo.dt.year


emprestimos_pos_graduacao_desde_2017 = emprestimos_pos_graduacao_desde_2017.iloc[:,[1,3]].value_counts().reset_index()
emprestimos_pos_graduacao_desde_2017.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']
emprestimos_pos_graduacao_desde_2017
# emprestimos_cursos_selecionados
     
emprestimos_pos_graduacao_e_curso_pivot = emprestimos_pos_graduacao_desde_2017.pivot_table(
        index = 'CURSO',
        columns = 'ANO',
        values = 'QUANTIDADE_EMPRESTIMOS'
)
# emprestimos_pos_graduacao_e_curso_pivot

previsao_2022 = "https://raw.githubusercontent.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/refs/heads/main/Dia_7-Apresentando_resultados_em_HTML/Dataset/previsao"

previsao_2022_df = pd.read_table(previsao_2022)

previsao_2022_df = previsao_2022_df['curso previsao_2022'].str.split(' ',expand=True)

#criar uma tabela com as diferenças percentuais de 
#empréstimos entre 2017-2018, 2018-2019, 2019-2022.

previsao_2022_df.index = emprestimos_pos_graduacao_e_curso_pivot.index
emprestimos_pos_graduacao_e_curso_pivot['2022'] = previsao_2022_df.iloc[:,1]
emprestimos_pos_graduacao_e_curso_pivot.info()


year_cols = [col for col in emprestimos_pos_graduacao_e_curso_pivot.columns]
emprestimos_pos_graduacao_e_curso_pivot[year_cols] = emprestimos_pos_graduacao_e_curso_pivot[year_cols].astype(int)  

def diferenca_percentual_ano_anterior(x,y):
  return round(((x / y * 100) - 100),2)

emprestimos_pos_graduacao_e_curso_pivot.iloc[:,0]
percentual_2018 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,1],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,0])
percentual_2019 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,2],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,1])
percentual_2022 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,3],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,2])

percentual = pd.DataFrame({'2018':percentual_2018,
                           '2019':percentual_2019,
                           '2022':percentual_2022})


percentual.reset_index(inplace=True)
percentual.columns = percentual.columns.str.capitalize()
percentual.Curso = percentual.Curso.str.capitalize()

percentual.style

th_props = [
  ('font-size', '1.4rem'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'whitesmoke'),
  ('background-color', '#001692'),
  ('border-radius', '0.25rem'),
  ('box-shadow','0 0 1rem gray')
  ]

td_props = [
  ('font-size', '1rem'),
  ('padding','0.5rem'),
  ('text-align', 'left'),
  ('font-weight', 'bold'),
  ('border-bottom','0.1rem solid lightgray')
  ]

styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

#ajuste para versão mais recente do pandas

# percentual.style.text_gradient(cmap='RdYlGn', low=1, axis=1, vmax=0.1, vmin=0)\
#     .format('{:.2f} %', subset=['2018', '2019', '2022'])\
#     .hide(axis="index")\  
#     .set_table_styles(styles)\
#     .to_html('teste.html', doctype_html=True,
#              table_attributes='ALIGN=LEFT WIDTH=50% CELLSPACING = 5')

percentual.style.text_gradient(cmap='RdYlGn',low=1, axis=1,vmax=0.1,vmin=0)\
                              .format('{:.2f} %',subset=['2018','2019','2022'])\
                              .hide(axis="index")\
                              .set_table_styles(styles)\
                              .to_html('teste.html',doctype_html =True,
                                       table_attributes='ALIGN=LEFT WIDTH=50% CELLSPACING = 5')