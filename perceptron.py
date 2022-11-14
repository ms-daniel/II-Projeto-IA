from sklearn.linear_model import Perceptron


def learn(atributos_norm, diagnostico_norm):
    modelo = Perceptron()
    modelo.fit(atributos_norm, diagnostico_norm)
    return ('%.2f' % (modelo.score(atributos_norm, diagnostico_norm) * 100) + '%')
