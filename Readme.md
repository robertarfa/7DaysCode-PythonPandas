## Desafio #7DaysOfCode - Pandas

PS: Readme desenvolvido com GenIA fazendo a leitura do arquivo do código utilizando a biblioteca LangChain.

**Dia 1: Carregando os Dados e Primeiras Análises**

- **Descrição:**

  - Começo do desafio #7DaysOfCode com Pandas! 🎉
  - Apresentação do conjunto de dados: contexto, fonte, o que ele representa.
  - Carregamento do dataset utilizando Pandas (`pd.read_csv()`).
  - Exploração inicial: primeiras linhas (`df.head()`), informações gerais (`df.info()`), estatísticas descritivas (`df.describe()`).
  - Limpeza básica: verificar se existem dados duplicados, verificar se há dados faltantes (`df.isnull().sum()`) e decidir como lidar com eles (excluir linhas/colunas ou preencher).
  - Bases: mesclar as diferentes bases.

**Dia 2: Limpeza e Transformação de Dados com Pandas**

- **Descrição:**

  - Classificação CDU: Foi criada uma lista (`CDU_lista`) para classificar as localizações dos livros de acordo com a Classificação Decimal Universal (CDU).
  - Adição da classificação CDU: A lista `CDU_lista` foi adicionada como uma nova coluna (`CDU_classification`) no conjunto de dados `complete_data`.
  - Exclusão da coluna registro_sistema: A coluna `registro_sistema` foi removida do conjunto de dados `complete_data`.
  - Conversão da coluna matricula_ou_siape: A coluna `matricula_ou_siape` foi convertida de float para string.

  Essas ações visam organizar e padronizar os dados para que possam ser analisados de forma mais eficiente.

**Dia 3: Descobrindo Tendências e Padrões com Pandas**

- **Descrição:**
  - Tratamento de dados: O código começa convertendo as colunas `data_emprestimo`, `data_renovacao` e `data_devolucao` do tipo string para o tipo datetime.
  - Análise de empréstimos por ano: O código calcula a quantidade total de empréstimos por ano e armazena os resultados em um DataFrame chamado `emprestimos_por_ano_df`. Em seguida, gera um gráfico de linha para visualizar os resultados.
    ![alt text](image-1.png)
  - Análise de empréstimos por mês: O código calcula a quantidade total de empréstimos por mês e armazena os resultados em um DataFrame chamado `emprestimos_por_mes_df`. Em seguida, gera um gráfico de linha para visualizar os resultados.
    ![alt text](image-2.png)
  - Análise de empréstimos por hora: O código calcula a quantidade total de empréstimos por hora e armazena os resultados em um DataFrame chamado `emprestimos_por_hora_df`. Em seguida, gera um gráfico de barras para visualizar os resultados.
    ![alt text](image-3.png)

O objetivo do código é analisar a frequência de empréstimos ao longo do tempo e identificar tendências e padrões nos dados.

**DIA 4: Análise de Frequência e Média**

**Descrição:**

Neste dia, realizamos uma análise de frequência e média para entender melhor os padrões de empréstimo de exemplares na biblioteca. Utilizamos a biblioteca Pandas para gerar tabelas de frequência e gráficos de barras para visualizar os resultados.

**Análise de Frequência**

A análise de frequência nos permite entender como os empréstimos de exemplares estão distribuídos entre as diferentes variáveis categóricas. Neste dia, realizamos a análise de frequência para as seguintes variáveis:

- Tipo de vínculo do usuário
- Coleção
- Biblioteca
- Tema da CDU (Classificação Decimal Universal)

Os resultados mostram que:

- Os empréstimos de exemplares estão mais concentrados em usuários com vínculo de aluno e professor.
- As coleções mais emprestadas são as de literatura e ciências exatas.
- As bibliotecas com mais empréstimos são a Biblioteca Central e a Biblioteca de Ciências.
- Os temas mais emprestados são os de ciências exatas e literatura.
