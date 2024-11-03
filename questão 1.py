import turtle

# Classe base Forma
class Forma:
    def desenhar(self):
        raise NotImplementedError("Este método deve ser sobrescrito por subclasses")

# Classe Circulo usando Turtle
class Circulo(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(0, -50)  # Posiciona o cursor para que o círculo fique centralizado
        turtle.pendown()
        turtle.circle(50)    # Desenha o círculo com raio de 50

# Classe Quadrado usando Turtle
class Quadrado(Forma):
    def desenhar(self):
        turtle.penup()
        turtle.goto(-50, -50)  # Posiciona o cursor para o canto inferior esquerdo do quadrado
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)  # Desenha um lado do quadrado
            turtle.left(90)      # Vira o ângulo para o próximo lado

# Função principal para desenhar as formas
def main():
    turtle.speed(2)  # Define a velocidade de desenho
    turtle.hideturtle()

    # Instanciando e desenhando as formas
    circulo = Circulo()
    quadrado = Quadrado()

    circulo.desenhar()  # Desenha o círculo
    quadrado.desenhar()  # Desenha o quadrado

    turtle.done()  # Mantém a janela aberta após o desenho

if __name__ == "__main__":
    main()
