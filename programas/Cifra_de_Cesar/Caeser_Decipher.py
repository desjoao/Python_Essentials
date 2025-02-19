
# Abre o arquivo com o texto criptografado e atribuir o texto à uma variável.
txt = input("Insira o nome do arquivo que deseja abrir: ")
txt+=".txt"
try:
    cipher_file = open(txt, "r")
    for char in cipher_file:
        cipher = char
    texto = ''
except Exception:
    print("Arquivo não encontrado. \nDica: insira o nome do arquivo sem \".txt\"")
    exit()

# Descriptografa o texto lido utilizando a cifra de César ao inverso.
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char)-1
    if code < ord('A'):
        code = ord('Z')
    texto += chr(code)

# Retorna a impressão do texto descriptografado.
print(texto)
