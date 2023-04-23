class Automata():
    def __init__(self, text):
        self.__text = text
    def table(self):
        print('|--------|----------------------|\n|        |  Simbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
        print('|--------|-----------|----------|\n|  Q0    |    Q1     |    Q2    |\n|  Q1    |    Q1     |    Q2    |\n|  Q2    |    Q1     |    Q2    |')
        print('|--------|-----------|----------|')

    def secuencias(self):
        aceptation = ['Q1','Q2']
        state = 'Q0'
        print('State:', state)
        for i in range(len(self.__text)):
            if state == 'Q0':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q0 to Q1')
                    state = 'Q1'
                if self.__text[i] == 'b':
                    print('Transition from Q0 to Q2')
                    state = 'Q2'
                elif state == 'Q1':
                    print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q1 to Q1')
                    state = 'Q1'
                if self.__text[i] == 'b':
                    print('Transition from Q1 to Q2')
                    state = 'Q2'
            elif state == 'Q2':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q2 to Q1')
                    state = 'Q1'
                if self.__text[i] == 'b':
                    print('Transition from Q2 to Q2')
                    state = 'Q2'
            print('State:', state)

        if state in aceptation:
            print('ESTADO DE ACEPTACION ALCANZADO')
            return False
        else:
            print('NO SE ALCANZA A UN ESTADO DE ACEPTACIÓN. CADENA NO VÁLIDA.\n')
            return True

    def validacion(self):
        valid = ['a', 'b']
        for i in range(len(self.__text)):
            if not self.__text[i] in valid:
                print('CARACTER INVALIDO:', self.__text[i])
                return False
        return True

def main():
    text = input("INTRODUCIR CARACTER:")
    AFD = Automata(text)
    AFD.table()
    AFD.secuencias()
    AFD.validacion()
if __name__ == "__main__":
    main()
