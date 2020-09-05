class CorteLinear:
    def __init__(self, tam_disco = 3, barra = 6000):
        self.tam_disco = tam_disco
        self.barra = barra

    def aproveitamento(self):
        tamanho_corte = float(input("Tamanho da barra a ser cortada: "))
        qtd = int(input("Quantidade a ser cortada: "))
        calc_corte = qtd * (tamanho_corte + self.tam_disco)
        qtd_barra = calc_corte / self.barra
        if qtd_barra < 1:
            qtd_barra = 1
            resto = self.barra - tamanho_corte
        else:
            resto = self.barra % tamanho_corte
        print("Seram necessárias {} barras para cortar {} unidades de {} mm".format(round(qtd_barra), qtd, tamanho_corte))
        print("Sobraram {} peças de {} mm".format(round(qtd_barra), resto)+ '\n')
        return calc_corte

    def calculo_peso(self):
        calc_corte = self.aproveitamento()
        peso_m = float(input("Insira o peso por metro da barra: "))
        peso_t = (peso_m * self.barra) / 1000
        peso_todo = (peso_m * calc_corte) / 1000
        print("O peso total da barra é de {:.2f} Kg".format(peso_t))
        print("O peso total das barras é {:.2f} Kg".format(peso_todo))
        
