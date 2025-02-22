
# Abre o arquivo com o texto criptografado e atribuir o texto à uma variável.

def recebeTexto():
    txt = input("Insira o nome do arquivo que deseja abrir: ")
    try:
        cipher_file = open(txt, "r")
        cipher = cipher_file.read()
        Caeser_Decipher(cipher)
    except Exception:
        print("Arquivo não encontrado.")
        recebeTexto()

def Caeser_Decipher(cipher):

    # Descriptografa o texto lido utilizando a cifra de César ao inverso.
    texto = ''
    salto = int(input('Insira o valor do salto: '))
    for char in cipher:
        if char.isalpha() and char.islower():
            code = ord(char) - salto
            if code < ord('a'):
                code += ord('z') - ord('a')
            texto += chr(code)
        elif char.isalpha() and char.isupper():
            code = ord(char) - salto
            if code < ord('A'):
                code += ord('Z') - ord('A')
            texto += chr(code)
        else:
            texto +=char
    # Retorna a impressão do texto descriptografado.
    print(texto)

if __name__ == '__main__':
    recebeTexto()
