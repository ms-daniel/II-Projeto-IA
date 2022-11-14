import validation

url = 'https://raw.githubusercontent.com/lauro-ss/Exercicio-IA-Rede-Neural/main/base_de_dados_diabetes.csv'
validation.validar(url)
print(validation.accuratePerceptron)
print(validation.accurateKNN)
print(validation.accurateOneR)
