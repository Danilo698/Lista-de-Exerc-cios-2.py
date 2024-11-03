class Motor:
    def status(self):
        return "O motor está funcionando."

class Pneu:
    def status(self):
        return "Os pneus estão em boas condições."

class Veiculo(Motor, Pneu):
    def status(self):
        # Chamando diretamente o método status de cada classe base
        motor_status = Motor.status(self)  # Chama o status da classe Motor
        pneu_status = Pneu.status(self)    # Chama o status da classe Pneu
        return f"{motor_status}\n{pneu_status}"

# Testando a implementação
carro = Veiculo()
print(carro.status())
