
# métodos para calcular o valor da entrada inteira e da meia-entrada.
# Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.

# Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.

# Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
# Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.

class dados_conta:
    def __init__(self, dia_semana, hora):
        self.data = dia_semana
        self.horario = hora

    def deposito(self, seg_ter_qui, qua, sex_sab_dom):
        if self.data == seg_ter_qui:
            valor = 16
            if 17 <= self.horario <= 23.983:
                valor += valor/2
            else:
                valor = 16

        if self.data == seg_ter_qui:
            valor = 20
            if 17 <= self.horario <= 23.983:
                valor += valor/2
                print("vai pagar")
            else:
                valor = 20
    