import traceback

class Stack():
    """
    Classe criada para definir métodos utilizados para se criar uma pilha.
    """

    def __init__(self):
        self.__stack = []

    def push(self, valor):
        try:
            self.__stack.append(valor)
        except Exception:
            msg = 'Erro em adicionar valor à pilha.'
            print(msg + traceback.format_exc())

    def pop(self):
        try:
            valor = self.__stack[-1]
            del self.__stack[-1]
        except Exception:
            msg = 'Erro em retirar valor da pilha.'
            print(msg + traceback.format_exc())
        return valor

    def print_stack(self):
        try:
            return self.__stack
        except Exception:
            msg = 'Erro em imprimir a pilha.'
            print(msg + traceback.format_exc())

