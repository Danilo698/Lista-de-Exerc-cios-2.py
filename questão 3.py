import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

def main():
    # Criar uma tela
    screen = turtle.Screen()

    # Criar um objeto Turtle
    t = turtle.Turtle()

    # Criar instâncias da classe Ponto
    ponto1 = Ponto(100, 100)
    ponto2 = Ponto(-100, -100)

    # Usar goto() para mover a tartaruga para os pontos
    t.goto(ponto1.x, ponto1.y)
    t.goto(ponto2.x, ponto2.y)

    # Encerrar a tela ao clicar
    screen.exitonclick()

if __name__ == "__main__":
    main()
