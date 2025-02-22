def Caeser_Cipher():

    try:
        texto = input("Insira uma mensagem: ")
        salto = int(input("Insira um valor para salto lexicográfico: "))
        cipher = ''

        for char in texto:
            if char.isalpha() and char.islower():
                code = ord(char) + salto
                if code > ord('z'):
                    code += ord('a') - ord('z')   
                cipher += chr(code)
            elif char.isalpha() and char.isupper():
                code = ord(char) + salto
                if code > ord('Z'):
                    code += ord('A') - ord('Z')
                cipher += chr(code)
            else:
                cipher += char

        arquivo = open("cripto.txt", "w")
        arquivo.write(f"{cipher}")
    except Exception as e:
        msg = f'Erro: {e}, por favor, pressione [1] para tentar novamente, ou qualquer outra tecla para sair.'
        print(msg)
        resp = int(input())
        if resp == 1:
            Caeser_Cipher()
        else:
            exit()
if __name__ == '__main__':
    Caeser_Cipher()




