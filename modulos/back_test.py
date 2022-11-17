from modulos import runit
from tkinter import StringVar
#
#
def test(url, separator, neighbors, listVar):
    """
        calculates the accuracy for the classifierless perceptron model, with the KNN classifier and the One Rule

        :param url:         string
        :param separator:   string
        :param neighbors:   int
        :param listVar:     StringVar list(0 = perceptron, 1 = knn, 2 = oneRule)
    """

    runit.run_it(url, separator, neighbors)

    listVar[0].set(runit.accuratePerceptron)
    listVar[1].set(runit.accurateKNN)
    listVar[2].set(runit.accurateOneR)
