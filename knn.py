from sklearn.neighbors import KNeighborsClassifier


def learn(atributos_norm, diagnostico_norm):
    modelo = KNeighborsClassifier(n_neighbors=1)
    modelo.fit(atributos_norm, diagnostico_norm)
    return ('%.2f' % (modelo.score(atributos_norm, diagnostico_norm) * 100) + '%')
