# MLearning-

Building Models:
1) Definir o modelo (DEFINE)
2) Treinar o modelo (FIT)
  Fitting or Training:  Capturar padrões nos dados.
  Training Data (80%):  Dados usados para treinar o modelo.
3) Fazer previses (PREDICT)
  Aplicar o modelo treinando na parte não vista (20%) dos dados.
4) Validar modelo (VALIDATE)
  Determine how accurate the model's predictions are.

Tipo de modelos:
1) Decision Trees
  Ponto final, onde ocorrem as previsões são as folhas (Leafs)
2) Features(columns lists) and Prediction target

Treinando o modelo:
1) escolhendo coluna para ser (Prediction)Target Variable; y = DATA_FRAME.column_name
2) escolhendo colunas para serem as features;  X = DATA_FRAME[columns_names1, columns_names2, columns_names3, etc]
3) Importando lib do modelo: from sklearn.tree import DecisionTreeRegressor
4) Especificando modelo e atribuindo um state fixo.  name_model = DecisionTreeRegressor(random_state=1)
(Specify a number for random_state to ensure same results each run)
5) Treinando o modelo:  name_model.fit(X, y)



Previsões usando o modelo treinando
1) predictions = name_model.predict(X.head()); onde X.head() são as primeiras linhas... usar as linhas desejadas aqui. ex.: (X)


Avaliar (Validar)
1) Summarize comparing Prediction vs Real Data into a single metric. Vejamos alguns tipos:
1.1) Mean Absolute Error (also called MAE). 
1.2) metrics lib: from sklearn.metrics import mean_absolute_error  (MAE)
  predicted_home_prices = melbourne_model.predict(X)
  mean_absolute_error(y, predicted_home_prices)


Pandas:
1) import pandas as pd
2) pd.read_csv(PATH_to_FILE) load data into DataFrames

Scikit-learn 
The most popular library for modeling the types of data typically stored in DataFrames.

