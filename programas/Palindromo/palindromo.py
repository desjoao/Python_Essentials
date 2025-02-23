def entrada():
    try:
        string = input("Insira um palindromo: ")
        string = string.upper()
        novaString = ''
        for char in string:
            if char.isalnum():
                novaString += char
        palindromo(novaString)
    except Exception as e:
        print(f'Um erro ocorreu: {e}')
        exit()

def palindromo(string):
    try:
        i = 0
        j = len(string)-1
        while i < j:
            if string[i] != string[j]:
                print("Não é um palíndromo.")
                exit()
            i+=1 
            j-=1
        print("È um palíndromo.")

    except Exception as e:
        print(f'Um erro ocorreu: {e}.')
        exit()
if __name__ == "__main__":
    entrada()

