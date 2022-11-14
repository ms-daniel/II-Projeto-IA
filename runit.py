import pandas as pd
from sklearn import preprocessing
import perceptron
import knn
import oneRule

accurateKNN = 0
accuratePerceptron = 0
accurateOneR = 0


def run_it(csv, separator, neighbors):
    base_Treinamento = pd.read_csv(csv, sep = separator, encoding='latin1').values
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
