import pandas as pd
from sklearn import preprocessing
from modulos import perceptron
from modulos import knn
from modulos import oneRule

accurateKNN = 0
accuratePerceptron = 0
accurateOneR = 0


def run_it(csv, separator, neighbors, removeds):
    csv = pd.read_csv(csv, sep = separator, encoding='latin1')
    for x in removeds:
        csv.pop(x)

    base_Treinamento = csv.to_numpy()

    # número de linhas e colunas do arquivo
    row_count, column_count = base_Treinamento.shape

    # Por padrão a última coluna é sempre a coluna de resultados
    fim = column_count-1

    # Normalização
    min_max = preprocessing.MinMaxScaler()
    atributos_norm = min_max.fit_transform(base_Treinamento[:, :fim])
    diagnostico_norm = base_Treinamento[:, fim]

    global accuratePerceptron
    accuratePerceptron = perceptron.learn(atributos_norm, diagnostico_norm)
    global accurateKNN
    accurateKNN = knn.learn(atributos_norm, diagnostico_norm, neighbors)
    global accurateOneR
    accurateOneR = oneRule.learn(atributos_norm, diagnostico_norm)
