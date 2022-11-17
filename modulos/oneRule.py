from mlxtend.classifier import OneRClassifier


def learn(atributos_norm, diagnostico_norm):
    modelo = OneRClassifier()
    modelo.fit(atributos_norm.astype(int), diagnostico_norm.astype(int))
    return ('%.2f' % (modelo.score(atributos_norm, diagnostico_norm) * 100) + '%')
