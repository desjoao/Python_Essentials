def entrada():
    try:
        entrada1 = input("Insira o primeiro texto: ")
        entrada2 = input("Insira o segundo texto: ")
        entrada1 = entrada1.upper()
        entrada2 = entrada2.upper()
        novaEntrada1 = novaEntrada2 = ''
        for char in entrada1:
            if char.isalnum():
                novaEntrada1 += char
        for char in entrada2:
            if char.isalnum():
                novaEntrada2 += char

        anagrama(novaEntrada1, novaEntrada2)

    except Exception as e:
        print (f'Um erro ocorreu: {e}')
        exit()

def anagrama(a, b):
    try:
        valor1 = valor2 = 0
        for char in a:
            valor1 += ord(char)
        for char in b:
            valor2 += ord(char)

        if valor1 == valor2 != 0:
            print('São anagramas.')
            exit()
        print('Não são anagramas.')

    except Exception as e:
        print(f'Um erro ocorreu: {e}.')
        exit()

if __name__ == '__main__':
    entrada()

