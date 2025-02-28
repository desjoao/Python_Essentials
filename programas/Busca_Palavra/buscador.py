class Buscador:
    def __init__(self):
        palavra_1 = input('Insira o primeiro texto: ')
        palavra_2 = input('Insira a palavra que procura: ')
        if self.buscador(palavra_1, palavra_2):
            print('sim')
            exit()
        print('não')

    def buscador(self, palavra_1, palavra_2):
        palavra_1 = palavra_1.upper()
        palavra_2 = palavra_2.upper()
        for i in palavra_1:
            for j in palavra_2:
                if i == j:
                    pos = int(palavra_1.index(j))
                    palavra_1 = palavra_1[pos:]
                    if len(palavra_1)-1 == 0:
                        return True
                    continue
        return False

if __name__ == "__main__":
    try:
        Buscador()
    except Exception as e:
        print(f'Erro: {e}')





