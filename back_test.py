import runit

#
#
def test(url, separator, neighbors, varPercept, varKnn, varOneR):
    """
        calculates the accuracy for the classifierless perceptron model, with the KNN classifier and the One Rule

        :param url:         string
        :param separator:   string
        :param neighbors:   int
        :param varPercept:  StringVar(tkinter)
        :param varKnn:      StringVar(tkinter)
        :param varOneR:     StringVar(tkinter)
    """
    runit.run_it(url)
    print(runit.accuratePerceptron)
    print(runit.accurateKNN)
    print(runit.accurateOneR)
