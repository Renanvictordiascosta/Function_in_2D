# abertura de uma classe
class grafico_funcao:
    
    # definir função init
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # definir uma função para mostrar o gráfico
    def mostrar_funcao(self, x, y):
        import matplotlib.pyplot as plot
        plot.plot(x, y, color="blue", marker="o", linestyle="solid")
        plot.show()

    # função que terá os valores e os cálculos definidos
    def funcao(self, x, y):
        from time import sleep
        valor1 = grafico_funcao(x, y)
        try:
            print("Olá, esse é o programa de mostrar gráficos de funções em 2D!")
            sleep(3)
            print("É um teste feito pelo meu criador!")
            sleep(3)
            print("Você pode me moldar conforme achar melhor, para mostrar seus próprios gráficos!")
            sleep(3)
            while True:
                try:
                    print("Digite 1 para poder inserir um valor de x.")
                    sleep(3)
                    print("Digite 2 para sair da operação.")
                    sleep(3)
                    opicao = int(input("Digite sua opição: "))
                    if opicao == 1:
                      x1 = float(input("Digite o valor da variável x: "))
                      y1 = 3 * x1
                      valor1.x.append(x1)
                      valor1.y.append(y1)
                    elif opicao == 2:
                      print("Vejo que já terminou de definir os elementos da lista de x. Tenha um bom dia!")
                      sleep(3)
                      break
                    else:
                      print("O valor digitado não é válido!")
                      sleep(2)
                except ValueError:
                    print("Ocorreu um erro de valor!")
                    sleep(2)
        except KeyboardInterrupt:
            print("A operação foi interrompida pelo usuário!")
        print(valor1.x)
        sleep(3)
        print(valor1.y)
        sleep(3)

# atribuição a x e y como sendo listas
x = [ ]
y = [ ]

# atribuição baseada na função init
valor = grafico_funcao(x, y)

# chamada da função de atribuir valores
print(valor.funcao(x, y))

# chamada da função de mostrar o gráfico
print(valor.mostrar_funcao(x, y))