texto = input("Insira uma mensagem: ")
cipher = ''

for char in texto:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char)+1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)


arquivo = open("cripto.txt", "w")
arquivo.write(f"{cipher}")


