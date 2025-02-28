from datetime import date

class digit_of_life:
    def __init__(self) -> None:
        try:
            data = input("Insira a data de seu aniversário no formato 'DDMMAAAA': ")
            digito = int(data)
            while digito >= 10:
                aux = str(digito)
                digito = 0
                for char in aux:
                    digito += int(char)
            print(f'{digito} é o seu dígito da vida.')
        except Exception as e:
            print(f'Ocorreu um ero: {e}')

if __name__ == "__main__":
    digito = digit_of_life()


                    
                    
                

        
